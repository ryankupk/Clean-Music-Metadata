﻿# Clean-Music-Metadata


## bubble_up_folders.py

Recursively find all directories within `PC_PATH`, iterate across those directories that are one level deeper than `PC_PATH`, prompt the user whether they should be brought up to the same depth as other folders in `PC_PATH`. EX:

* PC_PATH  
    *  dir1  
        *  dirA
    *  dir2  
    *  dir3  

will become

* PC_PATH  
    *  dirA  
    *  dir2  
    *  dir3  

if "y" is selected for dira. dira can be given a new name and will replace dir1

### Bugs/TODOs

Currently, the process is designed to correct a situation such as:

* PC_PATH
    * dir1
        * dirA
            * song
            * song
            * song
            * ....

where the desired result is simply

* PC_PATH
    * dirA
        * song
        * song
        * song
        * ....

so the current implementation is not very adaptive for other scenarios. For example, everything within dir1 -- other than dirA -- will be deleted when dirA is brought up to be under `PC_PATH`.

### Notes

Some amount of human input is still required because many subdirectories will be skipped, and the name of the subdirectory may not be what is ultimately desired under `PC_PATH` so it is renamed before being moved. It can be fully automated in the general case where all subdirectories should be brought up under `PC_PATH` by modifying the for loop within main
