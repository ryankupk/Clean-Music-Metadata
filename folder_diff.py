import os

# cd /storage/0000-0000/Music
# sudo sh -c "sudo ls >> "directories.txt""

# path to first directory
PC_PATH = r'your dir here'
# get a list of all directories and files on the pc
pcList = os.listdir(PC_PATH)

# path to second directory
PHONE_PATH = r'your dir here\\directories.txt'
# open file with utf8 encoding for some reason
f = open(PHONE_PATH, encoding='utf8')
# get a list of all directories and files on the phone from the "directories.txt file"
phoneList = f.read().strip().split('\n')

# directories and files are not necessarily in the same order
# sort them so that they are guaranteed to be in the same order
pcList.sort()
phoneList.sort()

acceptableOptions = ["del pc", "del phone", "move pc to phone", "move phone to pc"]

def differenceFound(directory1, directory2, firstDevice, secondDevice):
    print(firstDevice + " has directory " + directory1)
    print("where " + secondDevice + " has directory " + directory2)
    fix = ""
    while fix not in acceptableOptions:
        print()
        print(acceptableOptions)
        fix = input("Fix applied: ")
    if fix == acceptableOptions[0]:
        delPC(directory1)
    elif fix == acceptableOptions[1]:
        delPhone(directory1)
    elif fix == acceptableOptions[2]:
        movePCToPhone(directory1)
    elif fix == acceptableOptions[3]:
        movePhoneToPC(directory1)


def delPC(directory):
    pcList.remove(directory)

def delPhone(directory):
    phoneList.remove(directory)

def movePhoneToPC(directory):
    pcList.append(directory)
    pcList.sort()

def movePCToPhone(directory):
    phoneList.append(directory)
    phoneList.sort()

    

if __name__ == "__main__":

    for i in range(len(pcList) if len(pcList) < len(phoneList) else len(phoneList)):
        # if a difference is found between phone and PC:
        if pcList[i] != phoneList[i]:
            # if a directory is found on the PC that is not on the phone:
            if pcList[i] < phoneList[i]:
                differenceFound(pcList[i], phoneList[i], "PC", "Phone")
            # if a directory is found on the phone that is not on the PC:     
            else:
                differenceFound(phoneList[i], pcList[i], "Phone", "PC")
                
            # restart search from the beginning
            i = 0
                    