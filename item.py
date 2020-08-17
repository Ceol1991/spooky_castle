"""
Class for the items found across the rooms.
"""

class Item():
    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        self.itype = None
        self.quantity = 0
        self.durability = 0
    """
    Returns the item's name atribute.
    item.name()
    """    
    @property            
    def name(self):
        return self._name
    
    """
    Sets the item's name atribute.
    item.name(name)
    """
    @name.setter
    def name(self,item_name):
        self._name = item_name
    """
    Returns the item's flavor text
    item.description()
    """    
    @property
    def description(self):
        return self._description
    
    """
    Sets the item's flavor text
    item.description(text)
    """
    @description.setter
    def description(self,item_description):
        self._description = item_description
    """
    Returns the item type.
    item.itype()
    """
    @property
    def itype(self):
        return self._itype
    """
    Sets the item's type. An item can be either "Consumable" or "Usable"
    item.itype(item_type)
    """
    @itype.setter
    def itype(self,itype):
        self._itype = itype
    """
    Returns the item's quantity.
    item.quantity()
    """
    @property
    def quantity(self):
        return self._quantity   
     
    """
    Sets the amount of units of a certain item the player can find inside a room.
    item.quantity(number)
    """
    @quantity.setter
    def quantity(self,item_quantity):
        self._quantity = item_quantity
    """
    Returns the number of times an item can be used.
    item.durability()
    """
    @property
    def durability(self):
        return self._durability
    """
    Sets the number of times an item can be used.
    item.durability(number)
    """
    @durability.setter
    def durability(self,item_durability):
        self._durability = item_durability
    """
    Prints a description of the selected item. Descriptions have to be typed in
    the main body. A way to get them from a text file will be implemented later.
    item.describe()
    """
    def describe(self):
        print(self.description)
    """
    Provides the details of the selected item (could be merged with describe method)
    item.get_details()
    """
    def get_details(self):
        print("The "+self.name+" is a "+self.itype+" item. You have "+str(self.quantity)+" unit(s) left.")
        if self.itype != "Consumable":
            print("You have "+str(self.durability)+" use(s) left.")
        