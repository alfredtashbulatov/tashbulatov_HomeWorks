class user:
    first_name = ""
    last_name = ""
    
    def __init__(self, first_name):
        print("мое имя ", first_name)
        self.first_name = first_name
    
    def lastname(self, last_name):
        print("моя фамилия", last_name)
        self.last_name = last_name

    def flname(self):
        print(self.last_name, self.first_name)    
            

alfred = user("alfred")
alfred.lastname("tashbulatov")
alfred.flname()