# Import necessary modules...
from columns import EMAIL, ALERT, ERROR, ADDITIONAL_EMAILS
from library import re
from myutils import strip_lst
from errors import ERROR_TYPE
from alerts import ALERT_TYPE
from lengths import LIMITS


def email_cleaner(data):
    """Check if there are multiple emails in the email cell and add the extra
    emails to the additional emails column"""

    # Pattern to search email matches by...
    regex = r"[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+.[a-zA-Z.]*"

    # Iterate over the email column to clean those cells in which there is more than 1 email...
    for i, row in data.iterrows():
        # If more than one email is found then find them and clean them...
        if str(row[EMAIL]).count('@') >= 1:
            input_emails = re.findall(regex, str(row[EMAIL]))

            # Trim whitespaces to clean input email format...
            emails = strip_lst(input_emails)

            # Append valid email input to email column...
            data[EMAIL].iloc[i] = emails[0]

            # Append extra emails into additional emails column delimited with ","...
            additional_emails = ";".join(emails[1:])
            data[ADDITIONAL_EMAILS].iloc[i] = str(row[ADDITIONAL_EMAILS]) + ";" + additional_emails

            # Check there's only one left in email column otherwise there might be one not caught by regex..
            if str(row[EMAIL]).count('@') >= 1:
                data[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['email_error']

        else:
            data[ALERT].iloc[i] = str(row[ALERT]) + ALERT_TYPE['email_missing']

        # If email field exceeds length limit after cleaning note alert and remove value...
        if len(str(row[EMAIL])) > LIMITS['email']:
            data[ALERT].iloc[i] = str(row[ALERT]) + f"{row[EMAIL]}" + ALERT_TYPE['email_length']
            data[EMAIL].iloc[i] = ""

    return data
