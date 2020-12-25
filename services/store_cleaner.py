# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS


def store_cleaner(data):
    """ Copy alias name if store name is empty and vice-versa or omit """

    # For each row check if store name can be cleaned
    for i, row in data.iterrows():
        # If no store name found then copy customer name...
        if row['Store Name'] == "" and row['Customer Name'] != "":
            row['Store Name'] = row['Customer Name']
        # If no customer name is found copy store name...
        elif row['Store Name'] != "" and row['Customer Name'] == "":
            row['Customer Name'] = row['Store Name']
        # If no customer name nor store name then note an error...
        else:
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['store_error']

        # If length exceeds the limit note an error...
        if len(str(row['Store Name'])) > LIMITS['store_name']:
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['store_length']

    return data
