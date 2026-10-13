    elif current_room == 3:
        print("It appears you don't take care of your bathroom.")
        print("It is run down and dirty. You know your mother doesn't live here?")

    elif current_room == 4:
        print("It's chow time, buckaroo! Ya hungry?")
        print("There is a fridge in here. Inside is a plastic bottle of chocolate milk.")
        print("You drink it.")

    elif current_room == 5:
        print("What a boring place to write!")
        print("There's a chair and a desk without any drawers.")
        print("But there is a note. It reads:")
        print("'Do you see what's coming? Can you figure out your plot?'")

        writing_room_note = (
            "note that reads 'Do you see what's coming? Can you figure out your plot?'"
        )

        if writing_room_note not in inventory:
            inventory.append(writing_room_note)

    elif current_room == 6:
        if "paperclip" in inventory:
            print("Wowsers! You found a hidden room!")
            print("You see a hole in the wall just barely big enough for a paperclip.")
            print("You insert the paperclip into the hole and a secret passage opens.")
            print("Gee whiz, what do ya know? It's more prison.")
            print("You are in a maze of prisons.")
            print('"Sir, are you here to feed us?" an emaciated man asks you.')
            print("Is this a dream? No, this is the real world...")
            print("YOU WIN!!!")
            game_won = True
        else:
            print("Wowsers! You found a hidden room!")
            print("There is a hole in the wall, but you need something small to use it.")


def take_picture():
    if current_room == 1:
        print("You take a picture. This room is pretty bare.")
        photos.append("A photo of a bare room with a mattress in the corner.")
    elif current_room == 2:
        print("You take a picture. A washer and a dryer.")
        photos.append("A washer and dryer.")
    elif current_room == 3:
        print("You take a nice picture of your disgusting bathroom.")
        photos.append("A gross bathroom with a dirty sink, mirror, and tub.")
    elif current_room == 4:
        print("You snap a nice picture of your now empty fridge's contents.")
        photos.append("A sad open fridge.")
    elif current_room == 5:
        print("You take a somehow artistic photograph of the empty chair and desk.")
        photos.append("An artistic photograph of the empty chair and desk.")
    elif current_room == 6:
        print("You find no need to take a picture.")


def take_notes():
    note = input("You write: ")
    notes.append(note)


def action():
    print("\nWhat would you like to do?")
    print("7: inspect the area")
    print("9: take a picture")
    print("1: take notes")
    print("2: check inventory, notes, and photos")
    print("3: move on")

    choice = ask_for_number("> ")

    if choice == 7:
        inspect_room()
    elif choice == 9:
        take_picture()
    elif choice == 1:
        take_notes()
    elif choice == 2:
        show_status()
    elif choice == 3:
        print("You decide there's nothing else there.")
    else:
        print("That's not an option.")


def game_loop():
    while not game_won:
        location()
        action()

        if game_won:
            break

        keep_going = input("\nContinue on your shift? Press 'y' for yes, or 'n' for no. ")
        keep_going = keep_going.lower()

        if keep_going == "n":
            print("Ending kind of early.")
            break

        move_to_room()


game_loop()