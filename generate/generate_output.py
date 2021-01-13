# Import necessary modules...
from paths import OUTPUT_RESULT_FILE_PATH


# Generate the outputs into the output files directory
def generate_output(df):
    """ Extract clean and results file into output directory as csv files.

    Notes:
        Run as the final function.
    """

    # Export files given output path and file name
    results_file = df.to_excel(OUTPUT_RESULT_FILE_PATH)

    return results_file
