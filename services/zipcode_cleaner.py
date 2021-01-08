# Import necessary modules...
from errors import ERROR_TYPE
from alerts import ALERT_TYPE
from lengths import LIMITS


def zipcode_cleaner(data):
    """ Notes an error if country is United States and zip code is empty, otherwise do nothing.

    Notes:
        Run after cleaning countries and states.
    """

    for i, row in data.iterrows():
        # If zipcode is empty for united states countries then note an error...
        if row['Country'] == 'United States' and row['Zip'] == "":
            data['ERROR'].iloc[i] = str(row['ERROR']) + ERROR_TYPE['zip_error']

        # If zipcode exceeds character limit then note an alert and remove the value...
        if len(str(row['Zip'])) > LIMITS['zip']:
            data['ALERT'].iloc[i] = str(row['ALERT']) + f"{row['Zip']}" + ALERT_TYPE['zip_length']
            data['Zip'].iloc[i] = ""

    return data
