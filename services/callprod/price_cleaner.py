# Import necessary modules...



def price_cleaner(data):
    """ Note an error if row has no pricing data. Default their only price type if there is only one.

    Notes:
        This function could also check on database if it is a valid price type...

    """

    for i in range(0, len(data['Price Label'])):
        if data['Price Label'].iloc[i] == '':
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + 'Invalid price label; '
        else:
            pass

    return data
