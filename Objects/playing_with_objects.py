__author__ = 'drzewko'


class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("Critter count is eaqual to ", Critter.total)

    def __init__(self,name):
        print("A new critter was born!")
        self.name=name
        Critter.total +=1

    def set_name(self, new_name):
        if new_name == "":
            print("nie mozesz pało!")
        else:
            self.name=new_name
            print("Approved!")

    def talk(self):
        print("Arghhhh! Jestem", self.name)



crit1 = Critter("Ziutek")
crit2 = Critter("Leszek")
print(crit1.name)

crit1.talk()
crit2.talk()

Critter.status()
crit1.set_name("xxx")
crit1.talk()