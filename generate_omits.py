# Import necessary modules...
from library import pd, np, os


# Export ommit and clean files into output folders...
def generate_omits(data):
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
            omissions = omissions.append(data.iloc[i])
        else:
            pass

    # Delete rows with invalid errors from the clean data file
    for i in range(0, len(data['ERROR'])):
        if data['ERROR'].iloc[i] != "":
            data.drop(data.index[i], inplace=True)
        else:
            pass

    # Delete ERROR column from clean file
    data = data.drop(['ERROR'], axis=1)

    return data, omissions
