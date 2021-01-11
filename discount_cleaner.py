from columns import DISCOUNT, ALERT
from alerts import ALERT_TYPE
from lengths import LIMITS


def discount_cleaner(data):
    """Validates discount's field format removing any percentage symbols and checks its length. """

    for i, row in data.iterrows():
        # If there is any % symbol strip it...
        if row[DISCOUNT].count('%') > 1:
            data[DISCOUNT].iloc[i] = data[DISCOUNT].iloc[i].strip('%')

        # If length exceeds limit note an alert and remove the value...
        if len(str(row[DISCOUNT])) > LIMITS['discount']:
            data[ALERT].iloc[i] = str(row[ALERT]) + f"{row[DISCOUNT]}" + ALERT_TYPE['discount_length']
            data[DISCOUNT].iloc[i] = ""

    return data
