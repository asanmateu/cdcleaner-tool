from queries import query_company_numbers
from designer_id import DESIGNER_ID
from alerts import ALERT_TYPE


def company_number_cleaner(data, designer_id: int = DESIGNER_ID):
    """ Checks if input company number exists on the designer's settings. If it does not exist removes the current
    value and flags an alert."""

    # Check if column exists in template provided...
    if "Company Number Code" in data.columns:

        # Unpack customer group dictionary from prod...
        company_number_names, company_number_codes = query_company_numbers(designer_id)

        # Check if input element is either on the list of codes or the list of names
        for i, row in data.iterrows():
            # If value is not in either list then flag an alert and remove the value...
            if (row['Company Number Code'] not in company_number_names) and \
                    (row['Company Number Code'] not in company_number_codes):
                data['ALERT'].iloc[i] = str(row['ALERT']) + \
                                        f"{row['Company Number Code']}" + ALERT_TYPE['company_number_setup']
                data['Company Number Code'].iloc[i] = ""

    return data
