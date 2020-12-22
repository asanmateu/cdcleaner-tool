# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {

    # Sales reps validation alerts...
    "sales_rep": f"Sales rep {reference_sales_rep} does not exist: none was assigned. ",

    # Price type validation alerts...
    "price_type": f"Price type {reference_price_type} does not exist; first one assigned. ",

    # Payment methods validation alerts...
    "payment_name_setup": f"Payment method {reference_payment_name} does not exist: none was assigned. ",
    "payment_name_notfound": f"Payment name {reference_payment_name} not found; use code. ",
    "payment_code_setup": f"Payment method {reference_payment_code} does not exist: none was assigned. ",
    "payment_code_notfound": f"Payment code {reference_payment_code} not found; use name. ",
    "payment_name_duplicate": f"Payment name {reference_payment_name} is duplicated; none was assigned. ",
    "payment_code_duplicate": f"Payment code {reference_payment_code} is duplicated; none was assigned. ",
    "payment_method_setup": f"Payment method pair {reference_payment_name}: {reference_payment_code} "
                            f"is not setup; none was assigned. ",

    # Shipping methods validation alerts...
    "shipping_method_setup": f"Shipping method {reference_shipping_method} does not exist: none was assigned;  ",
    "shipping_method_duplicate": f"Shipping method {reference_shipping_method} is duplicated; ",

    # Email validation alerts...
    "email_missing": f"No email address provided, no user will be created; ",

}
