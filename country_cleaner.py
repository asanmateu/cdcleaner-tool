# Necessary modules...
from columns import ERROR, COUNTRY
from countries import country_dict
from errors import ERROR_TYPE


# Function to validate and clean country column from input DataFrame...
def country_cleaner(df):
    """Cleans invalid countries from input file if they
    meet the minimum requirements to be cleaned.

    Notes:
        I recommend you use this one first.
    """
    countries = [*map(lambda x: x.lower(), df[COUNTRY])]

    # Iterate over input country list sub with valid country...
    for i, row in df.iterrows():
        reference_country = countries[i]
        # If input country is not in valid entries dictionary keys then note invalid country error...
        if reference_country not in country_dict.keys():
            df[ERROR].iloc[i] = str(row[ERROR]) + f"{reference_country}: " + ERROR_TYPE['country_error']
        # If input country is in valid country dictionary keys then replace it by the corresponding value...
        else:
            df[COUNTRY].iloc[i] = country_dict.get(reference_country)

    return df
