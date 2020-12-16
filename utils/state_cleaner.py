# Import necessary modules...
from states import state_countries, aus_states, usa_states, cad_states, jpn_states
from errors import ERROR_TYPE


# Function to validate and clean states for required countries...
def state_cleaner(data):
    """ Clean invalid states for those rows which contain a country that requires state input.

    Notes:
        Use AFTER country column is clean.
    """

    # Cropping the data and setting it into lists in standardised format...
    d_states = data['State'].astype(str)
    d_states = list(d_state.map(lambda x: x.lower()))

    # Initialize empty list for clean states...
    c_states = []

    # Iterate over countries to validate states and populate c_states with clean states...
    for i in range(0, len(data['State'])):
        # Select clean country to validate state for...
        v_country = data['Country'].iloc[i]

        # Select country and its respective dictionary to clean states and note errors if invalid...
        if v_country in state_countries:

            # Clean from United States dictionary..
            if v_country == 'United States':
                if d_states[i] in usa_states.keys():
                    c_states.append(usa_states[d_states[i]])
                else:
                    c_states.append(d_states[i])
                    data['ERROR'].loc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['state_error']

            # Clean from Canada's dictionary...
            elif v_country == 'Canada':
                if d_states[i] in cad_states.keys():
                    c_states.append(cad_states[d_states[i]])
                else:
                    c_states.append(d_states[i])
                    data['ERROR'].loc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['state_error']

            # Clean from Australia's dictionary...
            elif v_country == 'Australia':
                if d_states[i] in aus_states.keys():
                    c_states.append(aus_states[d_states[i]])
                else:
                    c_states.append(d_states[i])
                    data['ERROR'].loc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['state_error']

            # Clean from Japan's dictionary...
            else:
                if d_states[i] in jpn_states.keys():
                    c_states.append(jpn_states[d_states[i]])
                else:
                    c_states.append(d_states[i])
                    data['ERROR'].loc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['state_error']

                    # If not in state countries then leave it as it is...
        else:
            c_states.append(data['State'].iloc[i])

    # Substitute states column with clean values...
    data['State'] = c_states

    return data
