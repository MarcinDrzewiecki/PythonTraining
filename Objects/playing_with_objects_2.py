__author__ = 'drzewko'


class Critter(object):
    def __init__(self,name,hunger=3,boredom=3):
        self.boredom = boredom
        self.hunger = hunger
        self.name = name

    def __pass_time(self):
        self.boredom+=1
        self.hunger+=1

    @property
    def mood(self):
        unhappiness = self.hunger+self.boredom
        if unhappiness <5:
            message = "szczesliwy" +str(unhappiness)
        elif 5<= unhappiness <15:
            message = "umiarkowany" + str(unhappiness)
        else:
            message = "wkurzony" + str(unhappiness)
        return message

    def talk(self):
        print("Nazywam sie",self.name, " i jestem teraz", self.mood)
        self.__pass_time()

    def eat(self,food=5):
        self.hunger-=food
        if self.hunger<0:
            self.hunger=0
        self.__pass_time()
        print(self.hunger)
        print(self.boredom)

    def play(self,fun=5):
        self.boredom-=fun
        if self.boredom<0:
            self.boredom=0
        self.__pass_time()
        print(self.hunger)
        print(self.boredom)

def main():
  crit_name = input("Podaj nazwe zwierzaka")
  crit = Critter(crit_name)
  choice=None

  while choice !="0":
      """0 - zakoncz
         1 - sluchaj co mowi
         2 - karm
         3 - baw sie
         """
      choice = input("Co wybierasz ?\n")
      if choice == "1":
          crit.talk()
      elif choice == "2":
          crit.eat()
      elif choice=="3":
          crit.play()
      else:
          print("nie ma takiej opcji, Sproboj ponownie")

main()