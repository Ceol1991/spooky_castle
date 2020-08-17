"""
Creates a character instance that can be either a friend or an enemy
character = Character(name,description)
"""
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.forf ="Friend"

    """
    Prints a description of the character
    character.describe()
    """
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    """
    Set what this character will say when talked to
    character.set_conversation(text)
    """
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    """
    Returns a character's conversation lines
    character.get_conversation()
    """
    def get_conversation(self):
        return self.conversation

    """
    Displays the conversation atribute
    character.talk()
    """
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    """
    If the character is not an enemy, it will simply show a warning that the
    character has no will to fight
    character.fight
    """
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
"""
Creates an instance of the Enemy subclass of the Character class
enemy = Enemy(Character)
"""    
class Enemy(Character):
    
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness = None
        self.forf = "Enemy"
        self.status = "Alive"
        self.interest = None
    """
    Sets the interest attribute which defines what the enemy can be bribed with
    to avoid a battle. Some enemies may not have any interests.
    enemy.set_interest(interest)
    """    
    def set_interest(self,interest):
        self.interest = interest
    
    """
    Returns the interest attribute of an enemy
    enemy.get_interest()
    """
    def get_interest(self):
        return self.interest
    """
    Sets the weakness attribute which defines what an enemy can be beaten with
    in battle. Some enemies may not have any weaknesses
    enemy.set_weakness(weakness)
    """
    def set_weakness(self,weakness):
        self.weakness = weakness
    
    """
    Returns the wakness atribute of an enemy
    enemy.get_weakness()
    """    
    def get_weakness(self):
        return self.weakness
    """
    Uses an item to fight an enemy. If combat_item matches the enemy's weakness
    attribute, the enemy is then defeated and removed from the room. Otherwise 
    it results in Game Over.
    enemy.fight(weapon)
    """
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            self.status = "Dead"
        else:
            print(self.name + " crushes you, puny adventurer")
    """
    Tries to use and item to convince the enemy not to fight. If the enemy´s
    interest attribute is None, negotiations will fail and a warning will be
    shown. Otherwise, the enemy will be convinced and removed from the room.
    The item check to see if it aligns with the enemy's interest atribute is
    done in the main body (will be moved here later)
    enemy.bribe(item)
    """
    def bribe(self,interest):
        if interest is None:
            print("You can't bribe this enemy!")
        else:
            print("You offered the enemy "+self.interest+" and they backed down.")
            self.status = "Dead"

"""
Creates an instance of the Friend sublcass of the Character class
friend = Friend(Character)
"""          
class Friend(Character):
        
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
    """
    Just for fun
    character.hug()
    """    
    def hug(self):
        print("You hugged your firend. You are filled with DETERMINATION")