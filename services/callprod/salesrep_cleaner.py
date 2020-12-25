# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_sales_reps
from lengths import LIMITS
from errors import ERROR_TYPE


def sales_rep_cleaner(data, designer_id: int):
    """ Calls sales reps query function and validates sales reps for each row of the customer list. If the sales rep
    does not exist it leaves the cell empty and leaves an alert note for csm to set it up an request an update.

    Notes:
        This validation function does not generate omits.
    """

    # Call sales reps query function...
    sales_reps_dict = query_sales_reps(designer_id)

    # Iterate and clean sales reps while making alert note for those that don't exist...
    for i, row in data.iterrows():
        reference_sales_rep = row['Sales Rep']
        # If input code or name are not found on prod then note an alert and set no default...
        if (reference_sales_rep not in sales_reps_dict.keys()) and (reference_sales_rep not in sales_reps_dict.values()):
            row['ALERT'] = str(row['ALERT']) + ALERT_TYPE["sales_rep"]
            row['Sales Rep'] = ""

    return data
