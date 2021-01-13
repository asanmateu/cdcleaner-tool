# Import necessary modules...
from queries import query_price_types
from designer_id import DESIGNER_ID
from alerts import ALERT_TYPE
from columns import PRICE_CURRENCY, PRICE_LABEL, WHOLESALE_CURRENCY, RETAIL_CURRENCY, ALERT


def price_type_cleaner(df, designer_id: int = DESIGNER_ID):
    """ Cleans price label and currencies depending on the template provided and returns either
    alerts and fixes the discrepancy or defaults the first price type and throws an error. """

    # Unpack necessary data from query_price_types function...
    default_price_tuple, wholesale_prices_dict, retail_prices_dict = query_price_types(designer_id)

    for i, row in df.iterrows():

        # Reference price label for the row...
        reference_label = row[PRICE_LABEL]

        # If old template is being processed...
        if (PRICE_LABEL in df.columns) and (PRICE_CURRENCY in df.columns):

            # Use price 'wholesale' currency as currency reference...
            reference_currency = row[PRICE_CURRENCY]

            # If price label provided is not in order settings set default and throw error...
            if reference_label not in wholesale_prices_dict.keys():
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_label}" + ALERT_TYPE['price_label_notfound']
                df[PRICE_LABEL].iloc[i] = default_price_tuple[1]
                df[PRICE_CURRENCY].iloc[i] = default_price_tuple[0]
            # If price label is in setting but currency does not match then fix it...
            elif wholesale_prices_dict.get(reference_label) != reference_currency:
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_currency}" + ALERT_TYPE['price_currency_match']
                df[PRICE_CURRENCY].iloc[i] = wholesale_prices_dict.get(reference_label)

        # If new template is being processed...
        elif (PRICE_LABEL in df.columns) and (WHOLESALE_CURRENCY in df.columns) \
                and (RETAIL_CURRENCY in df.columns):

            # Use wholesale currency, price label, retail currency as reference...
            reference_wholesale_currency = row[WHOLESALE_CURRENCY]
            reference_retail_currency = row[RETAIL_CURRENCY]

            # If price label provided is not in order settings set default and throw error...
            if reference_label not in wholesale_prices_dict.keys():
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_label}" + ALERT_TYPE['price_label_notfound']
                df[PRICE_LABEL].iloc[i] = default_price_tuple[1]
                df[WHOLESALE_CURRENCY].iloc[i] = default_price_tuple[0]
                df[RETAIL_CURRENCY].iloc[i] = default_price_tuple[2]

            # If retail currency does not match label then correct it...
            elif (wholesale_prices_dict.get(reference_label) == reference_wholesale_currency) and \
                    (retail_prices_dict.get(reference_label) != reference_retail_currency):
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_retail_currency}" + \
                                    ALERT_TYPE['retail_currency_match']
                df[RETAIL_CURRENCY].iloc[i] = retail_prices_dict.get(reference_label)

            # If wholesale currency does not match label then correct it...
            elif (wholesale_prices_dict.get(reference_label) != reference_wholesale_currency) and \
                    (retail_prices_dict.get(reference_label) == reference_retail_currency):
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_wholesale_currency}" + \
                                    ALERT_TYPE['wholesale_currency_match']
                df[WHOLESALE_CURRENCY].iloc[i] = wholesale_prices_dict.get(reference_label)

            # If both currencies do not match the label then correct both...
            elif (wholesale_prices_dict.get(reference_label) != reference_wholesale_currency) and \
                    (retail_prices_dict.get(reference_label) != reference_retail_currency):
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_retail_currency}" + \
                                    ALERT_TYPE['retail_currency_match']
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_wholesale_currency}" + \
                                    ALERT_TYPE['wholesale_currency_match']
                df[RETAIL_CURRENCY].iloc[i] = retail_prices_dict.get(reference_label)
                df[WHOLESALE_CURRENCY].iloc[i] = wholesale_prices_dict.get(reference_label)

    return df
