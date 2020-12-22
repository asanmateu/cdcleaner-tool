# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS


def city_cleaner(data):
    """ Note an error if city input is empty otherwise pass. """

    for i in range(len(data['City'])):
        # If city is empty note an error for invalid city input...
        if data['City'].iloc[i] == '':
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['city_error']

        # If city length exceeds character limit note an error...
        if len(str(data['City'].iloc[i])) > LIMITS['city']:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['city_length']

    return data

