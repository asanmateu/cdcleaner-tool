# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS


def zipcode_cleaner(data):
    """ Notes an error if country is United States and zip code is empty, otherwise do nothing.

    Notes:
        Run after cleaning countries and states.
    """

    for i in range(len(data['Zip'])):
        # If zipcode is empty for united states countries then note an error...
        if data['Country'].iloc[i] == 'United States' and data['Zip'].iloc[i] == "":
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['zip_error']

        # If zipcode exceeds character limit then note an error...
        if len(str(data['Zip'])) > LIMITS['zip']:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['zip_length']

    return data
