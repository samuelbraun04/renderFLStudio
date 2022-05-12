import pyautogui
from time import sleep
from re import sub
from os import walk
import os
import random
import sys

def basic(split):
    sleep(2)
    pyautogui.click(993,51)
    sleep(1)
    pyautogui.write(r'C:\Users\samlb\Documents\Image-Line\FL Studio\Projects\finished\UPLOAD')
    sleep(0.5)
    pyautogui.press('ENTER')
    sleep(1)
    pyautogui.click(818,936)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('BACKSPACE')
    sleep(0.5)
    if split == False:
        pyautogui.write(beatTitle)
    if split == True:
        pyautogui.write("STEMS - "+beatTitle)
    sleep(0.5)
    pyautogui.press('ENTER')
    sleep(1)
    if split == False:
        if (pyautogui.locateOnScreen('splitOn.png')) == None:
            pass
        else:
            pyautogui.click(965,636)
    if split == True:
        if (pyautogui.locateOnScreen('splitOff.png')) == None:
            pass
        else:
            pyautogui.click(965,636)
    
    sleep(1)
    pyautogui.click(1117,798)
    stillRendering = True
    while(stillRendering == True):
        if pyautogui.locateOnScreen('stillRendering.png') == None:
            stillRendering = False
        else:
            sleep(1)

def save(saveAs):
    pyautogui.click(pyautogui.locateOnScreen('startPoint.png'))
    sleep(1)
    if saveAs == True:
        pyautogui.hotkey('shift','ctrl','s')
    if saveAs == False:
        pyautogui.hotkey('ctrl','s')
    sleep(1)
    pyautogui.click(993,51)
    sleep(0.5)
    pyautogui.write(r"C:\Users\samlb\Documents\Image-Line\FL Studio\Projects\finished\toBeRendered")
    sleep(0.5)
    pyautogui.press('ENTER')
    sleep(1)
    pyautogui.click(277,936)
    sleep(0.5)
    pyautogui.write(beatTitle)
    sleep(0.5)
    pyautogui.press('ENTER')
    sleep(3)

keepGoing = True
illegalChars = ["<",">",":",'"',"/","\\","|","?","*"]

#Get used flps
textFile = open('rendered.txt', 'r')
lines = textFile.readlines()
lines = str(lines)
lines = lines[2:-2]
textFile.close()

#Split used flps into their seperate files
splitter = '.flp'
used =  [e+splitter for e in lines.split(splitter) if e]

files = next(walk(r'C:\Users\samlb\Documents\Image-Line\FL Studio\Projects\finished\toBeRendered'), (None, None, []))[2]

toBeAdded = []
for counter2 in range(len(files)):
    if (files[counter2] in used) == False:
        toBeAdded.append(files[counter2])

if len(toBeAdded) == 0:
    sys.exit("No files to render")

