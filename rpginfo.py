class RPGInfo():
    
    author = "Anonymous"
    
    def __init__(self,game_title):
        self.title = game_title
        
    def welcome(self):
        print("Welcome to "+self.title+".")
        
    @staticmethod
    def info ():
        print ("This was created using the OOP RPG creator.")
        
    @classmethod
    def credits (cls):
        print("Created by "+cls.author+".")