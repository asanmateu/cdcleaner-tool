# Import necessary modules...
from constants import DESIGNER_ID
from generate import generate_dataframe, generate_output, generate_results
from services import country_cleaner, state_cleaner, zipcode_cleaner, city_cleaner, store_cleaner, \
    email_cleaner, address_code_cleaner, address_cleaner, address_type_cleaner, discount_cleaner, \
    customer_code_cleaner, phone_cleaner, sales_rep_cleaner, payment_methods_cleaner, \
    shipping_methods_cleaner, price_type_cleaner, company_number_cleaner, customer_group_cleaner
from prod import query_sales_reps, query_payment_methods, query_shipping_methods, query_price_types, \
    query_customer_groups, query_company_numbers


def pipeline_master(designer_id: int = DESIGNER_ID):
    """Call to each of the cleaning functions in the right order and return nothing"""

    # Generate DataFrame...
    data = generate_dataframe()

    # Local validations...
    print("Template successfully uploaded. Starting cleaning process: ")

    customer_code_cleaner(data)
    print("Validating customer code column...")
    country_cleaner(data)
    print("Validating country column...")
    state_cleaner(data)
    print("Validating state column...")
    zipcode_cleaner(data)
    print("Validating zip column...")
    address_type_cleaner(data)
    print("Validating address type column...")
    address_cleaner(data)
    print("Validating address 1 and address 2 columns...")
    address_code_cleaner(data)
    print("Validating address codes...")
    city_cleaner(data)
    print("Validating city column...")
    store_cleaner(data)
    print("Validating store name column...")
    phone_cleaner(data)
    print("Validating phone column...")
    email_cleaner(data)
    print("Validating email column...")
    discount_cleaner(data)
    print("Validating discounts column (beta)...\n")

    # Retrieve data from database...
    print("Retrieving necessary data from prod: ")

    query_sales_reps(designer_id)
    print("Retrieving sales reps...")
    query_payment_methods(designer_id)
    print("Retrieving payment methods...")
    query_shipping_methods(designer_id)
    print("Retrieving shipping methods...")
    query_price_types(designer_id)
    print("Retrieving price types...")
    query_customer_groups(designer_id)
    print("Retrieving customer groups...\n")
    query_company_numbers(designer_id)

    # Validation with db data...
    print("Cleaning prod columns: ")

    sales_rep_cleaner(data, designer_id)
    print("Validating sales reps...")
    payment_methods_cleaner(data, designer_id)
    print("Validating payment methods...")
    shipping_methods_cleaner(data, designer_id)
    print("Validating shipping methods...")
    price_type_cleaner(data, designer_id)
    print("Validating price types...")
    customer_group_cleaner(data, designer_id)
    print("Validating customer groups...")
    company_number_cleaner(data, designer_id)
    print("Validating company numbers...\n")

    # Generate results flags...
    generate_results(data)
    print("Generating result flags...\n")

    # Generate output files...
    print("Generating ready file...\n")
    generate_output(data)

    return None