for counter3 in range(len(toBeAdded)):
    os.startfile(r"C:\\Users\\samlb\\Documents\\Image-Line\\FL Studio\\Projects\\finished\\toBeRendered\\"+str(toBeAdded[counter3]))

    getOut = False
    while(getOut == False):
        if pyautogui.locateOnScreen('isItOpen.png') == None:
            print("FL Studio not open yet")
            sleep(1)
        else:
            print("FL Studio is open")
            getOut = True

    sleep(4)

    print(toBeAdded)
    if ((pyautogui.locateOnScreen('doYouSave.png') != None) or (pyautogui.locateOnScreen('doYouSaveTwo.png') != None) or (pyautogui.locateOnScreen('doYouSaveThree.png') != None) or (pyautogui.locateOnScreen('doYouSaveFour.png') != None) or (pyautogui.locateOnScreen('doYouSaveFive.png') != None) or (pyautogui.locateOnScreen('doYouSaveSix.png') != None)):
        print('FL Studio needs to be saved')
        sleep(1)
        if pyautogui.locateOnScreen('saveVersionOne.png') != None:
            pyautogui.click(pyautogui.locateOnScreen('saveVersionOne.png'))
        if pyautogui.locateOnScreen('saveVersionTwo.png') != None:
            pyautogui.click(pyautogui.locateOnScreen('saveVersionTwo.png'))

        sleep(3)

        if pyautogui.locateOnScreen('needsToBeNamedTwo.png') != None:
            print("Needs to be named")
            pyautogui.click(679,52)
            sleep(1)
            pyautogui.write(r"C:\Users\samlb\Documents\Image-Line\FL Studio\Projects\finished\toBeRendered")
            pyautogui.press('ENTER')
            sleep(1)
            pyautogui.click(818,936)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('BACKSPACE')
            sleep(1)
            pyautogui.write(str(random.randint(1000000000,9999999999)))
            sleep(0.5)
            pyautogui.press('ENTER')
            sleep(1)

    #File "name"
    with open('new.txt') as f:
        girlNames = f.read()
    girlNames = sub( r"([A-Z])", r" \1", girlNames).split()
    with open('old.txt') as x:
        usedGirlNames = x.read()
    usedString = usedGirlNames
    usedGirlNames = sub( r"([A-Z])", r" \1", usedGirlNames).split()
    for counter in range(len(girlNames)):
        if girlNames[counter] in usedGirlNames:
            pass
        else:
            name = girlNames[counter]
            break
    with open('old.txt', 'w') as f:
        usedString = usedString+name
        f.write(usedString)

    #File bpm
    badBpm = True
    while(badBpm == True):
        try:
            bpm = int(input("What is this beat's BPM?: "))
        except Exception:
            print("Only numbers please.")
            bpm = 0
        else:
            if len(str(bpm))>3:
                print("Your BPM can't be longer than 3 digits.")
            else:
                badBpm = False

    #File key
    realKey = False
    allKeys = ["C flat minor","B minor","D flat minor","C sharp minor","D sharp major","E flat major","G flat minor","F sharp minor","G sharp major","A flat major","A flat minor" , "A flat major" , "A minor" , "A major" , "A sharp minor", "A sharp major", "B flat minor", "B flat major", "B minor", "B major", "C flat major", "C minor", "C major", "C sharp minor", "C sharp major", "D flat major", "D minor", "D major", "D sharp minor", "E flat minor", "E flat major", "E minor", "E major", "F minor", "F major", "F sharp minor", "F sharp major", "G flat major", "G minor", "G major", "G sharp minor"]

    while(realKey == False):
        key = str(input("What is this beat's Key? (Format examples: G sharp major, A flat minor, B major, F minor, etc): "))
        if key in allKeys:
            realKey = True
        else:
            print("Your input either isn't a real key or isn't following the proper format. You are a bozo.")

    #Song title tags
    tooLong = True
    while(tooLong == True):
        titleTags = str(input("Give the beat some adjectives (for beatstars title; should include: No Drums Type Beat): "))
        bad = False
        if len('" "'+name+titleTags) > 60:
            length = len(titleTags)+len(name)+3
            length = length-60
            print("Yikes. You have "+str(length)+" too many characters. Cut down.")
            bad = True
        for count6 in range(len(illegalChars)):
            if illegalChars[count6] in titleTags:
                print("Illegal char located. Please review your title.")
                bad = True
        if (bad == False):
            tooLong = False

    #Song tag tags
    getOut1 = False
    while(getOut1 == False):
        bad1 = False
        tag1 = str(input("Give the beat a tag (first out of 3): "))
        for count1 in range(len(illegalChars)):
            if illegalChars[count1] in tag1:
                print("Illegal char located. Please review your title.")
                bad1 = True
        if bad1 == False:
            getOut1 = True
    
    getOut2 = False
    while(getOut2 == False):
        bad2 = False
        tag2 = str(input("Give the beat a tag (second out of 3): "))
        for count2 in range(len(illegalChars)):
            if illegalChars[count2] in tag2:
                print("Illegal char located. Please review your title.")
                bad2 = True
        if bad2 == False:
            getOut2 = True
    
    getOut3 = False
    while(getOut3 == False):
        bad3 = False
        tag3 = str(input("Give the beat a tag (third out of 3): "))
        for count3 in range(len(illegalChars)):
            if illegalChars[count3] in tag3:
                print("Illegal char located. Please review your title.")
                bad3 = True
        if bad3 == False:
            getOut3 = True

    beatTitle = name.strip()+' - '+str(bpm)+' - '+key.strip()+' - '+titleTags.strip()+' ['+tag1.strip()+', '+tag2.strip()+', '+tag3.strip()+']'

    print("Rendering and saving process beginning in 5 seconds. Get FL Studio ready (put it on big monitor full screened).")
    sleep(5)

    #Save the .flp
    save(True)

    #Get mp3
    pyautogui.click(pyautogui.locateOnScreen('startPoint.png'))
    sleep(1)
    pyautogui.hotkey('ctrl','shift','r')
    basic(False)

    #Get wav
    pyautogui.click(pyautogui.locateOnScreen('altStartPoint.png'))
    sleep(1)
    counter = 1
    for pos in (pyautogui.locateAllOnScreen('On.png') or pyautogui.locateAllOnScreen('Off.png')):
        if counter == 10:
            pyautogui.click(pos)
            break
        counter = counter+1
    sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('startPoint.png'))
    sleep(0.5)
    pyautogui.hotkey('ctrl','r')
    basic(False)

    #Get zip (wav)
    pyautogui.click(pyautogui.locateOnScreen('altStartPoint.png'))
    sleep(1)
    pyautogui.hotkey('ctrl','r')
    basic(True)

    with open('rendered.txt', 'a') as f:
        f.writelines(''.join(str(toBeAdded[counter3])))
    with open('rendered.txt', 'a') as f:
        f.writelines(''.join(str(beatTitle+'.flp')))

    if (counter3 == 0):
        print(str(counter3+1) + " beat has been uploaded.")
    else:
        print(str(counter3+1) + " beats have been uploaded.")

print("Closing program.")
print("Remember to turn all the matching STEMS files into zip folders.")
print("You will never see this instance of this executable again in 5 seconds, so say farewell.")
sleep(5)