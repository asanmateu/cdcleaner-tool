# Import necessary modules...
from constants import DESIGNER_ID, OUTPUT_PATH
from generate import generate_dataframe, generate_output, generate_results
from services import country_cleaner, state_cleaner, zipcode_cleaner, city_cleaner, store_cleaner, \
    email_cleaner, address_code_cleaner, address_cleaner, address_type_cleaner, discount_cleaner, \
    customer_code_cleaner, phone_cleaner, sales_rep_cleaner, payment_methods_cleaner, \
    shipping_methods_cleaner, price_type_cleaner, company_number_cleaner, customer_group_cleaner
from prod import query_sales_reps, query_payment_methods, query_shipping_methods, query_price_types, \
    query_customer_groups, query_company_numbers, get_credentials, clear_credentials


def pipeline_master(designer_id: int = DESIGNER_ID):
    """Call to each of the cleaning functions in the right order and return nothing"""

    # Generate DataFrame...
    data = generate_dataframe()

    # Local validations...
    print("\nTemplate successfully uploaded. Starting cleaning process:\n")

    print("Validating customer code column...")
    customer_code_cleaner(data)
    print("Validating country column...")
    country_cleaner(data)
    print("Validating state column...")
    state_cleaner(data)
    print("Validating zip column...")
    zipcode_cleaner(data)
    print("Validating address type column...")
    address_type_cleaner(data)
    print("Validating address 1 and address 2 columns...")
    address_cleaner(data)
    print("Validating address codes...")
    address_code_cleaner(data)
    print("Validating city column...")
    city_cleaner(data)
    print("Validating store name column...")
    store_cleaner(data)
    print("Validating phone column...")
    phone_cleaner(data)
    print("Validating email column...")
    email_cleaner(data)
    print("Validating discounts column (beta)...")
    discount_cleaner(data)

    print("\nPlease enter prod credentials:\n")
    get_credentials()

    # Retrieve data from database...
    print("\nRetrieving necessary data from prod: ")

    print("\nRetrieving sales reps...")
    query_sales_reps(designer_id)

    print("Retrieving payment methods...")
    query_payment_methods(designer_id)
    print("Retrieving shipping methods...")
    query_shipping_methods(designer_id)
    print("Retrieving price types...")
    query_price_types(designer_id)
    print("Retrieving customer groups...")
    query_customer_groups(designer_id)
    print("Retrieving company numbers...")
    query_company_numbers(designer_id)

    # Validation with db data...
    print("\nCleaning prod columns: ")

    print("\nValidating sales reps...")
    sales_rep_cleaner(data, designer_id)
    print("Validating payment methods...")
    payment_methods_cleaner(data, designer_id)
    print("Validating shipping methods...")
    shipping_methods_cleaner(data, designer_id)
    print("Validating price types...")
    price_type_cleaner(data, designer_id)
    print("Validating customer groups...")
    customer_group_cleaner(data, designer_id)
    print("Validating company numbers...")
    company_number_cleaner(data, designer_id)

    # Generate results flags...
    print("\nGenerating result flags...")
    generate_results(data)

    # Generate output files...
    print("Generating ready file...")
    generate_output(data)

    print('\nThe file has been successfully cleaned, check output directory:\n' + OUTPUT_PATH + "\n")

    # Clear prod credentials
    clear_credentials()

    return None
