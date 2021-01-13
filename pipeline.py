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

    # Generate dataframe...
    data = generate_dataframe()

    # Local validations...
    customer_code_cleaner(data)
    country_cleaner(data)
    state_cleaner(data)
    zipcode_cleaner(data)
    address_type_cleaner(data)
    address_cleaner(data)
    address_code_cleaner(data)
    city_cleaner(data)
    store_cleaner(data)
    phone_cleaner(data)
    email_cleaner(data)
    discount_cleaner(data)

    # Retrieve data from database...
    query_sales_reps(designer_id)
    query_payment_methods(designer_id)
    query_shipping_methods(designer_id)
    query_price_types(designer_id)
    query_customer_groups(designer_id)
    query_company_numbers(designer_id)

    # Validation with db data...
    sales_rep_cleaner(data, designer_id)
    payment_methods_cleaner(data, designer_id)
    shipping_methods_cleaner(data, designer_id)
    price_type_cleaner(data, designer_id)
    customer_group_cleaner(data, designer_id)
    company_number_cleaner(data, designer_id)

    # Generate results flags...
    generate_results(data)

    # Generate output files...
    generate_output(data)

    return None
