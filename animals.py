__author__ = 'drzewiec'



class Animal(object):
    def sound(self):
        return "Generyczne zwierze nie wydaje dzwieku"

class Dog(Animal):
    def sound(self):
        return "hau hau"

class Cat(Animal):
    def sound(self):
        return "miau miau"

pies = Dog()

print pies.sound()
print Cat().sound()

animals = [Cat(),Dog(),Animal()]






























for animal in animals:
    print animal.sound()