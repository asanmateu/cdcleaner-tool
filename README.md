# Customer Data Cleaner

The purpose of this script is to speed up the process of cleaning manual customer data templates.

The script features a range of functions with different functionality that clean and flag errors and alers for each of the template columns.

It's launched from:
```
$ cd desktop/joor-cd-cleaner

$ python3 exe.py
```

## Instructions

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
  >>>>
  This step is done everytime so that you can run the script on the tool's environment. By default, terminal starts session on 'base' environment.
  >>>>

6. Make sure pip has installed the tool's python modules:
```
# Include the dot
$ pip install .
```

7. Deposit customer list data into the template found in **files/input** directory. **DO NOT CHANGE ITS NAME NOR COLUMN NAMES**.


8. Open terminal and activate environment:
```
$ conda activate cd-cleaner-conda-env
```

9. Navigate to tool directory and run **exe.py**:
```
$ cd ~/desktop/joor-cd-cleaner

$ python3 exe.py
```

10. You will need to enter:

  - DESIGNER ID
  - SSH USERNAME: This should be the same as on Postico - e.g. tsanmateu
  - SSH PASSWORD: Leave blank
  - PROD USERNAME: You should have this from step 1
  - PROD PASSWORD: You should have this on your 1password from step 1's request.
  
 
 11. Let the script run, if there is no error, once it is finished it will direct you to check the files/output directory where the results file will be placed.
 
  >>>>
  For best practices, delete this file or take it out of the output folder to avoid confusing next time you use the tool.
  Otherwise, make sure you check the last time it was updated in case the tool threw an error and you were collecting an old results file.
  >>>>
  
10. Slack Toni Sanmateu or Gabrielle Haam if an error occurs.
