# Import necessary modules...
from columns import STORE_NAME, CUSTOMER_NAME, ALERT, ERROR
from errors import ERROR_TYPE
from lengths import LIMITS
from alerts import ALERT_TYPE


def store_cleaner(df):
    """ Copy alias name if store name is empty and vice-versa or omit """

    # For each row check if store name can be cleaned
    for i, row in df.iterrows():
        # If no store name found then copy customer name...
        if row[STORE_NAME] == "" and row[CUSTOMER_NAME] != "":
            df[STORE_NAME].iloc[i] = row[CUSTOMER_NAME]
        # If no customer name is found copy store name...
        elif row[STORE_NAME] != "" and row[CUSTOMER_NAME] == "":
            df[STORE_NAME].iloc[i] = row[STORE_NAME]
        # If no customer name nor store name then note an error...
        elif row[STORE_NAME] == "" and row[CUSTOMER_NAME] == "":
            df[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['store_error']

        # If length exceeds the limit note an alert and remove value...
        if len(str(row[STORE_NAME])) > LIMITS['store_name']:
            df[ALERT].iloc[i] = str(row[ALERT]) + f"{row[STORE_NAME]}" + ALERT_TYPE['store_length']
            df[STORE_NAME].iloc[i] = ""

    return df
