from pipeline import pipeline_master
from paths import OUTPUT_PATH
from library import os


# Validate environment variables input to check if their type and if any is null...


print('\n Cleaning customer list...')


# Run pipeline master function...
pipeline_master()


print('The file has been successfully cleaned, check output directory: ')
print(OUTPUT_PATH)
