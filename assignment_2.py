class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
# It should have a function ‘description()’ which prints the name and age of the dog.
    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)
# It should have a function ‘get_info()’ which prints the coat color of the dog.
    def get_info(self):
        print("Coat Color:", self.coat_color)
# Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
# It should have at least two methods of its own.
class JackRussellTerrier(Dog):

    def play_fetch(self):
        print("Jack Russell Terrier is playing fetch!")
    def Snore(self):
        print("Jack Russell Terrier is snoring!")

class Bulldog(Dog):

    def Barking(self):
        print("Bulldog is Barking!")
    def sleeping(self):
        print("Bulldog is sleeping!")

# Create objects and implement the above functionalities.
dog1 = Dog("Max", 3, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Rocky", 5, "White and Brown")
dog2.description()
dog2.get_info()
dog2.play_fetch()
dog2.Snore()
print()

dog3 = Bulldog("Zoro", 2, "White")
dog3.description()
dog3.get_info()
dog3.Barking()
dog3.sleeping()
