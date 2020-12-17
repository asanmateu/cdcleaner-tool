from library import np, pd, os


def generate_dataframe():
    """ Take input file and generate a DataFrame to clean and another one to append errors to.

    Notes:
        First to execute.

    """
    # Change working directory to file inputs...
    os.chdir(r'/Users/antoniosanmateuserralta/PycharmProjects/JOOR/joor-cd-cleaner/files/input')

    # Load original excel sheet into a pandas DataFrame...
    data = pd.read_excel('customer_data_example.xlsx', na_values=['nan'])

    # Replace excel default null value...
    data.replace('nan', np.nan, inplace=True)
    data.fillna("", inplace=True)

    # Add an empty 'ERROR' column to original data DataFrame to report errors...
    data['ALERT'] = ""
    data['ERROR'] = ""
    data['RESULT'] = ""

    return data
