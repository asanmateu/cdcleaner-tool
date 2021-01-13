# Import necessary modules...
from constants import ALERT_TYPE, DESIGNER_ID, SALES_REP, ALERT
from prod import query_sales_reps


def sales_rep_cleaner(df, designer_id: int = DESIGNER_ID):
    """ Calls sales reps query function and validates sales reps for each row of the customer list. If the sales rep
    does not exist it leaves the cell empty and leaves an alert note for csm to set it up an request an update.

    Notes:
        This validation function does not generate omits.
    """

    # Call sales reps query function...
    sales_reps_dict = query_sales_reps(designer_id)

    # Iterate and clean sales reps while making alert note for those that don't exist...
    for i, row in df.iterrows():
        reference_sales_rep = row[SALES_REP]
        # If input value is not null:
        if reference_sales_rep != "":
            # If input code or name are not found on prod then note an alert and set no default...
            if (reference_sales_rep not in sales_reps_dict.keys()) and \
                    (reference_sales_rep not in sales_reps_dict.values()):
                df[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_sales_rep}" + ALERT_TYPE["sales_rep"]
                df[SALES_REP].iloc[i] = ""

    return df
