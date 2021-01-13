# Import necessary modules...
from constants import ERROR_TYPE, ALERT_TYPE, LIMITS, ZIP, COUNTRY, ALERT, ERROR


def zipcode_cleaner(df):
    """ Notes an error if country is United States and zip code is empty, otherwise do nothing.

    Notes:
        Run after cleaning countries and states.
    """

    for i, row in df.iterrows():
        # If zipcode is empty for united states countries then note an error...
        if row[COUNTRY] == 'United States' and row[ZIP] == "":
            df[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['zip_error']

        # If zipcode exceeds character limit then note an alert and remove the value...
        if len(str(row[ZIP])) > LIMITS['zip']:
            df[ALERT].iloc[i] = str(row[ALERT]) + f"{row[ZIP]}" + ALERT_TYPE['zip_length']
            df[ZIP].iloc[i] = ""

    return df
