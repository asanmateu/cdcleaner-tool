from errors import ERROR_TYPE
from lengths import LIMITS


def customer_code_cleaner(data):
    """Validate customer code filed mainly for any length constrains violation."""

    for i in range(len(data['Customer Code'])):
        # If input exceeds customer code character limit note an error...
        if len(str(data['Customer Code'])) > LIMITS['customer_code']:
            data['ERROR'].iloc[i] = str(data['ERROR'].iloc[i]) + ERROR_TYPE['customer_code_length']

    return data
