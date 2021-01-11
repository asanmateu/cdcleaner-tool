from environment_constants import SSH_USERNAME, SSH_PASSWORD, PROD_USERNAME, PROD_PASSWORD, DESIGNER
from pipeline import pipeline_master
from paths import OUTPUT_PATH
from library import os

"""
# Get environment variables and then run the script...
ssh_username_value = input(SSH_USERNAME + ": ")
os.environ[SSH_USERNAME] = ssh_username_value

ssh_password_value = input(SSH_PASSWORD + ": ")
os.environ[SSH_PASSWORD] = ssh_password_value

prod_username_value = input(PROD_USERNAME + ": ")
os.environ[PROD_USERNAME] = prod_username_value

prod_password_value = input(PROD_PASSWORD + ": ")
os.environ[PROD_PASSWORD] = prod_password_value
"""

designer_id_value = input(DESIGNER + ": ")
os.environ[DESIGNER] = designer_id_value

# Validate environment variables input to check if their type and if any is null...


print('\n Cleaning customer list...')


# Run pipeline master function...
pipeline_master()


print('The file has been successfully cleaned, check output directory: ')
print(OUTPUT_PATH)
