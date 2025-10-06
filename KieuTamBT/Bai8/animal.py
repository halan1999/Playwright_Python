class Animal:
    def bark(self):
        print("meo ... meo... !")

cat = Animal()
cat.bark()

class User:
    def __init__(self, Fname, Lname, age):
        self.Fname = Fname,
        self.Lname = Lname,
        self.age = int(age),
        isActive = True

    def Identify(self, age):
        if(age > 18):
            print("You are a mature")
        else:
            print("You are a kid")

sv1 = User("Alex", "Shander", 18)
sv2 = User("Mira","White", 20)

sv2.Identify(20)