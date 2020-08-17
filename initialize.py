from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item
from inventory import Inventory

"""
Creates and connects all the rooms and creates and locates all the items and
characters (enemies or friends) inside the different rooms. The starting 
location is also set here. Room descriptions are taken from a room.txt file.
Returns all items, inventory, characters and rooms.
"""

def game_start():
    fname = "rooms.txt"
    fh = open(fname)
    
    spooky_castle = RPGInfo("The Spooky Castle")
    spooky_castle.welcome()
    RPGInfo.info()
    RPGInfo.author = "Santiago Fernández de la Torre"
    
    for line in fh:
        if line.startswith("Kitchen:"):
            pieces = line.split(":")
            kitchen_description = pieces[1].strip()
            
        if line.startswith("Ballroom"):
            pieces = line.split(":")
            ballroom_description = pieces[1].strip()
            
        if line.startswith("Dining Hall"):
            pieces = line.split(":")
            dininghall_description = pieces[1].strip()
    
    backpack = Inventory()
    
    kitchen = Room("Kitchen")
    kitchen.set_description(kitchen_description)
    
    ballroom = Room("Ballroom")
    ballroom.set_description(ballroom_description)
    
    dining_hall = Room("Dining hall")
    dining_hall.set_description(dininghall_description)
    
    #print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
    
    kitchen.link_room(dining_hall,"south")
    
    dining_hall.link_room(kitchen,"north")
    dining_hall.link_room(ballroom,"east")
    
    ballroom.link_room(dining_hall,"west")
    
    dave = Enemy("Dave","A smelly zombie!\n")
    dave.set_conversation("BrAiNs!\n")
    dave.set_weakness("cheese")
    
    eustace = Enemy("Eustace","A very angry buttler")
    eustace.set_conversation("Justicia social!")
    eustace.set_weakness(None)
    eustace.set_interest("gold coin")
    
    morgan = Friend("Morgan Freeman","You just met GOD")
    morgan.set_conversation("Hello, my child.")
    
    cheese = Item("cheese")
    cheese.description = "A piece of moldy cheese"
    cheese.itype = "Consumable"
    cheese.quantity = 1
    kitchen.set_item(cheese)
    
    gold = Item("gold coin")
    gold.description = "A gold coin from ancient times"
    gold.itype = "Consumable"
    gold.quantity = 1
    dining_hall.set_item(gold)
    
    # sword = Item("sword")
    # sword.description = "An old rusty sword"
    # sword.itype="Usable"
    # sword.quantity = 1
    # dining_hall.set_item(sword)
    
    key = Item("key")
    key.description = "A key used to get out of the spooky castle"
    key.itype = "Usable"
    key.quantity = 1
    key.durability = 1
    ballroom.set_item(key)
    
    fists = Item("fists")
    fists.description = "Who needs weapons when you have these cannons?"
    fists.itype = "Usable"
    fists.quantity = 999
    fists.durability = 999
    backpack.set_inventory(fists)
    
    kitchen.set_character(morgan)
    dining_hall.set_character(dave)
    ballroom.set_character(eustace)
    
    current_room = kitchen
    
    return current_room, fists, key, kitchen, dining_hall, ballroom, gold, morgan, eustace, dave, backpack, spooky_castle