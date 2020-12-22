# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS


def store_cleaner(data):
    """ Copy alias name if store name is empty and vice-versa or omit """

    # For each row check if store name can be cleaned
    for i in range(len(data['Store Name'])):
        # If no store name found then copy customer name...
        if data['Store Name'].iloc[i] == "" and data['Customer Name'].iloc[i] != "":
            data['Store Name'].iloc[i] = data['Customer Name'].iloc[i]
        # If no customer name is found copy store name...
        elif data['Store Name'].iloc[i] != "" and data['Customer Name'].iloc[i] == "":
            data['Customer Name'].iloc[i] = data['Store Name'].iloc[i]
        # If no customer name nor store name then note an error...
        else:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['store_error']

        # If length exceeds the limit note an error...
        if len(str(data['Store Name'].iloc[i])) > LIMITS['store_name']:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['store_length']

    return data
