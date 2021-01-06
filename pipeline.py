# Import necessary modules...
from generate.generate_dataframe import generate_dataframe
from country_cleaner import country_cleaner
from state_cleaner import state_cleaner
from zipcode_cleaner import zipcode_cleaner
from address_cleaner import address_code_cleaner, address_cleaner, address_type_cleaner
from city_cleaner import city_cleaner
from store_cleaner import store_cleaner
from email_cleaner import email_cleaner
from queries import query_sales_reps, query_payment_methods, query_shipping_methods, query_price_types, \
    query_customer_groups, query_company_number
from company_number_cleaner import company_number_cleaner
from customer_group_cleaner import customer_group_cleaner
from salesrep_cleaner import sales_rep_cleaner
from payment_cleaner import payment_methods_cleaner
from shipping_cleaner import shipping_methods_cleaner
from price_cleaner import price_type_cleaner
from generate.generate_results import generate_results
from generate.generate_output import generate_output
from designer_id import DESIGNER_ID


def pipeline_master(designer_id: int = DESIGNER_ID):
    """Call to each of the cleaning functions in the right order and return nothing"""

    # Generate dataframe...
    data = generate_dataframe()

    # Local validations...
    country_cleaner(data)
    state_cleaner(data)
    zipcode_cleaner(data)
    address_type_cleaner(data)
    address_cleaner(data)
    address_code_cleaner(data)
    city_cleaner(data)
    store_cleaner(data)
    email_cleaner(data)

    # Retrieve data from database...
    query_sales_reps(designer_id)
    query_payment_methods(designer_id)
    query_shipping_methods(designer_id)
    query_price_types(designer_id)
    query_customer_groups(designer_id)
    query_company_number(designer_id)

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

    # Send reports to google sheets API...

    return None
