from prod import query_company_numbers
from constants import COMPANY_NUMBER, ALERT, DESIGNER_ID, ALERT_TYPE


def company_number_cleaner(df, designer_id: int = DESIGNER_ID):
    """ Checks if input company number exists on the designer's settings. If it does not exist removes the current
    value and flags an alert."""

    # Check if column exists in template provided...
    if COMPANY_NUMBER in df.columns:

        # Unpack customer group dictionary from prod...
        company_number_names, company_number_codes = query_company_numbers(designer_id)

        # Check if input element is either on the list of codes or the list of names
        for i, row in df.iterrows():
            # If input value is not null:
            if row[COMPANY_NUMBER] != "":
                # If value is not in either list then flag an alert and remove the value...
                if (row[COMPANY_NUMBER] not in company_number_names) and \
                        (row[COMPANY_NUMBER] not in company_number_codes):
                    df[ALERT].iloc[i] = str(row[ALERT]) + \
                                            f"{row[COMPANY_NUMBER]}" + ALERT_TYPE['company_number_setup']
                    df[COMPANY_NUMBER].iloc[i] = ""

    return df
