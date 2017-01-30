import sys
import time
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



inventory = []
text = """Do your own thing, on your own terms and get what you came here for...

(*_*) ( *_*)>-o-o (-o_o)
"""
text2 = "\nBrown's Hole, Wyoming, 1822"

def yourName():
    while True:
        raw1 = raw_input("\nWhat is your name?\n")
        return raw1
        if raw1:
            break
        print "Oh come on! Every cowboy has a name."
        return None



def slow_text1(str):
#    for c in str:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        seconds = randrange(1, 3, 1) * 0.1
#        time.sleep(seconds)
    print str

def yoMama():
    choice1 = None #None is always true according to the while loop condition
    while (choice1 != "1" and choice1 != "2"): # if choice1 is not 1 and is not 2, then continue the loop
        choice1 = raw_input("1. You excuse yourself and walk towards the door." "\n2. You answer, your mama is in the wrong neighborhood.")
        if choice1 == "1":
            print ("""\nYou try to stand up only to realize you are tied to the chair. \nThe man gets up, takes the gun and starts walking towards you.""")
        elif choice1 == "2":
            print ("""\nThe man gets up, takes the gun and starts walking towards you.\nWas that really necessary? \nYou try to stand up only to realize you are tied to the chair.""")
        else:
            print ("\nImpossible move brah. Choose between 1 and 2.")

def inv():
    print "Inventory: ", inventory

def examineInputForGlobalCommands(question):
    if 'inventory' in question:
        printInventory()
        return True
    elif 'help' in question:
        print 'These are the commands you can use: help inventory'
        return True
    else:
        return False

def askQuestion(questionMsg):
    answer = raw_input(questionMsg)
    if examineInputForGlobalCommands(answer) == False:
        return answer
    return None

def manBag():
    question = askQuestion("What object do you wanna pick up?.")
    if question == "money":
        moneyOption()
    elif question == "tobacco":
        tobaccoOption()
    elif question == "rope":
        ropeOption()
    else:
        print "You leave the manBag untouched."
    inv()

def addToInventory(item):
    inventory.append(item)

def moneyOption():
    money = raw_input("\n 5 gold coins!\n Do you want to put them in your inventory? (Y/n)")
    if (money == "Y") or (money == "Yes") or (money == "YES") or (money == "yes"):
        print "Item stored in inventory."
        addToInventory("money")
        list1.remove("money")
    else:
        print "The money was put back in the manbag."

def tobaccoOption():
    tobacco = raw_input("\n Best tobacco in the country. You better save it for the right occasion. \n Do you want to put the item in your inventory? (Y/n)")
    if (tobacco == "Y") or (tobacco == "Yes") or (tobacco == "YES") or (tobacco == "yes"):
        print "Item stored in inventory."
        addToInventory("tobacco")
        list1.remove("tobacco")
    else:
        print "The tobacco was put back in the manbag."

def ropeOption():
    rope = raw_input("\n A strong rope. \n Do you want to put the item in your inventory? (Y/n)")
    #if (rope == "Y") or (rope == "Yes") or (rope == "YES") or (rope == "yes"):
    if  rope in ['Y','y','yes','Yes','YES']:
        print "Item stored in inventory."
        addToInventory("rope")
        list1.remove("rope")
    else:
        print "The rope was put back in the manbag."

#Start!
slow_text1(text)

x = yourName()


slow_text1(text2)
#Here comes the first question
print """\n
Sven the Bartender: Hey %s!!! Get your drunk ass outta here! The saloon is closed.
You lift your head up from the counter and try to remember what happened.
You look around only to discover an almost emptied bottle of scotch on the counter in front of you.
Just another one of those nights... You take another sip straight from the bottle.
You: Uuh Sven, thank god you are here. Where am I?
Unknown: In the wrong neighborhood, son.
You turn around and see a dodgy man sitting by a table in the corner.
There is a gun on the table.
What do you do?""" % (x)

yoMama()

#Question 2
print """Damn it! Why are you always getting into trouble?!
The man is almost next to you and you realize
you are still holding onto that bottle of scotch.
What do you want to do next?"""

#while loop
choice2 = None
while choice2 != "3":
    choice2 = raw_input("1. You finish the scotch in your own time." "\n2. You wait for the man to get closer and then you hit him over the head. \n3. You do both.")
    if choice2 ==  "1":
        print ("\nFinishing the scotch was awesome! Unfortunately, right when you are done, the guy hits you over the head with his gun and you pass out.")
        print ("You wake up the next day without your cowboy hat, horse and wallet, and to make matters worse you are still tied to the goddamned chair. Game over, pal.")
        print ("Let's try that one more time.")
    elif choice2 == "2":
        print ("\nYou successfully hit the guy over the head with the bottle. Not so smoothly however since the last bit of scotch that was in the bottle went all over you and your awesome cowboy outfit. Damn it!")
        print ("Let's try that one more time.")
    elif choice2 == "3":
        continue
    else:
        print ("\nImpossible move brah.")


print """\nYou empty the bottle and successfully hit the man over the head with it.
You use the broken bottle to cut off the roap tha tied your feet to the chair. Oh so smooth!
You and Sven walk over to the guy to take a closer look.
Sven: Let's go through his bag.
You open his bag and find:"""
#our list that counts the content and number of items
list1 = ['money', 'tobacco', 'rope']
print len(list1), "items."
print list1

manBag()

#Question 3
print """Sven: Ah shit, look at that. This is bad.
He picks up a shiny object from the man's front pocket. It's a gold star badge.
Sven: He is a sheriff, great... I'm going to be out of business by tomorrow if anyone finds out! What should we do?"""
#if statement
time.sleep(2)

choice3 = None
while (choice3 != "1" and choice3 != "2"):
    choice3 = raw_input("1. You take the badge from Sven and put it on your vest. There is a new sheriff in town." "\n2. You consider this not your problem and suggests that Sven gets rid of it.\n")
    if choice3 == "1":
        print ("\nSven likes the sound of that and serves you another drink.")
        print ("To be continued.")
    elif choice3 == "2":
        print ("\nSven: I don't want to keep it! Please just take it!")
        print ("You take the badge from Sven and put it on your vest. No one is going to mess with you from now on.")
        print ("To be continued.")
    else:
        print ("\nImpossible move brah. Choose between 1 and 2.")
