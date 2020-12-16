# Necessary modules...
from countries import country_dict
from errors import ERROR_TYPE

# Function to validate and clean country column from input DataFrame...
def country_cleaner(data):
    """Cleans invalid countries from input file if they
    enter the minimum requirements to be cleaned.

    Args:
        data (pandas DataFrame): original file.
    Returns:
        data (pandas DataFrame): country field clean.
    Notes:
        I recommend you use this one first.
    """

    # Cropping the data and setting it into lists in standardised format...
    d_country = data['Country'].astype(str)
    d_country = list(d_country.map(lambda x: x.lower()))

    # Empty list to insert validated countries...
    c_country = []

    # Iterate over input country list sub with valid country...
    for i in range(0, len(d_country)):
        if d_country[i] in country_dict.keys():
            # Append valid country format to raw_clean...
            c_country.append(country_dict[d_country[i]])

        else:
            # Leave invalid countries and note error for ommit generator...
            c_country.append(d_country[i])
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['country_error']

    # Substitute valid values into original country column...
    data['Country'] = c_country

    return data
