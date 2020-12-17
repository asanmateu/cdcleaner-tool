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
    for i in range(0, len(data['Country'])):
        reference_country = data['Country'].iloc[i].lower()
        if reference_country not in country_dict.keys():
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['country_error']
        else:
            data['Country'].iloc[i] = country_dict[reference_country]

    return data
