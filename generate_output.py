# Import necessary modules...


# Generate the outputs into the output files directory
def generate_output(data, omissions):
    """ Extract clean and omit file into output directory as csv files.

    Notes:
        Run last of all functions.
    """

    # Export files into a given path and file name
    clean_file = data.to_csv(
        r'/Users/antoniosanmateuserralta/PycharmProjects/JOOR/joor-cd-cleaner/files/output/clean_file.csv')
    omits_file = omissions.to_csv(
        r'/Users/antoniosanmateuserralta/PycharmProjects/JOOR/joor-cd-cleaner/files/output/omits_file.csv')

    return clean_file, omits_file