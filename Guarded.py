"""
Author: Randall Eliot Ingalls

Name: Guarded

Start Date: 3/24/2026

Purpose: The purpose of this program is to provide entertainment to its user.
The program is a role playing game where the user is a security guard who goes
through a shift. Players must check locations and investigate incidents.

Notes: As of 4/13/2026, I've written out a bit complicated if/else/elif program for each room that automatically
stores information from each room. I was going to write each room as a function, but I focused on the same if/else/elif
design for each room. This is the first video game I've ever made, and it's certainly not efficient, and the AI ChatGPT 
is helping me learn this stuff. I made some of the original code into notes at the bottom of the program.

"""
print("You wake up in your bed. Welcome to the world of the living. It's a wonderful day to be alive!")

inventory = []
currentInventory = 1
notes = []
photos = []
room = {1:"bedroom", 2:"washroom", 3:"bathroom", 4:"kitchen", 5:"writing room", 6: "secret room"}
currentRoom = 1
 
def moveToRoom():
    global currentRoom

    choice = int(input("Which room would you like to go to? "))

    if choice in room:
        currentRoom = choice
        print("You get along to ", room[currentRoom] + ".")

    else:
        print("You've chosen incorrectly, Friend. How about another room from 1-5?")


def location():

    if currentRoom == 1:
        print("You are in the dreary", room[currentRoom],".")
    elif currentRoom == 2:
        print("You are in the somewhat gross", room[currentRoom],".")
    elif currentRoom == 3:
             print("You are in the definitely gross", room[currentRoom],".")
    elif currentRoom == 4:
            print("You are in the empty-appearing", room[currentRoom],".") 
    elif currentRoom == 5:
        print("You are in the little-used", room[currentRoom],".")         
    elif currentRoom == 6:
        print("I wasn't aware of this secret room!")

def action():
    investigate = int(input("What would you like to do? Press 7 to inspect the area, 9 to take a picture, 1 to take notes, or 3 to move on."))
    if currentRoom == 1:
        if investigate == 7:
            print("Everything seems to be in order. You should know. Wait, what's that? A paperclip. You pick it up.")
            inventory.append('paperclip') 
   
        elif investigate == 9:
            print("You take a picture. This room is pretty bare. Must be nice to sleep in.")
            photos.append(" A photo of a bare room with a mattress in the corner. ")
        
        elif investigate == 1:
            note = input("You write: ")
            notes.append(note)
   
        elif investigate == 3: 
            print("You decide there's nothing there.")
   
        else:
            print("That's not an option.")

    elif currentRoom == 2:
        if investigate == 7:
                print("You find a pair of dirty trousers with a piece of paper and the writing 'Try six'.")
                inventory.append("Note that reads 'Try six'.")

        elif investigate == 9 and currentRoom == 2:
                print("You take a picture. A washer and a dryer.")    
                photos.append(" A washer and dryer. ")

        elif investigate == 1 and currentRoom == 2:
                note = input("You write: ")
                notes.append(note)

        elif investigate == 3 and currentRoom ==2:
                print("You decide there's nothing there.") 
                int(input("Which room would you like to go to?", room))
        
        else:
                print("That's not an option.")    

    elif currentRoom == 3:

        if investigate == 7:
                    print("It appears you don't take care of your bathroom. It is run down and dirty. You know your mother doesn't live here?")
                    inventory.append("Note that reads 'Try six'.")

        elif investigate == 9 and currentRoom == 3:
                    print("You take a nice picture of your disgusting bathroom.")    
                    photos.append(" A gross bathroom. A dirty sink and mirror with a tub in the corner that needs to be scrubbed.")

        elif investigate == 1 and currentRoom == 3:
                    note = input("You write: ")
                    notes.append(note)
        
        elif investigate == 3 and currentRoom == 3:
                    print("You decide there's nothing else there.") 
                    int(input("Which room would you like to go to?", room))
        
        else:
                    print("That's not an option.")    

    elif currentRoom == 4:
        if investigate == 7:
            print("It's chow time, buckaroo! Ya hungry? It looks like there's a fridge in here. Nothing else. Inside the fridge is a pastic bottle of chocolate milk. You drink it.")

        elif investigate == 9 and currentRoom == 4:
                    print("You snap a nice picture of your now empty fridge's contents. ")    
                    photos.append(" A sad open fridge.")

        elif investigate == 1 and currentRoom == 4:
                    note = input("You write: ")
                    notes.append(note)
        
        elif investigate == 3 and currentRoom == 4:
                    print("You decide there's nothing else there.") 
                    int(input("Which room would you like to go to?", room))


    elif currentRoom == 5:
        if investigate == 7:
                            print("What a boring place to write! There's a chair and desk without any drawers. You can barely call it a desk, really. But there is a note. It reads: ''Do you see what's coming? Can you figure out your plot?''")
                            inventory.append("Note that reads 'Do you see what's coming? Can you figure out your plot?'.")

        elif investigate == 9 and currentRoom == 5:
                        print("You take a somehow artistic photograph of the empty chair and desk.")    
                        photos.append(" A somehow artistic photograph of the empty chair and desk.")

        elif investigate == 1 and currentRoom == 5:
                        note = input("You write: ")
                        notes.append(note)
        
        elif investigate == 3 and currentRoom == 5:
                        print("You decide there's nothing else there.") 
                        int(input("Which room would you like to go to?", room))

    elif currentRoom == 6:
        if investigate == 7:
            print("Wowsers! You found a hidden room! It's the last room inside of these wonderful walls! There's nothing in... Wait, you see a hole in the wall just barely big enough a paperclip.")

        elif investigate == 9 and currentRoom == 6:
                            print("You find no need to take a picture.")    

        elif investigate == 1 and currentRoom == 6:
                            note = input("You write: ")
                            notes.append(note)
        
        elif investigate == 3 and currentRoom == 6:
                            print("You think about leaving the room.") 
                            int(input("Which room would you like to go to? Press ''6'' to stay in this room.", room))

        elif investigate == 7 and inventory == "paperclip":
             print("You insert the paperclip into the hole and... what's this? A secret passage has opened up! Gee whiz, what do ya know? It's more prison. You are in a maze of prisons. You stare at the innumerable cells and their occupants. ''Sir, are you here to feed us? An emaciated man asks you. Is this a dream? No, this is the real world... YOU WIN!!!")   
