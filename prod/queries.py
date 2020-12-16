# Import prod connection modules
from connection import query_read_only_prod


def query_sales_reps(designer_id):
    """ Take designer id and call prod to make a query that retrieves account users
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.
    """
    # Prepare query with f-string to insert designer id and close as string...
    query = f"select id, code, display_name from joor_web.accounts_users where account_id = {designer_id};"

    # Call prod and run query saving it as a pandas DataFrame called sales_reps...
    sales_reps = query_read_only_prod(query)

    return sales_reps


def query_price_types(designer_id):
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


def query_payment_methods(designer_id):
    """ Take designer id and call prod to make a query that retrieves active payment methods
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.

   """
    query = f"select dpm.code, pm.payment_name, pm.code from joor_web.designer_payment_methods dpm " \
            f"join joor_web.payment_methods pm on pm.id = dpm.payment_method_id" \
            f"where dpm.designer_id = {designer_id} and dpm.deleted = 0;"

    payment_methods = query_read_only_prod(query)

    return payment_methods


def query_shipping_methods(designer_id):
    """ Take designer id and call prod to make a query that retrieves active shipping methods
    for the specific designer id.

   Returns:
       panda DataFrame with desired columns.

   """
    query = f"select dsm.code, sm.shipping_name, sm.code from joor_web.designer_shipping_methods dsm " \
            f"join joor_web.shipping_methods sm on sm.id = dsm.shipping_method_id where " \
            f"dsm.designer_id = {designer_id} and dpm.deleted = 0;"

    shipping_methods = query_read_only_prod(query)

    return shipping_methods
