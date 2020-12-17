# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {
    "sales_rep": f"Sales rep {reference_sales_rep} does not exist: none was assigned, please submit an update request once setup; ",
    "price_type": f"Price type {reference_price_type} does not exist; first one assigned, please submit an update request once setup; ",
    "payment_method_setup": f"Payment method {reference_payment_method} not found, please set up and request update; ",
    "payment_method_duplicate": f"Payment method {reference_payment_method} has duplicates, none has been defaulted. Please fix settings; ",
    "shipping_method_setup": f"Shipping method {reference_shipping_method} not found, please set up and request update; ",
    "shipping_method_duplicate": f"Shipping method {reference_shipping_method} has duplicates, none has been defaulted. Please fix settings; ",
    "email_missing": f"No email address provided, no user will be created; ",

}


