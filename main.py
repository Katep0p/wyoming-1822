import sys
import time
from texts import allTexts
#from random import randrange


#PLAY BACKGROUND MUSIC


#mixer.init()
#pygame.mixer.pre_init(44100,16,2,4096)
#pygame.mixer.music.load("A_Fistful_of_Dollars_-_Ennio_Morricone.mp3")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)
#import pyglet
#sound = pyglet.media.load('A_Fistful_of_Dollars_-_Ennio_Morricone.wav', streaming=False)
#sound.play()
#pyglet.app.run()
#pyglet.mixer.pre_init(44100,16,2,4096)
#pyglet.mixer.music.set_volume(0.2)

#add names/verbs for functions

inventory = []

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
#    for c in str:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        seconds = randrange(1, 3, 1) * 0.1
#        time.sleep(seconds)
    print str


def askQuestionOne():
    choice1 = None #None is always true according to the while loop condition
    while (choice1 != "1" and choice1 != "2"): # if choice1 is not 1 and is not 2, then continue the loop
        choice1 = askQuestion("1. You excuse yourself and walk towards the door." "\n2. You answer, your mama is in the wrong neighborhood.")
        if choice1 == "1":
            print ("""\nYou try to stand up only to realize you are tied to the chair. \nThe man gets up, takes the gun and starts walking towards you.""")
        elif choice1 == "2":
            print ("""\nThe man gets up, takes the gun and starts walking towards you.\nWas that really necessary? \nYou try to stand up only to realize you are tied to the chair.""")
        else:
            print ("\nImpossible move brah. Choose between 1 and 2.")


def askQuestionTwo():
    #if "rope" in inventory:
    #    print "....."

    choice2 = None
    while choice2 != "3":
        choice2 = askQuestion("1. You finish the scotch in your own time." "\n2. You wait for the man to get closer and then you hit him over the head. \n3. You do both.")
        if choice2 ==  "1":
            print ("\nFinishing the scotch was awesome! Unfortunately, right when you are done, the guy hits you over the head with his gun and you pass out.")
            print ("You wake up the next day without your cowboy hat, horse and wallet, and to make matters worse you are still tied to the goddamned chair. Game over, pal.")
            print ("Let's try that one more time.")
        elif choice2 == "2":
            print ("\nYou successfully hit the guy over the head with the bottle. Not so smoothly however since the last bit of scotch that was in the bottle went all over you and your awesome cowboy outfit. Damn it!")
            print ("Let's try that one more time.")
        elif choice2 == "3":
            continue
        #elif "rope" in inventory and choice2 == "4":

        else:
            print ("\nImpossible move brah.")


def askQuestionThree():
    choice3 = None
    while (choice3 != "1" and choice3 != "2"):
        choice3 = askQuestion("1. You take the badge from Sven and put it on your vest. There is a new sheriff in town." "\n2. You consider this not your problem and suggests that Sven gets rid of it.\n")
        if choice3 == "1":
            print ("\nSven likes the sound of that and serves you another drink.")
            print ("To be continued.")
        elif choice3 == "2":
            print ("\nSven: I don't want to keep it! Please just take it!")
            print ("You take the badge from Sven and put it on your vest. No one is going to mess with you from now on.")
            print ("To be continued.")
        else:
            print ("\nImpossible move brah. Choose between 1 and 2.")


def listManBag():
    list1 = ['money', 'tobacco', 'rope']
    print len(list1), "items."
    print list1


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
    money = askQuestion("\n 5 gold coins!\n Do you want to put them in your inventory? (Y/n)")
    if (money == "Y") or (money == "Yes") or (money == "YES") or (money == "yes"):
        print "Item stored in inventory."
        addToInventory("money")
        list1.remove("money")
    else:
        print "The money was put back in the manbag."


def tobaccoOption():
    tobacco = askQuestion("\n Best tobacco in the country. You better save it for the right occasion. \n Do you want to put the item in your inventory? (Y/n)")
    if (tobacco == "Y") or (tobacco == "Yes") or (tobacco == "YES") or (tobacco == "yes"):
        print "Item stored in inventory."
        addToInventory("tobacco")
        list1.remove("tobacco")
    else:
        print "The tobacco was put back in the manbag."


def ropeOption():
    rope = askQuestion("\n A strong rope. \n Do you want to put the item in your inventory? (Y/n)")
    #if (rope == "Y") or (rope == "Yes") or (rope == "YES") or (rope == "yes"):
    if  rope in ['Y','y','yes','Yes','YES']:
        print "Item stored in inventory."
        addToInventory("rope")
        list1.remove("rope")
    else:
        print "The rope was put back in the manbag."

#Start!

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

print """\nYou empty the bottle and successfully hit the man over the head with it.
You use the broken bottle to cut off the roap tha tied your feet to the chair. Oh so smooth!
You and Sven walk over to the guy to take a closer look.
Sven: Let's go through his bag.
You open his bag and find:"""

listManBag()

pickUpObjectFromManBag()

#Question 3
print """Sven: Ah shit, look at that. This is bad.
He picks up a shiny object from the man's front pocket. It's a gold star badge.
Sven: He is a sheriff, great... I'm going to be out of business by tomorrow if anyone finds out! What should we do?"""
#if statement

askQuestionThree()
