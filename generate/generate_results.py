# Import necessary modules...
from results import RESULT_TYPE


# Note fin
def generate_results(data):
    """ Populate results column in line with overall inputs in alert and error columns.

    Notes:
        Use this function after all validations have been done.
    """

    # Populate omissions with files containing errors...
    for i, row in data.iterrows():
        if row['ERROR'] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['denied']
        elif row['ALERT'] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['defaulted']
        else:
            data['RESULT'].iloc[i] = RESULT_TYPE['approved']

    return data
