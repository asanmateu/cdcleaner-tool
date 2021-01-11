from environment_constants import DESIGNER
from pipeline import pipeline_master
from paths import OUTPUT_PATH
from library import os

"""
designer_id_value = input(DESIGNER + ": ")
os.environ[DESIGNER] = designer_id_value
"""
# Validate environment variables input to check if their type and if any is null...


print('\n Cleaning customer list...')


# Run pipeline master function...
pipeline_master()


print('The file has been successfully cleaned, check output directory: ')
print(OUTPUT_PATH)
