# Import necessary modules...
from alerts import ALERT_TYPE
from queries import query_sales_reps


def sales_rep_cleaner(data):
    """ Calls sales reps query function and validates sales reps for each row of the customer list. If the sales rep does not exist it leaves the cell empty
    and leaves an alert note for csm to set it up an request an update.

    Notes:
        This validation function does not generate omits.
    """

    # Call sales reps query function...
    sales_rep_names, sales_rep_codes = query_sales_reps(designer_id)

    # Iterate and clean sales reps while making alert note for those that don't exist...
    for i in range(0, len(data['Sales Rep'])):
        if data['Sales Rep'].iloc[i] in sales_rep_names or data['Sales Rep'].iloc[i] in sales_rep_codes or \
                data['Sales Rep'].iloc[i] == '':
            pass
        else:
            data['Sales Rep'].iloc[i] = ''
            data['ALERT'].iloc[i] = str(data['ALERT'].iloc[i]) + ALERT_TYPE["sales_rep"]

    return data
