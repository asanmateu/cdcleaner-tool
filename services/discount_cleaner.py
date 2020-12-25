from errors import ERROR_TYPE
from lengths import LIMITS


def discount_cleaner(data):
    """Validates discount's field format removing any percentage symbols and checks its length. """

    for i, row in data.iterrows():
        # If there is any % symbol strip it...
        if row['Discount'].count('%') > 1:
            row['Discount'] = row['Discount'].strip('%')

        # If length exceeds limit throw error...
        if len(str(row['Discount'])) > LIMITS['discount']:
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['discount_length']

    return data
