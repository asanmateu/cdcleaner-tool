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
    "customer_code_length": f"Customer code exceeds {LIMITS['customer_code']} characters. Please fix. /",
    "alias_length": f"Customer alias exceeds {LIMITS['customer_name']} characters. Please fix. /",
    "address_code_length": f"Address code exceeds {LIMITS['address_code']} characters. /",
    "address_1_length": f": Address 1 exceeds {LIMITS['address_1']} characters. Please fix. /",
    "address_2_length": f": Address 2 exceeds {LIMITS['address_2']} characters. Please fix. /",
    "store_name_length": f"Store name exceeds {LIMITS['store_name']} characters. Please fix. /",
    "address1_length": f"Address 1 exceeds {LIMITS['address_1']} characters. Please fix. /",
    "city_length": f"City exceeds {LIMITS['city']} characters. Please fix. /",
    "state_length": f"State exceeds {LIMITS['state']} characters. Please fix. /",
    "zip_length": f"Zipcode exceeds {LIMITS['zip']} characters. Please fix. /",
    "phone_length": f"Phone exceeds {LIMITS['phone']} characters. Please fix. /",
    "buyer_name_length": f"Buyer name exceeds {LIMITS['buyer_name']} characters. Please fix. /",
    "email_length": f"Email exceeds {LIMITS['email']} characters. Please fix. /",
    "price_currency_length": f"Price currency exceeds {LIMITS['price_currency']} characters. Please fix. /",
    "discount_length": f"Discount exceeds {LIMITS['discount']} characters. Please fix. /"

}
