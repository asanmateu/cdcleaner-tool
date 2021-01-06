# Import necessary modules...
from results import RESULT_TYPE


# Note final result per row
def generate_results(data):
    """ Populate results column in line with overall inputs in alert and error columns.

    Notes:
        Use this function after all validations have been done.
    """

    # Populate omissions with files containing errors...
    for i, row in data.iterrows():
        if row['ERROR'] != "":
            # Files containing at least one error are denied
            data['RESULT'].iloc[i] = RESULT_TYPE['denied']
        elif row['ALERT'] != "":
            # Files containing only alerts are defaulted but processed
            data['RESULT'].iloc[i] = RESULT_TYPE['defaulted']
        else:
            # Files with no errors are approved to be processed
            data['RESULT'].iloc[i] = RESULT_TYPE['approved']

    return data
