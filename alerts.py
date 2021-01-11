from lengths import LIMITS

# Alerts do not generate an omit but point out a possible error //////
ALERT_TYPE = {

    # VALUE ALERTS ////

    # Sales reps validation alerts
    "sales_rep": ": sales rep does not exist: none was assigned. /",

    # Company number alert
    "company_number_setup": ": company number provided not setup; none was assigned. /",

    # Customer group validation alerts
    "customer_group_name_required": ": group name required to use code; none was assigned. /",
    "customer_group_setup": ": customer group provided not setup; none was assigned. /",
    "customer_group_match": ": customer group pair does not match settings; none was assigned. /",
    
    # Price type validation alerts
    "price_label_notfound": ": price type does not exist; first label default assigned. /",
    "price_currency_match": ": price currency didn't match label; replaced with label's match. /",
    "wholesale_currency_match": ": wholesale currency didn't match label; replaced with label's match. /",
    "retail_currency_match": ": retail currency didn't match label; replaced with label's match. /",

    # Payment methods validation alerts
    "payment_name_setup": ": payment method does not exist: none was assigned. /",
    "payment_name_notfound": ": payment name not found; use code. /",
    "payment_name_required": " payment name required to use code: none was assigned. /",
    "payment_code_replaced": ": payment code doesn't match name: replaced by correct match. /",
    "payment_name_duplicate": ": payment method containing duplicates; none was assigned. /",
    "payment_method_setup": ": payment method pair is not setup; none was assigned. /",
    "payment_method_match": ": payment method pair does not match settings; none was assigned. /",

    # Shipping methods validation alerts
    "shipping_name_setup": ": shipping method does not exist: none was assigned. /",
    "shipping_name_notfound": ": shipping name not found; use code. /",
    "shipping_name_required": ": shipping name required to use code; none was assigned. /",
    "shipping_code_replaced": ": shipping code doesn't match name: replaced by correct match. /",
    "shipping_name_duplicate": ": shipping method containing duplicates; none was assigned. /",
    "shipping_method_setup": ": shipping method pair is not setup; none was assigned. /",
    "shipping_method_match": ": shipping method pair does not match settings; none was assigned. /",

    # Email validation alerts
    "email_missing": "No email address provided; no user will be created. /",


    # LENGTH ALERTS ////

    "customer_code_length": f": Customer code exceeds {LIMITS['customer_code']} characters. /",
    "alias_length": f": Customer alias exceeds {LIMITS['customer_name']} characters. Value removed. /",
    "address_code_length": f": Address code exceeds {LIMITS['address_code']} characters. Value removed. /",
    "store_name_length": f": Store name exceeds {LIMITS['store_name']} characters. Value removed. /",
    "address1_length": f": Address 1 exceeds {LIMITS['address_1']} characters. Value removed. /",
    "city_length": f": City exceeds {LIMITS['city']} characters. Value removed. /",
    "state_length": f": State exceeds {LIMITS['state']} characters. Value removed. /",
    "zip_length": f": Zipcode exceeds {LIMITS['zip']} characters. Value removed. Value removed. /",
    "phone_length": f":Phone exceeds {LIMITS['phone']} characters. Value removed. /",
    "buyer_name_length": f": Buyer name exceeds {LIMITS['buyer_name']} characters. Value removed. /",
    "email_length": f": Email exceeds {LIMITS['email']} characters. Value removed. /",
    "discount_length": f": Discount exceeds {LIMITS['discount']} characters. Value removed. /"

}
