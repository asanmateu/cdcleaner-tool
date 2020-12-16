from addtypes import valid_types
from errors import ERROR_TYPE


def address_type_cleaner(data):
    """ Clean valid address types. Make sure that there is only one B and one S per customer
    code unless there are unique address codes. Address 1 cannot be empty, if it is notes error.

    Notes:
        Run before doing any other work on addresses. Make sure store_cleaner has been run.
    """

    # Formatting data for lookups...
    d_addtypes = data['Address Type'].astype(str)
    d_addtypes = list(d_addtypes.map(lambda x: x.lower()))

    # Empty list for validated values...
    c_addtypes = []

    # # Iterate over input address type list and populate empty list with clean values ...
    for i in range(0, len(data['Address Type'])):
        if d_addtypes[i] in valid_types.keys():
            # Append valid address type format to raw_clean...
            c_addtypes.append(valid_types[d_addtypes[i]])

        else:
            # Leave invalid address type and note error for ommit generator...
            c_addtypes.append(d_addtypes[i])
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['address_type_error']

    # Substitute valid values into original address type column...
    data['Address Type'] = c_addtypes

    return data


def address_cleaner(data):
    """ Address 1 cannot be empty, if it is notes error. """

    # Note error if Address 1 is empty...
    for i in range(0, len(data['Address 1'])):
        if data['Address 1'].iloc[i] == "":
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['address_error']
        else:
            pass

    return data


def address_code_cleaner(data):
    """ Make sure that there is only one B and one S per customer code unless there are
    unique address codes. Only note error on extra ones. """

    # Separate rows that are unique in terms of the subsets specified from the duplicates...
    uniques = data.drop_duplicates(subset=['Customer Code', 'Store Name', 'Address Type', 'Address Code'])
    duplicates = data.iloc[list(set(data.index) - set(uniques.index))]

    # Note error if connections has a second B or S address type without unique address code...
    for i in range(0, len(duplicates)):
        index = duplicates.index[i]
        data['ERROR'].iloc[index] = str(data['ERROR'].iloc[index]) + ERROR_TYPE['address_code_error']

    return data
