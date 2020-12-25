# Import necessary modules...
from errors import ERROR_TYPE
from lengths import LIMITS


def city_cleaner(data):
    """ Note an error if city input is empty otherwise pass. """

    for i, row in data.iterrows():
        # If city is empty note an error for invalid city input...
        if row['City'] == '':
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['city_error']

        # If city length exceeds character limit note an error...
        if len(str(row['City'])) > LIMITS['city']:
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['city_length']

    return data

