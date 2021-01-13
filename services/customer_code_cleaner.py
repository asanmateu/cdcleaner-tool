from columns import ERROR, CUSTOMER_CODE
from errors import ERROR_TYPE
from lengths import LIMITS


def customer_code_cleaner(df):
    """Validate customer code filed mainly for any length constrains violation."""

    for i, row in df.iterrows():
        # If input exceeds customer code character limit note an error...
        if len(str(row[CUSTOMER_CODE])) > LIMITS['customer_code']:
            df[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['customer_code_length']

    return df
