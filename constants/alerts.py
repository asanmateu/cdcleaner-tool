# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {

    # Sales reps validation alerts
    "sales_rep": ": sales rep does not exist: none was assigned. ",

    # Price type validation alerts
    "price_label_notfound": ": price type does not exist; first label default assigned. ",
    "price_currency_match": ": Price currency didn't match label; replaced with label's match. ",
    "wholesale_currency_match": ": wholesale currency didn't match label; replaced with label's match. ",
    "retail_currency_match": ": retail currency didn't match label; replaced with label's match. ",

    # Payment methods validation alerts
    "payment_name_setup": ": payment method does not exist: none was assigned. ",
    "payment_name_notfound": ": payment name not found; use code. ",
    "payment_name_required": " payment name required for code: ",
    "payment_code_replaced": ": payment code doesn't match name: replaced by correct match. ",
    "payment_name_duplicate": ": payment method containing duplicates; none was assigned. ",
    "payment_method_setup": ": payment method pair is not setup; none was assigned. ",
    "payment_method_match": ": payment method pair does not match; none was assigned. ",

    # Shipping methods validation alerts
    "shipping_name_setup": ": shipping method does not exist: none was assigned. ",
    "shipping_name_notfound": ": shipping name not found; use code. ",
    "shipping_name_required": ": shipping name required for code: ",
    "shipping_code_replaced": ": shipping code doesn't match name: replaced by correct match. ",
    "shipping_name_duplicate": ": shipping method containing duplicates; none was assigned. ",
    "shipping_method_setup": ": shipping method pair is not setup; none was assigned. ",
    "shipping_method_match": ": shipping method pair does not match; none was assigned. ",

    # Email validation alerts
    "email_missing": "No email address provided, no user will be created; ",

}
