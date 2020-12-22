from errors import ERROR_TYPE
from lengths import LIMITS


def discount_cleaner(data):
    """Validates discount's field format removing any percentage symbols and checks its length. """

    for i in range(len(data['Discount'])):
        # If there is any % symbol strip it...
        if data['Discount'].iloc[i].count('%') > 1:
            data['Discount'].iloc[i] = data['Discount'].iloc[i].strip('%')

        # If length exceeds limit throw error...
        if len(str(data['Discount'].iloc[i])) > LIMITS['discount']:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['discount_length']

    return data
