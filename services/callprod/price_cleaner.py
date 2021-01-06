# Import necessary modules...
from queries import query_price_types
from alerts import ALERT_TYPE


def price_type_cleaner(data, designer_id: int):
    """ Cleans price label and currencies depending on the template provided and returns either
    alerts and fixes the discrepancy or defaults the first price type and throws an error. """

    # Unpack necessary data from query_price_types function...
    default_price_tuple, wholesale_prices_dict, retail_prices_dict = query_price_types(designer_id)

    for i, row in data.iterrows():

        # Reference price label for the row...
        reference_label = row['Price Label']

        # If old template is being processed...
        if ("Price Label" in data.columns) and ("Price Currency" in data.columns):

            # Use price 'retail' currency as currency reference...
            reference_currency = row['Price Currency']

            # If price label provided is not in order settings set default and throw error...
            if reference_label not in wholesale_prices_dict.keys():
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_label}" + ALERT_TYPE['price_label_notfound']
                data['Price Label'].iloc[i] = default_price_tuple[1]
                data['Price Currency'].iloc[i] = default_price_tuple[0]
            # If price label is in setting but currency does not match then fix it...
            elif wholesale_prices_dict.get(reference_label) != reference_currency:
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_currency}" + ALERT_TYPE['price_currency_match']
                data['Price Currency'].iloc[i] = wholesale_prices_dict.get(reference_label)

        # If new template is being processed...
        elif ("Price Label" in data.columns) and ("Wholesale Currency" in data.columns) and (
                "Retail Currency" in data.columns):

            # Use wholesale currency, price label, retail currency as reference...
            reference_wholesale_currency = row['Wholesale Currency']
            reference_retail_currency = row['Retail Currency']

            # If price label provided is not in order settings set default and throw error...
            if reference_label not in wholesale_prices_dict.keys():
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_label}" + ALERT_TYPE['price_label_notfound']
                data['Price Label'].iloc[i] = default_price_tuple[1]
                data['Wholesale Currency'].iloc[i] = default_price_tuple[0]
                data['Retail Currency'].iloc[i] = default_price_tuple[2]

            # If retail currency does not match label then correct it...
            elif (wholesale_prices_dict.get(reference_label) == reference_wholesale_currency) and (
                    retail_prices_dict.get(reference_label) != reference_retail_currency):
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_retail_currency}" + ALERT_TYPE[
                    'retail_currency_match']
                data['Retail Currency'].iloc[i] = retail_prices_dict.get(reference_label)

            # If wholesale currency does not match label then correct it...
            elif (wholesale_prices_dict.get(reference_label) != reference_wholesale_currency) and (
                    retail_prices_dict.get(reference_label) == reference_retail_currency):
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_wholesale_currency}" + ALERT_TYPE[
                    'wholesale_currency_match']
                data['Wholesale Currency'].iloc[i] = wholesale_prices_dict.get(reference_label)

            # If both currencies do not match the label then correct both...
            elif (wholesale_prices_dict.get(reference_label) != reference_wholesale_currency) and (
                    retail_prices_dict.get(reference_label) != reference_retail_currency):
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_retail_currency}" + ALERT_TYPE[
                    'retail_currency_match']
                data['ALERT'].iloc[i] = str(row['ALERT']) + f"{reference_wholesale_currency}" + ALERT_TYPE[
                    'wholesale_currency_match']
                data['Retail Currency'].iloc[i] = retail_prices_dict.get(reference_label)
                data['Wholesale Currency'].iloc[i] = wholesale_prices_dict.get(reference_label)

    return data
