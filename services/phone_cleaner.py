from alerts import ALERT_TYPE
from lengths import LIMITS


def phone_cleaner(data):
    """ Remove value if it exceeds the maximum length limit. Set an alert in this case.
    If it does not exceed the maximum length limit then does nothing."""

    for i, row in data.iterrows():
        # If phone field exceed maximum character limit then note alert and remove value...
        if len(str(row['Phone'])) > LIMITS['phone']:
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + f"{row['Phone']}" + ALERT_TYPE['phone_length']
            data['Phone'].iloc[i] = ""

    return data
