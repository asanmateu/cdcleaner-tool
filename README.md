# ⚡️  CD Customer List Cleaner (version: 1.0.0)  ⚡️

The purpose of this script is to speed up the process of cleaning manual customer data templates.

The script features a range of functions with different functionality that clean each of the template columns.


## Version 1.0.0

This version does:

1. Cleans every filed of the customer list data except the Discount related fields. Please review this beforehand.

2. Includes address codes validation process, however, for it to work data needs to be in a decent status, including address types, and either customer codes or customer names that are unique for the connection.

2. Returns a results.xlsx file with 3 new columns RESULT, ALERT, ERROR.

- RESULT: Indicates whether the row is clean, values have been set to default, or denied.
- ALERT: Alerts contain recommendations and require taking note as this may include payment methods defaulted to none since these were not setup or price type defaulted to the first in the designer's order settings.
- ERROR: Fields that need to be fixed compulsory for analysts to process them.

3. These flags will make obvious if values have been removed to default or where the key errors are.


## What this version does NOT do

- Clean discount fields
- Check intention of bad data (i.e. multiple rows for a same retailer without customer code that try to add only different buyers...)
- Bad data must be spot intuitively and unfortunately


## 🛠  Installation    

1. Request your credential to access **prod_ro** to management.


2. Make sure you have installed conda: https://docs.anaconda.com/anaconda/install/mac-os/.


3. Open Anaconda Navigator and open **jupyter-lab > terminal** window. Then, run this command on the command line:
```
# This is to make conda environments work on 'zsh' -> MAC OSX's terminal system.

$ conda init zsh
```

4. Create a new conda environment using environment export found in the tool's conda directory:
```
# If this doesn't work try -f path/to/cdcleaner-conda-env.yml

$ conda env create -f cdcleaner-conda-env.yml
```

5. Activate conda environment from terminal (it will go back to **base** environment every time you reset terminal session). Check it works:

```
$ conda activate cd-cleaner-conda-env
```
  
This step is done everytime so that you can run the script on the tool's environment. By default, terminal starts session on 'base' environment.


6. Make sure pip has installed the tool's python modules:
```
# Include the dot

$ pip install .
```


## 🧹  Instructions   

1. Deposit customer list data into the template found in **files/input** directory. **DO NOT CHANGE ITS NAME NOR COLUMN NAMES**.


2. Open terminal and activate environment:
```
$ conda activate cd-cleaner-conda-env
```

3. Navigate to tool directory and run **exe.py**:
```
$ cd ~/desktop/joor-cd-cleaner

$ python3 exe.py
```

4. You will need to enter:

  - DESIGNER ID
  - SSH USERNAME: This should be the same as on Postico - e.g. tsanmateu
  - SSH PASSWORD: Leave blank
  - PROD USERNAME: You should have this from step 1
  - PROD PASSWORD: You should have this on your 1password from step 1's request.
  
 
5. Let the script run, if there is no error, once it is finished it will direct you to check the files/output directory where the results file will be placed.
 

7. For best practices, delete this file or take it out of the output folder to avoid confusing next time you use the tool.Otherwise, make sure you check the last time it was updated in case the tool threw an error and you were collecting an old results file.

  
8. Slack Toni Sanmateu or Gabrielle Haam if an error occurs.


## Updating CD Cleaner Tool

1. Download the repository's zip file and remove the old one.

2. Open terminal in the tool's conda environment and run:

```
# Include the dot

$ pip install .
```

3. You should be able to use the script as usual. Check on the **version** section to see what has changed.

