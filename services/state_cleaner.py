# Import necessary modules...
from states import state_countries, aus_states, usa_states, cad_states, jpn_states
from errors import ERROR_TYPE


# Function to validate and clean states for required countries...
def state_cleaner(data):
    """ Note an error if country requires state and the state input is invalid.

    Notes:
        Use AFTER country column is clean.
    """

    for i in range(len(data['State'])):
        reference_country = data['Country'].iloc[i].title()
        reference_state = data['State'].iloc[i].lower()

        # If country is in state countries check if the input state is valid otherwise not error...
        if reference_country in state_countries:
            if reference_country == 'United States' and reference_state in usa_states.keys():
                pass
            elif reference_country == 'Canada' and reference_state in cad_states.keys():
                pass
            elif reference_country == 'Australia' and reference_state in aus_states.keys():
                pass
            elif reference_country == 'Australia' and reference_state in jpn_states.keys():
                pass
        else:
            data['ERROR'].loc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['state_error']

    return data
