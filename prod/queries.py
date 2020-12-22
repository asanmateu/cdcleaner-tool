# Import prod connection modules
from connection import query_read_only_prod


def query_sales_reps(designer_id):
    """ Take designer id and call prod to make a query that retrieves account users
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.
    """
    # Query with f-string to insert designer id and close as string...
    query = f"select id, code, display_name from joor_web.accounts_users where account_id = {designer_id};"
    sales_reps = query_read_only_prod(query)

    # Extract unique values...
    unique_sales_reps = sales_reps.drop_duplicates(subset=['code', 'display_name'])
    sales_reps_dict = dict(zip(unique_sales_reps['display_name'], unique_sales_reps['code']))

    # Return dictionary of unique sales reps name code pairs...
    return sales_reps_dict


def query_price_types(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active price types
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.

    """
    query = f"select c.code, pt.name, cx.code, pt.created from joor_web.price_types pt join joor_web.currencies " \
            f"c on c.id = pt.currency_id join joor_web.currencies cx on cx.id = pt.retail_currency_id " \
            f"where pt.designer_id = {designer_id};"

    price_types = query_read_only_prod(query)

    return price_types


def query_payment_methods(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active payment methods
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.

   """
    query = f'select dpm.code, pm.payment_name from joor_web.designer_payment_methods dpm join' \
            f' joor_web.payment_methods pm on pm.id = dpm.payment_method_id where ' \
            f'dpm.designer_id = {designer_id} and dpm.deleted = 0;'

    # Extract DataFrame with designer's active payment methods...
    payment_methods = query_read_only_prod(query)

    # Divide duplicates and unique values into dictionaries to ease validation...
    duplicate_payment_methods = payment_methods[payment_methods.duplicated(subset=['code', 'payment_name'], keep=False)]
    duplicate_payment_dict = dict(zip(duplicate_payment_methods['payment_name'], duplicate_payment_methods['code']))

    unique_payment_methods = payment_methods.drop_duplicates(subset=['code', 'payment_name'])
    unique_payment_dict = dict(zip(unique_payment_methods['payment_name'], unique_payment_methods['code']))

    # Return dataframe with data from call to prod by running query...
    return duplicate_payment_dict, unique_payment_dict


def query_shipping_methods(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active shipping methods
    for the specific designer id.

   Returns:
       panda DataFrame with desired columns.

   """

    query = f"select dsm.code, sm.shipping_name from joor_web.designer_shipping_methods dsm " \
            f"join joor_web.shipping_methods sm on sm.id = dsm.shipping_method_id where " \
            f"dsm.designer_id = {designer_id} and dpm.deleted = 0;"

    # Extract DataFrame with designer's active payment methods...
    shipping_methods = query_read_only_prod(query)

    # Divide duplicates and unique values into dictionaries to ease validation...
    duplicate_shipping_methods = shipping_methods[shipping_methods.duplicated(subset=['code', 'shipping_name'], keep=False)]
    duplicate_shipping_dict = dict(zip(duplicate_shipping_methods['shipping_name'], duplicate_shipping_methods['code']))

    unique_shipping_methods = shipping_methods.drop_duplicates(subset=['code', 'shipping_name'])
    unique_shipping_dict = dict(zip(unique_shipping_methods['shipping_name'], unique_shipping_methods['code']))

    # Return dataframe with data from call to prod by running query...
    return duplicate_shipping_dict, unique_shipping_dict


def query_customer_info(designer_id: int):
    """Takes designer id and retrieves active customer group name and code details for the desired
    designer ready for validation. """

    query = f"select customer_group_name, customer_group_code from joor_web.customer_groups " \
            f"where account_id = {designer_id} and deleted = FALSE;"

    customer_groups = query_read_only_prod(query)
