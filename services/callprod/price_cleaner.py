# Import necessary modules...
from queries import query_price_types
from alerts import ALERT_TYPE
from errors import ERROR_TYPE


def price_type_cleaner(data):
    """ Note an error if row has no pricing data. Default their only price type if there is only one.

    Notes:
        This function could also check on database if it is a valid price type...

    """

    for i in range(0, len(data['Price Label'])):
        # Get a tuple with wholesale currency, price label, retail currency as reference
        reference_price_type =
        if data['Price Label'].iloc[i] == '':
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['price_type_error']
        elif

    return data
