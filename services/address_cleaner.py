from dictionaries import valid_types
from constants import ERROR_TYPE, ALERT_TYPE, ERROR, ALERT, ADDRESS_TYPE, ADDRESS_1, ADDRESS_2, \
    ADDRESS_CODE, STORE_NAME, CUSTOMER_CODE, LIMITS


def address_type_cleaner(df):
    """ Clean valid address types. Make sure that there is only one B and one S per customer
    code unless there are unique address codes. Address 1 cannot be empty, if it is notes error.

    Notes:
        Run before doing any other work on addresses. Make sure store_cleaner has been run.
    """
    address_types = [*map(lambda x: x.lower(), data[ADDRESS_TYPE])]

    # # Iterate over input address type list and populate empty list with clean values ...
    for i, row in df.iterrows():
        reference_address_type = address_types[i]
        if reference_address_type not in valid_types.keys():
            df[ERROR].iloc[i] = str(row[ERROR]) + f"{reference_address_type}" + ERROR_TYPE['address_type_error']
        else:
            df[ADDRESS_TYPE].iloc[i] = valid_types[reference_address_type]

    return df


def address_cleaner(df):
    """ Address 1 cannot be empty, if it is notes error. Also, validates Address 1 and 2 lengths
    throwing an alert if lengths are exceeded. """

    for i, row in df.iterrows():
        # If address 1 is empty then note an error...
        if row[ADDRESS_1] == "":
            df[ALERT].iloc[i] = str(row[ALERT]) + ALERT_TYPE['address_1_missing']

        # If Address 1 exceeds the character limit then note an alert and remove the value...
        if len(str(row[ADDRESS_1])) > LIMITS['address_1']:
            df[ERROR].iloc[i] = str(row[ERROR]) + f"{row[ADDRESS_1]}" + ERROR_TYPE['address_1_length']

        # If Address 1 exceeds the character limit then note an alert and remove the value...
        if len(str(row[ADDRESS_2])) > LIMITS['address_2']:
            df[ERROR].iloc[i] = str(row[ERROR]) + f"{row[ADDRESS_2]}" + ERROR_TYPE['address_2_length']

    return df


def address_code_cleaner(df):
    """ Make sure that there is only one B and one S per customer code unless there are
    unique address codes. Only note error on extra ones. """

    # Separate rows that are unique in terms of the subsets specified from the duplicates...
    uniques = df.drop_duplicates(subset=[CUSTOMER_CODE, STORE_NAME, ADDRESS_TYPE, ADDRESS_CODE])
    duplicates = df.iloc[list(set(df.index) - set(uniques.index))]

    # Note error if connections has a second B or S address type without unique address code...
    for i in range(len(duplicates)):
        index = duplicates.index[i]
        df[ERROR].iloc[index] = str(df[ERROR].iloc[index]) + ERROR_TYPE['address_code_error']

        # If address code exceeds the character limit then note an error...
        if len(df[ADDRESS_CODE].iloc[i]) > LIMITS['address_code']:
            df[ERROR].iloc[i] = str(df[ERROR].iloc[i]) + ERROR_TYPE['address_code_length']

    return df
