from constants import np, pd, os, sys, INPUT_PATH, RESULT, ALERT, ERROR
from utils import strip_df, df_to_object_type


def generate_dataframe():
    """ Take input file and generate a DataFrame to clean and another one to append errors to. """

    # Change working directory to file inputs...
    os.chdir(INPUT_PATH)

    try:
        print("\nReading and parsing template...")

        # Load original excel sheet into a pandas DataFrame...
        data = pd.read_excel("customer_list_cleaner_template.xlsx", na_values=['nan'])

    except IndexError:
        print("ERROR: make sure you use and .xlsx file that it is saved as Excel Workbook and NOT as "
              "Strict Open XML Spreadsheet and try again.")

        sys.exit()

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
