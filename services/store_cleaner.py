# Import necessary modules...
from errors import ERROR_TYPE


def store_cleaner(data):
    """ Copy alias name if store name is empty and vice-versa or omit """

    # For each row check if store name can be cleaned
    for i in range(len(data['Store Name'])):
        if data['Store Name'].iloc[i] == "" and data['Customer Name'].iloc[i] != "":
            data['Store Name'].iloc[i] = data['Customer Name'].iloc[i]
        elif data['Store Name'].iloc[i] != "" and data['Customer Name'].iloc[i] == "":
            data['Customer Name'].iloc[i] = data['Store Name'].iloc[i]
        else:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['store_error']

    return data
