from zipfile import ZipFile
from os import walk

def makeZipFile(name):
    allFiles = next(walk("C:\\Users\\samlb\\Documents\\Image-Line\\FL Studio\\Projects\\finished\\UPLOAD"), (None, None, []))[2]
    allStemFiles = []

    for counter in range(len(allFiles)):
        if str('STEMS - '+name) in allFiles[counter]:
            allStemFiles.append(allFiles[counter])

    myZipFile = ZipFile(r'C:\Users\samlb\Documents\Image-Line\FL Studio\Projects\finished\UPLOAD\beatTitle.zip', 'w')

    for counter in range(len(allStemFiles)):
        myZipFile.write('C:\\Users\\samlb\\Documents\\Image-Line\\FL Studio\\Projects\\finished\\UPLOAD\\'+allStemFiles[counter])

    myZipFile.close()