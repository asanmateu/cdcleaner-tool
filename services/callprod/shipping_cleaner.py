# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_shipping_methods


def shipping_methods_cleaner(data, designer_id: int):
    """ Validates shipping methods by checking that there are no duplicate names. If it does contain duplicates or
    if it the shipping method does not exist it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function does not generate omits.
    """

    # Call shipping method query function...
    duplicate_shipping_dict, unique_shipping_dict = query_shipping_methods(designer_id)

    # Iterate over shipping method and shipping code columns and validate rows...
    for i, row in data.iterrows():
        reference_shipping_method = row['Shipping Method']

        # Validate reference shipping method note alerts if not setup or duplicate otherwise do nothing...
        if reference_shipping_method not in duplicate_shipping_dict.keys():
            if reference_shipping_method not in unique_shipping_dict.keys() or reference_shipping_method not in \
                    unique_shipping_dict.values():
                row['ALERT'] = str(row['ALERT']) + ALERT_TYPE['shipping_method_setup']
                row['Shipping Method'] = ""
                row['Shipping Code'] = ""
        else:
            row['ALERT'] = str(row['ALERT']) + ALERT_TYPE['shipping_method_duplicate']
            row['Shipping Method'] = ""
            row['Shipping Code'] = ""

    return data
