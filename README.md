# Clean-Music-Metadata


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


## change_folders.py

Upon running, enter the directory to start at. It's assumed that directories are being changed in alphabetical order, therefore backtracking shouldn't be necessary. If the directory structure is

* PC_PATH  
    *  dir1  
    *  dir2  
    *  dir3 

and "dir2" is entered, dir3 will be the first directory considered.

User will be shown the current name of the directory and given an option to (k)eep, (c)hange, or (t)ype new title. If "k" is entered, the directory will be skipped and will is assumed to be correct. If "t" is entered, a new title can be typed and will be applied as the name of the directory and the program continues with the next directory. If "c" is entered, user can opt to remove sections of the current directory name (b)efore or (a)fter a given string. EX:

`Start after which directory? (nothing for the first): `Daft Punk - Discovery  
`Current name: Daft Punk - Homework [FLAC]  
(k)eep, (c)hange, or (t)ype new title?: `c  
`Remove (b)efore or (a)fter given string? `a  
`Remove everything after: `\[  
`Current name: Daft Punk - Homework  
(k)eep, (c)hange, or (t)ype new title?: `k  

changes the directory name to "Daft Punk - Homework". The same happens for (b)efore but characters prior to the entered string.

### Notes

Directory names are "pre-processed" to remove everything after and including the first \[ as I determined that no directories had anything that I wanted to keep after a \[. This isn't perfect, but it removes the necessity of changing several directory names manually because opting to keep those directory names will change them.

This is very specifically made for my own use cases (cleaning up music folder names to be standardized to "artist - album") so likely doesn't have much other utility. It works very well for this case and streamlines the process for changing hundreds of folder names with somewhat consistent or entirely inconsistent naming conventions.


## folder_diff.py

Grab all directories in `PC_PATH` and `PHONE_PATH`, identify differences, and apply "fixes" to the data in each until they are the same. Options are to delete a directory on the phone, delete a directory on the PC, copy a directory from the phone to the PC, copy a directory from the PC to the phone. It's assumed that the phone is rooted so that scripts can be run in the terminal to get a .txt file "directories.txt" which is placed in `PC_PATH` before starting. 

### Notes

This can be done in a much more automated and intelligent way if it were reasonably possible to programmatically copy/delete folders on a phone. I had tried a couple of things and none of them worked well, and it's really not that onerous to do it manually assuming that the two directories are already similar. In the worst case, all directories can be deleted from one and copied from the other, but that takes a long time in my experience. The program does little more than track progress for doing this all manually, though, but makes it much easier and faster to do so.

There's a bit of a hack in the main for loop to just restart the search from the beginning whenever a change is applied rather than properly indexing `pcList` and `phoneList`, but the search space is very small (sub-1000 directories in my case) so this doesn't hurt efficiency in any noticeable way.
