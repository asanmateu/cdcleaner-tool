from lengths import LIMITS


# Declaration of constant error variables...
ERROR_TYPE = {

    # General input errors
    "country_error": "Invalid country; /",
    "state_error": "Invalid state; /",
    "city_error": "Invalid city; /",
    "address_type error": "Invalid address type; /",
    "address_error": "Invalid address 1 input; /",
    "address_code_error": "Requires a unique address code; /",
    "store_error": "Invalid store name; /",
    "email_error": "Max 1 email per row; /",
    "price_label_error": "Invalid price label; /",
    "payment_method_error": "Invalid payment method; /",
    "shipping_method_error": "Invalid shipping method; /",
    "sales_rep_error": "Invalid sales rep; /",
    "zip_error": "United State addresses require zipcode input; /",

    # Length validation errors
    "customer_code_length": f"Customer code exceeds {LIMITS['customer_code']} characters. /",
    "alias_length": f"Customer alias exceeds {LIMITS['customer_name']} characters. /",
    "address_code_length": f"Address code exceeds {LIMITS['address_code']} characters. /",
    "store_name_length": f"Store name exceeds {LIMITS['store_name']} characters. /",
    "address1_length": f"Address 1 exceeds {LIMITS['address_1']} characters. /",
    "city_length": f"City exceeds {LIMITS['city']} characters. /",
    "state_length": f"State exceeds {LIMITS['state']} characters. /",
    "zip_length": f"Zipcode exceeds {LIMITS['zip']} characters. /",
    "phone_length": f"Phone exceeds {LIMITS['phone']} characters. /",
    "buyer_name_length": f"Buyer name exceeds {LIMITS['buyer_name']} characters. /",
    "email_length": f"Email exceeds {LIMITS['email']} characters. /",
    "price_currency_length": f"Price currency exceeds {LIMITS['price_currency']} characters. /",
    "discount_length": f"Discount exceeds {LIMITS['discount']} characters. /"

}
