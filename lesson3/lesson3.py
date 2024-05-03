class user:
    age = 0

    def __init__(self, name):
        print("я создался!!")
        self.username = name
        
        
    def sayname(self):
        print("Меня зовут:", self.username)

    def sayage(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge
        print(newAge)






alfred = user("Альфред")        
alfred.sayname()
alfred.setAge(21)
alfred.sayage