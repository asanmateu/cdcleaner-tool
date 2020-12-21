# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {
    "sales_rep": f"Sales rep {reference_sales_rep} does not exist: none was assigned; ",
    "price_type": f"Price type {reference_price_type} does not exist; first one assigned; ",
    "payment_method_setup": f"Payment method {reference_payment_method} does not exist: none was assigned;  ",
    "payment_method_duplicate": f"Payment method {reference_payment_method} is duplicated; ",
    "shipping_method_setup": f"Shipping method {reference_shipping_method} does not exist: none was assigned;  ",
    "shipping_method_duplicate": f"Shipping method {reference_shipping_method} is duplicated; ",
    "email_missing": f"No email address provided, no user will be created; ",

}


