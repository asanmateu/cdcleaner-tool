from pipeline import pipeline_master
from constants import OUTPUT_PATH


print('\n Cleaning customer list...')


# Run pipeline master function to clean file and output results file...
pipeline_master()


print('The file has been successfully cleaned, check output directory: ')
print(OUTPUT_PATH)
