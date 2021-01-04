# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {

    # Sales reps validation alerts...
    "sales_rep": f": sales rep does not exist: none was assigned. ",

    # Price type validation alerts...
    "price_type": f": price type does not exist; first one assigned. ",

    # Payment methods validation alerts...
    "payment_name_setup": f": payment method does not exist: none was assigned. ",
    "payment_name_notfound": f": payment name not found; use code. ",
    "payment_name_required": f" payment name required for code: ",
    "payment_code_replaced": ": payment code doesn't match name: replaced by correct match. ",
    "payment_name_duplicate": f": payment method containing duplicates; none was assigned. ",
    "payment_method_setup": f": payment method pair is not setup; none was assigned. ",
    "payment_method_match": f": payment method pair does not match; none was assigned. ",

    # Shipping methods validation alerts...
    "shipping_name_setup": f": shipping method does not exist: none was assigned. ",
    "shipping_name_notfound": f": shipping name not found; use code. ",
    "shipping_name_required": f" shipping name required for code: ",
    "shipping_code_replaced": ": shipping code doesn't match name: replaced by correct match. ",
    "shipping_name_duplicate": f": shipping method containing duplicates; none was assigned. ",
    "shipping_method_setup": f": shipping method pair is not setup; none was assigned. ",
    "shipping_method_match": f": shipping method pair does not match; none was assigned. ",

    # Email validation alerts...
    "email_missing": f"No email address provided, no user will be created; ",

}
