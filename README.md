# Customer Data Cleaner

This script is made to be run from docker, therefore, make sure you have
downloaded and configured docker (more on installing docker:
https://github.com/joor/dev/blob/master/README.md)

The purpose of this script is to speed up the process of cleaning manual
customer data templates received on JIRA tickets for manual uploads.

The script features a range of functions with different functionality.
The combination of these functions executed with `pipeline_master()`.

## Instructions

The input files must be dropped inside the `files/input` directory in **X** 
format. Once the script has run, both the clean files and the omission files
will be found inside  `file/output` directory.
