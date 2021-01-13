from constants import DISCOUNT, ALERT, ALERT_TYPE, LIMITS


def discount_cleaner(df):
    """Validates discount's field format removing any percentage symbols and checks its length. """

    for i, row in df.iterrows():
        # If there is any % symbol strip it...
        if row[DISCOUNT].count('%') > 1:
            df[DISCOUNT].iloc[i] = df[DISCOUNT].iloc[i].strip('%')

        # If length exceeds limit note an alert and remove the value...
        if len(str(row[DISCOUNT])) > LIMITS[DISCOUNT]:
            df[ALERT].iloc[i] = str(row[ALERT]) + f"{row[DISCOUNT]}" + ALERT_TYPE['discount_length']
            df[DISCOUNT].iloc[i] = ""

    return df
