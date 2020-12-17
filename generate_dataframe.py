from library import np, pd, os
from paths import PATHS


def generate_dataframe():
    """ Take input file and generate a DataFrame to clean and another one to append errors to.

    Notes:
        First to execute.

    """
    # Change working directory to file inputs...
    files = os.listdir(PATHS['path_input'])

    # Load original excel sheet into a pandas DataFrame...
    data = pd.read_excel(files[1], na_values=['nan'])

    # Replace excel default null value...
    data.replace('nan', np.nan, inplace=True)
    data.fillna("", inplace=True)

    # Add an empty 'ERROR' column to original data DataFrame to report errors...
    data['RESULT'] = ""
    data['ALERT'] = ""
    data['ERROR'] = ""

    return data
