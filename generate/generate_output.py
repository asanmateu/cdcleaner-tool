# Import necessary modules...
from library import pd
from paths import OUTPUT_CLEAN_FILE_PATH, OUTPUT_RESULT_FILE_PATH
from columns import ERROR


# Generate the outputs into the output files directory
def generate_output(data):
    """ Extract clean and results file into output directory as csv files.

    Notes:
        Run as the final function.
    """

    clean_data = pd.DataFrame(columns=data.columns)

    # Rescue all clean rows without error flags and send them to clean DataFrame...
    for i, row in data.iterrows():
        if row[ERROR] == "":
            clean_data.append(row)

    clean_data.drop(ERROR, axis=1, inplace=True)

    # Export files given output path and file name
    clean_file = clean_data.to_csv(OUTPUT_CLEAN_FILE_PATH)
    results_file = data.to_csv(OUTPUT_RESULT_FILE_PATH)

    return clean_file, results_file
