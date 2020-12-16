# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_shipping_methods


def shipping_methods_cleaner(data):
    """ Validates shipping methods by checking that there are no duplicate names. If it does contain duplicates or
    if it the shipping method does not exist it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function does not generate omits.
    """

    # Call shipping method query function...
    duplicate_shipping_dict, unique_shipping_dict = query_shipping_methods(designer_id)

    # Iterate over shipping method and shipping code columns and validate rows...
    for i in range(0, len(data['Shipping Method'])):

        if data['Shipping Method'].iloc[i] not in duplicate_shipping_dict.keys() and data['Shipping Code'].iloc[i] \
                not in duplicate_shipping_dict.values():
            if data['Shipping Method'].iloc[i] in unique_shipping_dict.keys() and data['Shipping Code'].iloc[i] in \
                    unique_shipping_dict.values():
                pass
            else:
                if data['Shipping Method'].iloc[i] not in unique_shipping_dict.keys():
                    data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE['shipping_method_setup']
        else:
            data['Shipping Method'].iloc[i] = ''
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE['shipping_method_duplicate']

    return data
