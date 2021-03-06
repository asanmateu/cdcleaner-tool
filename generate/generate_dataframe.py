from constants import np, pd, os, INPUT_PATH, RESULT, ALERT, ERROR
from utils import strip_df, df_to_object_type


def generate_dataframe():
    """ Take input file and generate a DataFrame to clean and another one to append errors to. """

    # Change working directory to file inputs...
    os.chdir(INPUT_PATH)

    # Load original excel sheet into a pandas DataFrame...
    data = pd.read_excel("customer_list_cleaner_template.xlsx", na_values=['nan'])

    # Replace excel default null value with ""...
    data.replace('nan', np.nan, inplace=True)
    data.fillna("", inplace=True)

    # Add an empty 'ERROR', 'ALERT' and 'RESULT' column to original data DataFrame note flags...
    data[RESULT] = ""
    data[ALERT] = ""
    data[ERROR] = ""

    # Convert data columns into object type...
    data = df_to_object_type(data)

    # Strip whitespaces from columns...
    data = strip_df(data)

    return data
