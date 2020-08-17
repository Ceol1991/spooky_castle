from rpginfo import RPGInfo
from initialize import game_start
import sys

#The main module stablishes the possible commands and events that take place in the game.

current_room, fists, key, kitchen, dining_hall, ballroom, gold, morgan, eustace, dave, backpack, spooky_castle=game_start()

instfile = open("instructions.txt")

print("\n\nPlease enter 'instructions' to see an explanation about the game")

while True:
    print("\n")
    current_room.describe()        
    current_room.get_details()
    command = input("> ")
    print("\n")
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        if current_room.character is None or current_room.character.forf != "Enemy":
            current_room = current_room.move(command)
        else:
            print(current_room.character.name+" blocks your path!")
        
    elif command == "talk":
        if current_room.character is None:
            print("There is no one here...")
        else:
            current_room.character.talk()
            
    elif command == "fight":
        if current_room.character is None:
            print("There is no one here...")
            
        else:
            if current_room.character.forf != "Enemy":
                print("Hey, don't fight!")
            else:
                weapon = None
                print("What will you fight with?")
                fight_with = input("> ")
                print("\n")
                for element in backpack.inventory:
                    if element.name == fight_with:
                        weapon = element
                        current_room.character.fight(fight_with)
                        break
                if weapon == None:
                    print("You don't have this weapon...")
                    continue
                if fight_with == current_room.character.weakness:
                    backpack.use_item(weapon)
                if current_room.character.status == "Dead":
                    current_room.set_character(None)
                else:
                    print("Game Over...")
                    RPGInfo.credits()
                    sys.exit()
                    
    elif command == "hug":
        if current_room.character is None:
            print("There is no one here...")
        if current_room.character.forf == "Enemy":
            print("You shouldn't hug enemies...\n\nGame Over.")
            RPGInfo.credits()
            sys.exit()
        elif current_room.character.forf == "Friend":
            current_room.character.hug()
            
    elif command == "bribe":
        bargain = None
        if current_room.character is None:
            print("There is no one here...")
            continue
        if current_room.character.forf == "Enemy":
            bribe = input("What will you offer?\n>")
            for element in backpack.inventory:
                if element.name == bribe:
                    bargain = element
                    break
            if bargain == None:
                print("You don't have this item.")
                continue
            if bribe == current_room.character.interest:
                backpack.use_item(bargain)
                current_room.character.bribe(current_room.character.interest)
                current_room.set_character(None)
            else:
                print("The enemy doesn't seem interested...")
        else:
            print("There's no one to bribe, bud.")
            
    elif command == "search":
        if current_room.character is not None and current_room.character.forf == "Enemy":
                print(current_room.character.name+" blocks your path!")
        else:
            if current_room.item is not None:
                print("You found "+current_room.item.name+"!")
                backpack.set_inventory(current_room.item)
                current_room.item = None
            else:
                print("There is nothing here...")
                
    elif command == "inventory":
        backpack.describe()
        
    elif command == "exit":
        print("Closing game.")
        RPGInfo.credits()
        sys.exit()
        
    elif command == "go outside":
        if key in backpack.inventory and current_room == dining_hall:
            print("You win!\n")
            RPGInfo.credits()
            sys.exit()
        else:
            print("You can't get out yet...")
    
    elif command == "instructions":
        for line in instfile:
            print(line)
            
    else:
        for element in backpack.inventory:
            if element.name == command:
                check = True
                break
        if check == True:
            element.describe()
            element.get_details()

        else:
            print("Invalid command.")