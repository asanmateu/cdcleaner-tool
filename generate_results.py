# Import necessary modules...
from results import RESULT_TYPE


# Note fin
def generate_results(data):
    """ Populate results column in line with overall inputs in alert and error columns.

    Notes:
        Use this function after all validations have been done.
    """

    # Populate omissions with files containing errors...
    for i in range(0, len(data['ERROR'])):
        if data['ERROR'].iloc[i] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['denied']
        elif data['ALERT'].iloc[i] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['defaulted']
        else:
            data['RESULT'].iloc[i] = RESULT_TYPE['approved']

    return data
