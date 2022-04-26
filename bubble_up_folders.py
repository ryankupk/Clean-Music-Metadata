import os
import shutil

PC_PATH = r"D:\music"

def getAllFolderPaths(searchPaths, returnPaths):
    # base case: return when there are no more searchPaths to check
    if len(searchPaths) == 0:
        return returnPaths
    # recursive case: recurse in all found directories
    elif len(searchPaths) > 0:
        # if file, skip and continue to the next searchPath
        if   searchPaths[0].is_file():
            return getAllFolderPaths(searchPaths[1:], returnPaths)

        # if directory, recurse in that directory
        elif searchPaths[0].is_dir():
            # newSearchPaths is an iterator of all directories and files within searchPaths[0]
            with os.scandir(searchPaths[0].path) as newSearchPaths:
                for path in newSearchPaths:
                    if path.is_dir():
                        with os.scandir(path.path) as nextPaths:
                            # concatenate lists
                            returnPaths += [ path for path in getAllFolderPaths(list(nextPaths), returnPaths) if path not in returnPaths ]
                        # append current path to returnPaths
                        returnPaths.append(path)
            return getAllFolderPaths(searchPaths[1:], returnPaths)
            


def bubble(path, newName):
    # folder contents will be moved to a dummy folder before being replaced with the correct name to avoid name collisions
    dummyName = PC_PATH + r"\\dummy name"
    # move folder contents to dummy folder under the "root" directory
    shutil.move(path.path, dummyName)
    # delete the entire folder that the desired contents came from
    # not ideal, there may be other folders that we want. probably ideal to iterate across directories in this directory first before deleting
    shutil.rmtree(os.path.split(path)[0])
    # rename the dummy folder to the proper name given by user
    os.rename(dummyName, newName)

if __name__ == "__main__":
    with os.scandir(PC_PATH) as paths:
        for directory in getAllFolderPaths(list(paths), []):
            bubbleInput = input(f"Bubble directory {directory.path} to {PC_PATH}? (y or n): ")
            if bubbleInput.upper() == "Y":
                newName = f"{PC_PATH}\\" + input("New name?: ")
                bubble(directory, newName)