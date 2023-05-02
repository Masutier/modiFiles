import os
from django.conf import settings


def pickcss():
    online = settings.ONLINE
    return online


def createFolder(filepath, newName):
    os.makedirs(filepath + newName)
    endDir = filepath + newName
    return endDir


def newFolder(filepath, newfoldername, fileNamex):
    if newfoldername:
        folderExist = os.path.isdir(filepath + newfoldername)
        if not folderExist:
            endDir = createFolder(filepath, newfoldername)
        else:
            endDir = filepath + newfoldername
    else:
        folderExist = os.path.isdir(filepath + fileNamex)
        if not folderExist:
            endDir = createFolder(filepath, fileNamex)
        else:
            endDir = filepath + fileNamex

    return endDir