"""
        elif investigate == 5 and currentRoom == 6 and inventory == paperclip: use paperclip in hole to open up ending of game.
"""        

def continueGame():

    keepGoing = str(input("Continue on your shift? Press 'y' for yes, or 'n' for no.").lower())
        
    if keepGoing == "y":
        int(input("Great! Let's go! Which room would you like to go to?", currentRoom))

        print("Inventory: ", inventory)
        print("Notes: ", notes)
        
    elif keepGoing == "n":
        print("Ending kind of early.")
    



def gameLoop():
    while True:
        location()
        action()
        moveToRoom()
        
        keepGoing = input("Continue on your shift? Press 'y' for yes, or 'n' for no.").lower()

        if keepGoing == "n":
            print("Ending kind of early.")
            break

"""        

def actionRoomOne():
    investigateRoomOne = (int(input("What would you like to do? Press 7 to inspect the area, 9 to take a picture, 1 to write notes, or 3 to move on.")))    

    if investigateRoomOne == 7:
        print("You find a phone number in the pair of shoes that reads 1-234-678-9100, drawings of well-endowed people in the textbooks, and a paperclip on the bookself. You take the paperclip.")
        inventory.append("Paperclip. ")

    elif investigateRoomOne == 9:
        print("You take a picture of the room.")
        photos.append("Table with textbooks, empty bookshelf, two-and-a-half pairs of shows. ")

    elif investigateRoomOne == 1:
        global notes; input(f"You pull out your pad and write:")

    elif investigateRoomOne == 3:
        print("You move onto the next room.")    

def actionRoomTwo():
    investigateRoomTwo = (int(input("What would you like to do? Press 7 to inspect the area, 9 to take a picture, 1 to write notes, or 3 to move on.")))    

    if investigateRoomTwo == 7:
        print("You find a note on a single table that reads, 'What is this place even? How is your section?'")
        inventory.append("Letter that reads 'What is this place even? How is your section?'. ")

    elif investigateRoomTwo == 9:
        print("You take a picture of the room.")
        photos.append("Room 2: Table with letter on it. ")

    elif investigateRoomTwo == 1:
        global notes; input(f"You pull out your pad and write:")

    elif investigateRoomTwo == 3:
        print("You move onto the next room.")   

def actionRoomThree():
    investigateRoomThree = (int(input("What would you like to do? Press 7 to inspect the area, 9 to take a picture, 1 to write notes, or 3 to move on.")))    

    if investigateRoomThree == 7:
        print("You find a phone number in the pair of shoes that reads 1-234-678-9100, drawings of well-endowed people in the textbooks, and a paperclip on the bookself. You take the paperclip.")
        inventory.append("Paperclip. ")

    elif investigateRoomThree == 9:
        print("You take a picture of the room.")
        photos.append("Table with textbooks, empty bookshelf, two-and-a-half pairs of shows. ")

    elif investigateRoomThree == 1:
        global notes; input(f"You pull out your pad and write: ")

    elif investigateRoomThree == 3:
        print("You move onto the next room.")    
"""

gameLoop()