# Import necessary modules...
from generate_dataframe import generate_dataframe
from country_cleaner import country_cleaner
from state_cleaner import state_cleaner
from zipcode_cleaner import zipcode_cleaner
from address_cleaner import address_code_cleaner, address_cleaner, address_type_cleaner
from city_cleaner import city_cleaner
from store_cleaner import store_cleaner
from email_cleaner import email_cleaner
from queries import query_sales_reps, query_payment_methods, query_shipping_methods, query_price_types
from salesrep_cleaner import sales_rep_cleaner
from payment_cleaner import payment_methods_cleaner
from shipping_cleaner import shipping_methods_cleaner
from price_cleaner import price_type_cleaner
from generate_results import generate_results
from generate_output import generate_output


def pipeline_master(designer_id: int):
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

    # Validation with db data...
    sales_rep_cleaner(data)
    payment_methods_cleaner(data)
    shipping_methods_cleaner(data)
    price_type_cleaner(data)

    # Generate results flags...
    generate_results(data)

    # Generate output files...
    generate_output(data)

    # Send reports to google sheets API...

    return None
