# Import necessary modules...
from errors import ERROR_TYPE


def zipcode_cleaner(data):
    """ Notes an error if country is United States and zip code is empty, otherwise do nothing.

    Notes:
        Run after cleaning countries and states.
    """

    for i in range(0, len(data['Zip'])):
        if data['Country'].iloc[i] == 'United States' and data['Zip'].iloc[i] == "":
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['zipcode_error']

    return data
