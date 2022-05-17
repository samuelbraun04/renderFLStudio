from zipfile import ZipFile
import os

def makeZipFile(name, beatTitle):
    os.chdir("C:\\Users\\samlb\\Documents\\Image-Line\\FL Studio\\Projects\\finished\\UPLOAD")
    allFiles = next(os.walk("."), (None, None, []))[2]
    allStemFiles = []

    for counter in range(len(allFiles)):
        if str('STEMS - '+str(name)) in allFiles[counter]:
            allStemFiles.append(allFiles[counter])

    myZipFile = ZipFile(str(beatTitle)+'.zip', 'w')

    for counter in range(len(allStemFiles)):
        myZipFile.write(allStemFiles[counter])

    myZipFile.close()

    for counter1 in range(len(allStemFiles)):
        os.remove(allStemFiles[counter1])