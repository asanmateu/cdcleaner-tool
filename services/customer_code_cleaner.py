from errors import ERROR_TYPE
from lengths import LIMITS


def customer_code_cleaner(data):
    """Validate customer code filed mainly for any length constrains violation."""

    for i, row in data.iterrows():
        # If input exceeds customer code character limit note an error...
        if len(str(row['Customer Code'])) > LIMITS['customer_code']:
            data['ERROR'].iloc[i] = str(row['ERROR']) + ERROR_TYPE['customer_code_length']

    return data
