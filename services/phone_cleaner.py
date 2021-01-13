from constants import PHONE, ALERT, ALERT_TYPE, LIMITS


def phone_cleaner(df):
    """ Remove value if it exceeds the maximum length limit. Set an alert in this case.
    If it does not exceed the maximum length limit then does nothing."""

    for i, row in df.iterrows():
        # If phone field exceed maximum character limit then note alert and remove value...
        if len(str(row[PHONE])) > LIMITS[PHONE]:
            df[ALERT].iloc[i] = str(df[ALERT].iloc[i]) + f"{row[PHONE]}" + ALERT_TYPE['phone_length']
            df[PHONE].iloc[i] = ""

    return df
