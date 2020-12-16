# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_payment_methods


def payment_methods_cleaner(data):
    """ Validates payment methods by checking that there are no duplicate names. If it does contain duplicates or if it the payment method does not exist
    it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function does not generate omits.
    """

    # Call payment method query function...
    duplicate_payment_dict, unique_payment_dict = query_payment_methods(designer_id)

    # Iterate over payment method and payment code columns and validate rows...
    for i in range(0, len(data['Payment Method'])):

        if data['Payment Method'].iloc[i] not in duplicate_payment_dict.keys() and data['Payment Code'].iloc[i] not in duplicate_payment_dict.values():
            if data['Payment Method'].iloc[i] in unique_payment_dict.keys() and data['Payment Code'].iloc[i] in unique_payment_dict.values():
                pass
            else:
                if data['Payment Method'].iloc[i] not in unique_payment_dict.keys():
                    data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["payment_method_setup"]
        else:
            data['Payment Method'].iloc[i] = ''
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["payment_method_duplicate"]

    return data
