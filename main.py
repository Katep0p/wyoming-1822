import sys
import time
from texts import allTexts
from soundplayer import playSoundfile, stopSoundFile
from random import randrange



#add names/verbs for functions

inventory = []
manBagInventory = ['money', 'tobacco', 'rope']
isLastPuzzleSolved = False

def printInventory():
    if inventory == []:
        print "\nYour inventory is empty."
        print "You are so broke, you cant afford to pay attention."
    else:
        print "\n", inventory


def yourName():
    while True:
        raw1 = raw_input("\nWhat is your name?\n")
        if raw1 != '':
            return raw1
        print "Oh come on! Every cowboy has a name."


def slow_text1(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = randrange(1, 3, 1) * 0.1
        time.sleep(seconds)



def askQuestionOne():
    choice1 = None #None is always true according to the while loop condition
    while (choice1 != "1" and choice1 != "2"): # if choice1 is not 1 and is not 2, then continue the loop
        choice1 = askQuestion(allTexts["options1"])
        if choice1 == "1":
            print (allTexts["choiceNo1"])
        elif choice1 == "2":
            print (allTexts["choiceNo2"])
        else:
            print ("\nImpossible move brah. Choose between 1 and 2.")


def askQuestionTwo():
    #if "rope" in inventory:
    #    print "....."

    choice2 = None
    while choice2 != "3":
        choice2 = askQuestion(allTexts["options2"])
        if choice2 ==  "1":
            print (allTexts["alternativeNo1"])
        elif choice2 == "2":
            print (allTexts["alternativeNo2"])
        elif choice2 == "3":
            print (allTexts["alternativeNo3"])
            continue
        #elif "rope" in inventory and choice2 == "4":

        else:
            print ("\nImpossible move brah.")


def askQuestionThree():
    choice3 = None
    while (choice3 != "1" and choice3 != "2"):
        choice3 = askQuestion(allTexts["options3"])
        if choice3 == "1":
            print (allTexts["altNo1"])
        elif choice3 == "2":
            print (allTexts["altNo2"])
        else:
            print ("\nImpossible move brah. Choose between 1 and 2.")


def listManBag():
    print len(manBagInventory), "items."
    print manBagInventory


def inv():
    print "Inventory: ", inventory


def examineInputForGlobalCommands(answer):
    if 'inventory' in answer:
        printInventory()
    elif 'help' in answer:
        print 'These are the commands you can use: help inventory'


def askQuestion(questionMsg):
    answer = raw_input(questionMsg)
    examineInputForGlobalCommands(answer)
    return answer


def pickUpObjectFromManBag():
    answer = askQuestion("What object do you wanna pick up?.")
    if answer == "money":
        moneyOption()
    elif answer == "tobacco":
        tobaccoOption()
    elif answer == "rope":
        ropeOption()
    else:
        print "You leave the manBag untouched."
    inv()


def addToInventory(item):
    inventory.append(item)


def moneyOption():
    money = askQuestion(allTexts["goldCoins"])
    if (money == "Y") or (money == "Yes") or (money == "YES") or (money == "yes"):
        print "Item stored in inventory."
        addToInventory("money")
        manBagInventory.remove("money")
    else:
        print "The money was put back in the manbag."


def tobaccoOption():
    tobacco = askQuestion(allTexts["finestTobacco"])
    if (tobacco == "Y") or (tobacco == "Yes") or (tobacco == "YES") or (tobacco == "yes"):
        print "Item stored in inventory."
        addToInventory("tobacco")
        manBagInventory.remove("tobacco")
    else:
        print "The tobacco was put back in the manbag."


def ropeOption():
    rope = askQuestion(allTexts["strongRope"])
    #if (rope == "Y") or (rope == "Yes") or (rope == "YES") or (rope == "yes"):
    if  rope in ['Y','y','yes','Yes','YES']:
        print "Item stored in inventory."
        addToInventory("rope")
        manBagInventory.remove("rope")
    else:
        print "The rope was put back in the manbag."

def main():

    while isLastPuzzleSolved == False:
        #or playerIsDead == True

        audioProcess = playSoundfile('A_Fistful_of_Dollars_-_Ennio_Morricone.mp3', loop=True)

        slow_text1(allTexts["intro"])

        playerName = yourName()

        slow_text1(allTexts["commandReminder"])

        slow_text1(allTexts["intro2"])

        #Here comes the first question
        print allTexts["question1"] % (playerName)

        askQuestionOne()

        #Question 2
        print allTexts["question2"]

        askQuestionTwo()

        listManBag()

        pickUpObjectFromManBag()

        #Question 3
        print allTexts["question3"]

        #if statement
        askQuestionThree()

        stopSoundFile(audioProcess)

        isLastPuzzleSolved = True



if __name__ == '__main__':
    main()
