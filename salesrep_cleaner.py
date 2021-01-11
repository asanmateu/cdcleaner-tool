# Import necessary modules...
from alerts import ALERT_TYPE
from designer_id import DESIGNER_ID
from queries import query_sales_reps
from columns import SALES_REP, ALERT


def sales_rep_cleaner(data, designer_id: int = DESIGNER_ID):
    """ Calls sales reps query function and validates sales reps for each row of the customer list. If the sales rep
    does not exist it leaves the cell empty and leaves an alert note for csm to set it up an request an update.

    Notes:
        This validation function does not generate omits.
    """

    # Call sales reps query function...
    sales_reps_dict = query_sales_reps(designer_id)

    # Iterate and clean sales reps while making alert note for those that don't exist...
    for i, row in data.iterrows():
        reference_sales_rep = row[SALES_REP]
        if reference_sales_rep != "":
            # If input code or name are not found on prod then note an alert and set no default...
            if (reference_sales_rep not in sales_reps_dict.keys()) and \
                    (reference_sales_rep not in sales_reps_dict.values()):
                data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_sales_rep}" + ALERT_TYPE["sales_rep"]
                data[SALES_REP].iloc[i] = ""

    return data
