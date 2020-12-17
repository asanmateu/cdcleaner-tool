# Import necessary modules...
from errors import ERROR_TYPE


def city_cleaner(data):
    """ Note an error if city input is empty otherwise pass. """

    for i in range(0, len(data['City'])):
        # Note error if value is empty otherwise leave as it is...
        if data['City'].iloc[i] == '':
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['city_error']

    return data

