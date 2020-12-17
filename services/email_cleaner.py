# Import necessary modules...
from library import re
from errors import ERROR_TYPE
from alerts import ALERT_TYPE


def email_cleaner(data):
    """Check if there are multiple emails in the email cell and add the extra
    emails to the additional emails column"""

    # Pattern to search email matches by...
    regex = r"\w.+@\S+"

    # Iterate over the email column to clean those cells in which there is more than 1 email...
    for i in range(0, len(data['Email'])):

        if str(data['Email'].iloc[i]).count('@') >= 1:
            emails = re.findall(regex, str(data['Email'].iloc[i]))

            # Make sure split works if there is a ; too...
            if emails[0].count(',') >= 1:
                emails = re.split(r", ", emails[0])
            elif emails[0].count(';') >= 1:
                emails = re.split(r"; ", emails[0])
            else:
                emails = re.split(r" ", emails[0])

            # Trim whitespaces to clean emails format...
            v_emails = [e.strip(" ") for e in emails]

            # Append valid email input to email column...
            data['Email'].iloc[i] = v_emails[0]

            # Prepare to append extra emails into additional emails column
            ad_emails = ", ".join(v_emails[1:])

            # Add additional emails to string or just sub in if the are no emails yet...
            if str(data['Additional Emails'].iloc[i]).count('@') >= 1:
                data['Additional Emails'].iloc[i] = str(data['Additional Emails'].iloc[i]) + ad_emails

                # Check there's only one left in email column otherwise there might be one not caught by regex..
                if str(data['Email'].iloc[i]).count('@') >= 1:
                    data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['email_error']

            else:
                data['Additional Emails'].iloc[i] = ad_emails

        else:
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE['email_missing']

    return data
