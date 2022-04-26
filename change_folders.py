import os


def removeParts(name, place):
    place = place.upper()
    remove = input("Remove everything " + ("after: " if place == "A" else "before: "))
    index = name.find(remove)
    return name[0:index] if place == "A" else name[index:]

def switchFrontBack(name, position):
    # find the point along which to switch positions
    index = name.find(position)
    # get the parts of the name leading up to the switch position
    front = name[0:index].strip()
    # get the parts of the name after the switch position
    back  = name[index+1:].strip()
    return back + " - " + front  

# path to first directory
PC_PATH = r'D:\music'
PHONE_PATH = r'S:\Music'


if __name__ == "__main__":
    # get a list of all directories and files on the pc
    directoryList = os.listdir(PC_PATH)
    startAfter = input("Start after which directory? (nothing for the first): ")
    if startAfter != "":
        i = 0
        while startAfter.upper() not in directoryList[i].upper():
            i += 1
        directoryList = directoryList[i+1:]
    

    for name in directoryList:
        keep = "C"
        switch = "N"
        newName = None
        if name.find("[") != -1:
            newName = name[0:name.find("[")]
        if name.find("(20") != -1:
            newName = name[0:name.find("(20")]
        
        while keep.upper() == "C":
            print(f"Current name: {(name if not newName else newName)}")
            # determine if name should be left as is or changed
            keep = input("(k)eep, (c)hange, or (t)ype new title?: ")
            if keep.upper() == "C":
                # determine if we want to remove text before or after the string provided by user
                before = input("Remove (b)efore or (a)fter given string? ")
                if before.upper() == "A" or before.upper() == "B":
                    # remove selected parts of text
                    newName = removeParts(name if not newName else newName, before.upper())
                else: continue
            elif keep.upper() == "T":
                newName = input("Enter new name: ")
            else: break
                
        if keep.upper() != "T":
            print(f"Current name: {(name if not newName else newName)}")
            switch = input("Switch artist and album? (y or n): ")
            if switch.upper() == "Y":
                # switch front and back, assign to newName
                newName = switchFrontBack(name if not newName else newName, input("Position to switch at: "))


        # rename the directory with newName
        if newName:
            try:
                os.rename(os.path.join(PC_PATH, name),
                          os.path.join(PC_PATH, newName))
            except OSError:
                newName = input("Write failed, type new album name: ")
                os.rename(os.path.join(PC_PATH, name),
                          os.path.join(PC_PATH, newName))
