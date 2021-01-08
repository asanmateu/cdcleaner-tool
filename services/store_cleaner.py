# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS
from alerts import ALERT_TYPE


def store_cleaner(data):
    """ Copy alias name if store name is empty and vice-versa or omit """

    # For each row check if store name can be cleaned
    for i, row in data.iterrows():
        # If no store name found then copy customer name...
        if row['Store Name'] == "" and row['Customer Name'] != "":
            data['Store Name'].iloc[i] = row['Customer Name']
        # If no customer name is found copy store name...
        elif row['Store Name'] != "" and row['Customer Name'] == "":
            data['Customer Name'].iloc[i] = row['Store Name']
        # If no customer name nor store name then note an error...
        else:
            data['ERROR'].iloc[i] = str(row['ERROR']) + ERROR_TYPE['store_error']

        # If length exceeds the limit note an alert and remove value...
        if len(str(row['Store Name'])) > LIMITS['store_name']:
            data['ALERT'].iloc[i] = str(row['ALERT']) + f"{row['Store Name']}" + ALERT_TYPE['store_length']
            data['Store Name'].iloc[i] = ""

    return data
