# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_sales_reps


def sales_rep_cleaner(data):
    """ Calls sales reps query function and validates sales reps for each row of the customer list. If the sales rep
    does not exist it leaves the cell empty and leaves an alert note for csm to set it up an request an update.

    Notes:
        This validation function does not generate omits.
    """

    # Call sales reps query function...
    sales_reps_dict = query_sales_reps(designer_id)

    # Iterate and clean sales reps while making alert note for those that don't exist...
    for i in range(len(data['Sales Rep'])):
        reference_sales_rep = data['Sales Rep'].iloc[i]
        if reference_sales_rep not in sales_reps_dict.keys() or reference_sales_rep not in sales_reps_dict.values():
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["sales_rep"]
            data['Sales Rep'].iloc[i] = ""

    return data
