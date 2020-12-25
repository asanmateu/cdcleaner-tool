# Import necessary modules...
from library import re
from errors import ERROR_TYPE
from alerts import ALERT_TYPE
from lengths import LIMITS


def email_cleaner(data):
    """Check if there are multiple emails in the email cell and add the extra
    emails to the additional emails column"""

    # Pattern to search email matches by...
    regex = r"\w.+@\S+"

    # Iterate over the email column to clean those cells in which there is more than 1 email...
    for i, row in data.iterrows():

        if str(row['Email']).count('@') >= 1:
            input_emails = re.findall(regex, str(row['Email']))

            # Make sure split works if there is a ; too...
            if input_emails[0].count(',') >= 1:
                input_emails = re.split(r", ", input_emails[0])
            elif input_emails[0].count(';') >= 1:
                input_emails = re.split(r"; ", input_emails[0])
            else:
                input_emails = re.split(r" ", input_emails[0])

            # Trim whitespaces to clean emails format...
            valid_emails = [e.strip(" ") for e in input_emails]

            # Append valid email input to email column...
            row['Email'] = valid_emails[0]

            # Append extra emails into additional emails column
            additional_emails = ", ".join(valid_emails[1:])
            row['Additional Emails'] = str(row['Additional Emails']) + additional_emails

            # Check there's only one left in email column otherwise there might be one not caught by regex..
            if str(row['Email']).count('@') >= 1:
                row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['email_error']

        else:
            row['ALERT'] = str(row['ALERT']) + ALERT_TYPE['email_missing']

        if len(str(row['Email'])) > LIMITS['email']:
            row['ERROR'] = str(row['ERROR']) + ALERT_TYPE['email_length']

    return data
