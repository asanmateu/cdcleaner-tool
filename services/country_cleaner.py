# Necessary modules...
from countries import country_dict
from errors import ERROR_TYPE


# Function to validate and clean country column from input DataFrame...
def country_cleaner(data):
    """Cleans invalid countries from input file if they
    meet the minimum requirements to be cleaned.

    Notes:
        I recommend you use this one first.
    """

    # Iterate over input country list sub with valid country...
    for i in range(len(data['Country'])):
        reference_country = data['Country'].iloc[i].lower()
        # If input country is not in valid entries dictionary keys then note invalid country error...
        if reference_country not in country_dict.keys():
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['country_error']
        # If input country is in valid country dictionary keys then replace it by the corresponding value...
        else:
            data['Country'].iloc[i] = country_dict[reference_country]

    return data
