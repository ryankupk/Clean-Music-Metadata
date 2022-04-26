import eyed3
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3
import os

# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = "Token Entry"
# audiofile.tag.album = "Free For All Comp LP"
# audiofile.tag.album_artist = "Various Artists"
# audiofile.tag.title = "The Edge"
# audiofile.tag.track_num = 3

# audiofile.tag.save()

# audio = ID3("example.mp3")
# audio.add(TIT2(encoding=3, text=u"An example"))
# audio.save()

PC_PATH = r'D:\clean music metadata\\'
PHONE_PATH = r'S:\Music'

# determines whether there are any folders in the current directory
# returns true if a folder is found, false if only files exist
def checkIfFolders(path):
    with os.scandir(path) as all:
        for item in all:
            if item.is_dir():
                return True

    return False

# TODO: add functionality for doing the same on arbitrary file path
def deleteMetadata(path):
    with os.scandir(path) as currentFolder:
        # iterate across files
        for file in currentFolder:
            # delete metadata for each file
            if file.endswith(".flac"):
                deleteFLACMetadata(PC_PATH + file)
            elif file.endswith(".mp3"):
                deleteMP3Metadata(PC_PATH + file)
            else: # idk what this would be other than cover image but we probably want to delete these files
                print(file.name)


def deleteFLACMetadata(filePath):
    file = FLAC(filePath)

    file["isrc"] = ""
    file["copyright"] = ""
    file["publisher"] = ""
    file["releasecountry"] = ""
    file["composer"] = ""
    file["conductor"] = ""
    file["organization"] = ""
    file["encoder"] = ""
    file["description"] = ""


    file.save()

# TODO: add all mp3 tags
def deleteMP3Metadata(filePath):
    file = MP3(filePath, ID3=EasyID3)

    file['compilation'] = ""
    file['composer'] = ""
    file['copyright'] = ""
    file['encodedby'] = ""
    file['lyricist'] = ""
    file['media'] = ""
    file['mood'] = ""
    file['version'] = ""
    file['conductor'] = ""
    file['arranger'] = ""
    file['organization'] = ""
    file['isrc'] = ""
    file['discsubtitle'] = ""
    file['musicbrainz_trackid'] = ""
    file['website'] = ""
    file['replaygain_*_gain'] = ""
    file['replaygain_*_peak'] = ""
    file['musicbrainz_artistid'] = ""
    file['musicbrainz_albumid'] = ""
    file['musicbrainz_albumartistid'] = ""
    file['musicbrainz_trmid'] = ""
    file['musicip_puid'] = ""
    file['musicip_fingerprint'] = ""
    file['musicbrainz_albumstatus'] = ""
    file['musicbrainz_albumtype'] = ""
    file['releasecountry'] = ""
    file['musicbrainz_discid'] = ""
    file['asin'] = ""
    file['barcode'] = ""
    file['catalognumber'] = ""
    file['musicbrainz_releasetrackid'] = ""
    file['musicbrainz_releasegroupid'] = ""
    file['musicbrainz_workid'] = ""
    file['acoustid_fingerprint'] = ""
    file['acoustid_id'] = ""

    file.save()
    
    # todo: add id3 tags for Subtitle, Comments, Publisher, Author URL, Group Description :(((((((
    file = MP3(filePath)



    file.save()


if __name__ == "__main__":
    with os.scandir(PC_PATH) as folders:
        # iterate across all folders and files in PC_PATH
        for folder in folders:
            # do work only on folders
            if folder.is_dir():
                # change directory to the current folder being worked
                os.chdir(PC_PATH + folder)
                if not checkIfFolders(os.getcwd()):
                    deleteMetadata(os.getcwd())

                else:
                    pass



    # # get list of all folders in the base directory (not mp3 files)
    # baseFolders = [folder for folder in os.listdir(BASE_DIR) if not folder.endswith(".mp3")]
    # for folder in baseFolders:
