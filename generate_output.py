# Import necessary modules...
from library import pd


# Generate the outputs into the output files directory
def generate_output(data):
    """ Extract clean and omit file into output directory as csv files.

    Notes:
        Run last of all functions.
    """

    clean_data = pd.DataFrame(columns=data.columns)

    for i in range(0, len(data['Country'])):
        if data['ERROR'].iloc[i] == "":
            clean_data.append(data.iloc[i])

    clean_data.drop(['ERROR'], axis=1)

    # Export files into a given path and file name
    clean_file = clean_data.to_csv(
        r'/Users/antoniosanmateuserralta/PycharmProjects/JOOR/joor-cd-cleaner/files/output/clean_file.csv')
    results_file = data.to_csv(
        r'/Users/antoniosanmateuserralta/PycharmProjects/JOOR/joor-cd-cleaner/files/output/omits_file.csv')

    return clean_file, results_file
