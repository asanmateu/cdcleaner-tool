from alerts import ALERT_TYPE
from lengths import LIMITS


def discount_cleaner(data):
    """Validates discount's field format removing any percentage symbols and checks its length. """

    for i, row in data.iterrows():
        # If there is any % symbol strip it...
        if row['Discount'].count('%') > 1:
            data['Discount'].iloc[i] = data['Discount'].iloc[i].strip('%')

        # If length exceeds limit note an alert and remove the value...
        if len(str(row['Discount'])) > LIMITS['discount']:
            data['ALERT'].iloc[i] = str(row['ALERT']) + f"{row['Discount']}" + ALERT_TYPE['discount_length']
            data['Discount'].iloc[i] = ""

    return data
