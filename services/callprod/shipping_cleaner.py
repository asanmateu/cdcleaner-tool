# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_shipping_methods


def shipping_methods_cleaner(data, designer_id: int):
    """ Validates shipping methods by checking that there are no duplicate names. If it does contain duplicates or
    if it the shipping method does not exist it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function only sets alert flags.
    """

    # Call payment method query function...
    duplicate_shipping_dict, unique_shipping_dict = query_shipping_methods(designer_id)

    # Iterate over shipping method and payment code columns and validate rows over dictionaries retrieved from db...
    for i, row in data.iterrows():
        reference_shipping_name = row['Shipping Method']
        reference_shipping_code = row['Shipping Code']

        # if shipping name is blank but there is a payment code
        if reference_shipping_name == "" and reference_shipping_code != "":
            if reference_shipping_code not in duplicate_shipping_dict.values():
                if reference_shipping_code not in unique_shipping_dict.values():
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_code}" + ALERT_TYPE["shipping_code_setup"]
                    data['Shipping Code'].iloc[i] = ""
            else:
                # if given shipping code is duplicate value
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_code}" + ALERT_TYPE["shipping_code_duplicate"]
                # Reset values to no default...
                data['Shipping Method'].iloc[i] = ""
                data['Shipping Code'].iloc[i] = ""

        # if shipping code is blank but there is a payment name
        elif reference_shipping_name != "" and reference_shipping_code == "":
            if reference_shipping_name not in duplicate_shipping_dict.keys():
                if reference_shipping_name not in unique_shipping_dict.keys():
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}" + ALERT_TYPE["shipping_name_setup"]
                    data['Shipping Method'].iloc[i] = ""
            # shipping name in duplicate
            else:
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}" + ALERT_TYPE["shipping_name_duplicate"]
                # Reset values to no default...
                data['Shipping Method'].iloc[i] = ""
                data['Shipping Code'].iloc[i] = ""

        # if both shipping method and code exist
        elif reference_shipping_name != "" and reference_shipping_code != "":
            # if neither are in duplicates
            if (reference_shipping_name not in duplicate_shipping_dict.keys()) and (
                    reference_shipping_code not in duplicate_shipping_dict.values()):
                # if neither name nor code is in unique shipping dict
                if (reference_shipping_name not in unique_shipping_dict.keys()) and (
                        reference_shipping_code not in unique_shipping_dict.values()):
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}: {reference_shipping_code}" + ALERT_TYPE["shipping_method_setup"]
                    data['Shipping Method'].iloc[i] = ""
                    data['Shipping Code'].iloc[i] = ""
                # if code is in unique shipping dict but name is not
                elif (reference_shipping_name not in unique_shipping_dict.keys()) and (
                        reference_shipping_code in unique_shipping_dict.values()):
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}" + ALERT_TYPE["shipping_name_notfound"]
                    data['Shipping Method'].iloc[i] = ""
                # if name is found but code is not
                elif (reference_shipping_name in unique_shipping_dict.keys()) and (
                        reference_shipping_code not in unique_shipping_dict.values()):
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_code}" + ALERT_TYPE["shipping_code_notfound"]
                    data['Shipping Method'].iloc[i] = ""
                # if name and code don't match
                elif unique_shipping_dict.get(reference_shipping_name) != reference_shipping_code:
                    data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}: {reference_shipping_code}" + ALERT_TYPE['shipping_method_match']
                    # Reset values to no default...
                    data['Shipping Method'].iloc[i] = ""
                    data['Shipping Method'].iloc[i] = ""
            # name or code in duplicate
            else:
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_shipping_name}: {reference_shipping_code}" + ALERT_TYPE["shipping_method_duplicate"]
                # Reset values to no default...
                data['Shipping Method'].iloc[i] = ""
                data['Shipping Code'].iloc[i] = ""

    return data
