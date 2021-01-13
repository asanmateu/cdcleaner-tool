# Import necessary modules...
from dictionaries import state_countries, aus_states, usa_states, cad_states, jpn_states
from constants import COUNTRY, STATE, ERROR, ALERT, ERROR_TYPE, ALERT_TYPE, LIMITS


# Function to validate and clean states for required countries...
def state_cleaner(df):
    """ Note an error if country requires state and the state input is invalid.

    Notes:
        Use AFTER country column is clean.
    """

    countries = [*map(lambda x: x.title(), df[COUNTRY])]
    states = [*map(lambda x: x.lower(), df[STATE])]

    for i, row in df.iterrows():
        reference_country = countries[i]
        reference_state = states[i]

        # If country is in state countries check if the input state is valid otherwise not error...
        if reference_country in state_countries:
            if ((reference_country == 'United States') and (reference_state not in usa_states.keys())) or \
                    ((reference_country == 'Canada') and (reference_state not in cad_states.keys())) or \
                    ((reference_country == 'Australia') and (reference_state not in aus_states.keys())) or \
                    ((reference_country == 'Japan') and (reference_state not in jpn_states.keys())):
                df[ERROR].iloc[i] = str(row[ERROR]) + f"{reference_state}: " + ERROR_TYPE['state_error']

        # If length exceeds the limit note an alert and remove the value...
        if len(str(row[STATE])) > LIMITS[STATE]:
            df[ALERT].iloc[i] = str(row[ALERT]) + f"{row[STATE]}" + ALERT_TYPE['state_length']
            df[STATE].iloc[i] = ""

    return df
