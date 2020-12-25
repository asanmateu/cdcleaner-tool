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
    countries = [*map(lambda x: x.lower(), data['Country'])]

    # Iterate over input country list sub with valid country...
    for i, row in data.iterrows():
        reference_country = countries[i]
        # If input country is not in valid entries dictionary keys then note invalid country error...
        if reference_country not in country_dict.keys():
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['country_error']
        # If input country is in valid country dictionary keys then replace it by the corresponding value...
        else:
            row['Country'] = country_dict.get('reference_country')

    return data
