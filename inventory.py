"""
The inventory module holds the constructor for the player's inventory. 
An instance of the Inventory class holds a list of objects. The items'
attributes are changed according to their item type when they are used.
inventory = Inventory()
"""  
class Inventory():
    def __init__(self):
        self.inventory = []
        
        
    """
    Returns the item list
    inventory.get_inventory()
    """
    def get_inventory(self):
        return self.inventory
    
    
    """
    Modifies the item list by adding items, changing their quantities and/or
    durabilities. If the list self.inventory is empty, it will simply add the
    item. The variables pos and lst are used to search through fractions of the
    original list and locate a new item's intended position (it's sorted
    alphabetically). lst is the fraction of the list being searched, pos is the
    position from wich the comparison is made.
    inventory.set_inventory(item)
    """
    def set_inventory(self,item):
        
        if len(self.inventory) == 0:
            self.inventory.append(item)
            
        else:
            pos=int(len(self.inventory)/2)
            lst = self.inventory.copy()
            while self.inventory[pos].name != item.name and len(lst) != 1:
                if self.inventory[pos].name < item.name:
                    lst=self.inventory[pos:-1]
                else:
                    lst=self.inventory[:pos]
                pos = int(len(lst)/2)
                
            if lst[pos].name == item.name:
                lst[pos].quantity = lst[pos].quantity + item.quantity
            else:
                if item.name < lst[pos].name:
                    self.inventory = self.inventory[:pos]+[item]+self.inventory[pos:]
                else:
                    self.inventory = self.inventory[:pos+1]+[item]+self.inventory[pos+1:]
                    
                    
                    
    """
    Prints a list of the available items and their respective quantities. If
    the inventory list is empty, a warning is displayed.
    inventory.describe()
    """
    def describe(self):
        if len(self.inventory) == 0:
            print("Your backpack is empty...")
        else:
            for element in self.inventory:
                print(element.name.upper()+": "+str(element.quantity))
                
                
                
    """
    Uses the selected item stored in the inventory list. This substracts from
    the item's quantity or durability depending on the item type ("Consumable"
    or otherwise). If an item's quantity reaches 0, it is removed from the list.
    inventory.use_item(item)
    """        
    def use_item(self,item):
        if item.itype == "Consumable":
            item.quantity = item.quantity - 1
        else:
            item.durability = item.durability - 1
            if item.durability == 0:
                print("A "+item.name+" broke!")
                item.quantity = item.quantity - 1
        if item.quantity == 0:
            self.inventory.remove(item)
            print("Ran out of "+item.name+"!")
                
            
            
    """
    Discards a unit of the selected item. The item cannot be retrieved if it is
    dropped (currently not implemented in the main body)
    inventory.drop_item(item)
    """
    def drop_item(self,drop_ammount,item):
        self.quantity = self.quantity - drop_ammount
        print(item.name+" dropped!")
        if item.quantity == 0:
            self.inventory.remove(item)