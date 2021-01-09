# Import necessary modules...
from alerts import ALERT_TYPE
from designer_id import DESIGNER_ID
from queries import query_payment_methods
from columns import PAYMENT_CODE, PAYMENT_NAME, ALERT


def payment_methods_cleaner(data, designer_id: int = DESIGNER_ID):
    """ Validates payment methods by checking that there are no duplicate names. If it does contain duplicates or
    if the payment method does not exist it will leave an alert note for csm to take the necessary action.

    Note:
        This validation function only sets alert flags.
    """

    # Call payment method query function...
    duplicate_payment_dict, unique_payment_dict = query_payment_methods(designer_id)

    # Iterate over payment method and payment code columns and validate rows over dictionaries retrieved from db...
    for i, row in data.iterrows():
        reference_payment_name = row[PAYMENT_NAME]
        reference_payment_code = row[PAYMENT_CODE]

        # if payment name is blank but there is a payment code
        if (reference_payment_name == "") and (reference_payment_code != ""):
            # Set alert: payment name required
            data[ALERT].iloc[i] = str(row[ALERT]) \
                                    + f"{reference_payment_code}" + ALERT_TYPE["payment_name_required"]
            # Reset values to no default...
            data[PAYMENT_CODE].iloc[i] = ""

        # if payment code is blank but there is a payment name
        elif (reference_payment_name != "") and (reference_payment_code == ""):
            # if neither are in duplicates
            if reference_payment_name not in duplicate_payment_dict.keys():
                # if payment method name is not on unique payment methods dictionary...
                if reference_payment_name in unique_payment_dict.keys():
                    data[PAYMENT_CODE] = unique_payment_dict.get(reference_payment_name)
                else:
                    data[ALERT].iloc[i] = str(row[ALERT]) \
                                            + f"{reference_payment_name}" + ALERT_TYPE["payment_name_setup"]
                    data[PAYMENT_NAME].iloc[i] = ""
            # payment name in duplicate
            else:
                data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_name}" \
                                        + ALERT_TYPE["payment_name_duplicate"]
                # Reset values to no default...
                data[PAYMENT_NAME].iloc[i] = ""
                data[PAYMENT_CODE].iloc[i] = ""

        # if both payment method and code exist
        elif (reference_payment_name != "") and (reference_payment_code != ""):
            # if neither are in duplicates
            if (reference_payment_name not in duplicate_payment_dict.keys()) and \
                    (reference_payment_code not in duplicate_payment_dict.values()):
                # if neither name nor code is in unique payment dict
                if (reference_payment_name not in unique_payment_dict.keys()) and \
                        (reference_payment_code not in unique_payment_dict.values()):
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_name}: {reference_payment_code}" \
                                            + ALERT_TYPE["payment_method_setup"]
                    data[PAYMENT_NAME].iloc[i] = ""
                    data[PAYMENT_CODE].iloc[i] = ""
                # if code is in unique payment dict but name is not
                elif (reference_payment_name not in unique_payment_dict.keys()) and \
                        (reference_payment_code in unique_payment_dict.values()):
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_name}: {reference_payment_code}" \
                                            + ALERT_TYPE["payment_method_setup"]
                    data[PAYMENT_NAME].iloc[i] = ""
                    data[PAYMENT_CODE].iloc[i] = ""
                # if name is found but code is not
                elif (reference_payment_name in unique_payment_dict.keys()) and \
                        (reference_payment_code not in unique_payment_dict.values()):
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_code}" \
                                            + ALERT_TYPE['payment_code_replaced']
                    data[PAYMENT_CODE].iloc[i] = unique_payment_dict.get(reference_payment_name)
                # if name and code don't match
                elif unique_payment_dict.get(reference_payment_name) != reference_payment_code:
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_name}: {reference_payment_code}" \
                                            + ALERT_TYPE['payment_method_match']
                    # Reset values to no default...
                    data[PAYMENT_NAME].iloc[i] = ""
                    data[PAYMENT_CODE].iloc[i] = ""
            # name or code in duplicate
            else:
                data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_payment_name}: {reference_payment_code}" \
                                        + ALERT_TYPE["payment_method_duplicate"]
                # Reset values to no default...
                data[PAYMENT_NAME].iloc[i] = ""
                data[PAYMENT_CODE].iloc[i] = ""

    return data
