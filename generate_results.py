# Import necessary modules...
from library import pd, np, os
from results import RESULT_TYPE


# Export ommit and clean files into output folders...
def generate_results(data):
    """ Populates omissions and export both clean and omits file based on rows with errors.

    Args:
        data (pandas DataFrame):

    Returns:
        clean_file (csv): Clean data file export.
        omits_file(csv): Omit data file (containing rows with errors).

    Notes:
        Use this function last.
    """

    # Populate omissions with files containing errors...
    for i in range(0, len(data['ERROR'])):
        if data['ERROR'].iloc[i] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['denied']
        elif data['ALERT'].iloc[i] != "":
            data['RESULT'].iloc[i] = RESULT_TYPE['defaulted']

    return data
