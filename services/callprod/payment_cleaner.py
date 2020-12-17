# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_payment_methods


def payment_methods_cleaner(data):
    """ Validates payment methods by checking that there are no duplicate names. If it does contain duplicates or
    if it the payment method does not exist it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function does not generate omits.
    """

    # Call payment method query function...
    duplicate_payment_dict, unique_payment_dict = query_payment_methods(designer_id)

    # Iterate over payment method and payment code columns and validate rows...
    for i in range(0, len(data['Payment Method'])):
        reference_payment_method = data['Payment Method'].iloc[i]

        # Validate reference shipping method note alerts if not setup or duplicate otherwise do nothing...
        if reference_payment_method not in duplicate_payment_dict.keys():
            if reference_payment_method not in unique_payment_dict.keys() or reference_payment_method \
                    not in unique_payment_dict.values():
                data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["payment_method_setup"]
                data['Payment Method'].iloc[i] = ""
                data['Payment Code'].iloc[i] = ""
        else:
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["payment_method_duplicate"]
            data['Payment Method'].iloc[i] = ""
            data['Payment Code'].iloc[i] = ""

    return data
