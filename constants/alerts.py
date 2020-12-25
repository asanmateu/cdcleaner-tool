# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {

    # Sales reps validation alerts...
    "sales_rep": f": sales rep does not exist: none was assigned. ",

    # Price type validation alerts...
    "price_type": f": price type does not exist; first one assigned. ",

    # Payment methods validation alerts...
    "payment_name_setup": f": payment method does not exist: none was assigned. ",
    "payment_name_notfound": f": payment name not found; use code. ",
    "payment_code_setup": f": payment method does not exist: none was assigned. ",
    "payment_code_notfound": f": payment code not found; use name. ",
    "payment_name_duplicate": f": payment name is duplicated; none was assigned. ",
    "payment_code_duplicate": f": payment code is duplicated; none was assigned. ",
    "payment_method_setup": f": payment method pair is not setup; none was assigned. ",
    "payment_method_match": f": payment method pair does not match; none was assigned. ",

    # Shipping methods validation alerts...
    "shipping_name_setup": f": shipping method does not exist: none was assigned. ",
    "shipping_name_notfound": f": shipping name not found; use code. ",
    "shipping_code_setup": f": shipping method does not exist: none was assigned. ",
    "shipping_code_notfound": f": shipping code not found; use name. ",
    "shipping_name_duplicate": f": shipping name is duplicated; none was assigned. ",
    "shipping_code_duplicate": f": shipping code is duplicated; none was assigned. ",
    "shipping_method_setup": f": shipping method pair is not setup; none was assigned. ",
    "shipping_method_match": f": shipping method pair does not match; none was assigned. ",

    # Email validation alerts...
    "email_missing": f"No email address provided, no user will be created; ",

}
