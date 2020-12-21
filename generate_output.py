# Import necessary modules...
from library import pd
from paths import PATHS


# Generate the outputs into the output files directory
def generate_output(data):
    """ Extract clean and results file into output directory as csv files.

    Notes:
        Run as the final function.
    """

    clean_data = pd.DataFrame(columns=data.columns)

    # Rescue all clean rows without error flags and send them to clean DataFrame...
    for i in range(len(data['Country'])):
        if data['ERROR'].iloc[i] == "":
            clean_data.append(data.iloc[i])

    clean_data.drop(['ERROR'], axis=1)

    # Export files given output path and file name
    clean_file = clean_data.to_csv(PATHS['clean_output_path'])
    results_file = data.to_csv(PATHS['results_output_path'])

    return clean_file, results_file
