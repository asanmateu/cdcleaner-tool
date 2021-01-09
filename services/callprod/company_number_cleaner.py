from queries import query_company_numbers
from columns import COMPANY_NUMBER, ALERT
from designer_id import DESIGNER_ID
from alerts import ALERT_TYPE


def company_number_cleaner(data, designer_id: int = DESIGNER_ID):
    """ Checks if input company number exists on the designer's settings. If it does not exist removes the current
    value and flags an alert."""

    # Check if column exists in template provided...
    if COMPANY_NUMBER in data.columns:

        # Unpack customer group dictionary from prod...
        company_number_names, company_number_codes = query_company_numbers(designer_id)

        # Check if input element is either on the list of codes or the list of names
        for i, row in data.iterrows():
            # If value is not in either list then flag an alert and remove the value...
            if (row[COMPANY_NUMBER] not in company_number_names) and \
                    (row[COMPANY_NUMBER] not in company_number_codes):
                data[ALERT].iloc[i] = str(row[ALERT]) + \
                                        f"{row[COMPANY_NUMBER]}" + ALERT_TYPE['company_number_setup']
                data[COMPANY_NUMBER].iloc[i] = ""

    return data
