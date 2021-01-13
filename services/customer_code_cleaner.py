from constants import ERROR, CUSTOMER_CODE, ERROR_TYPE, LIMITS


def customer_code_cleaner(df):
    """Validate customer code filed mainly for any length constrains violation."""

    for i, row in df.iterrows():
        # If input exceeds customer code character limit note an error...
        if len(str(row[CUSTOMER_CODE])) > LIMITS[CUSTOMER_CODE]:
            df[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['customer_code_length']

    return df
