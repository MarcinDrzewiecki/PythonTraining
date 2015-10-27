__author__ = 'drzewko'

def mod(a):
    if a > 0:
        return a
    else:
        return -a

def dlugosc(a,b):
    return mod(a[0]-b[0])+mod(a[1]-b[1])
all_cities = []
visited_cities =[]
ile_miast = int(input("How many cities? "))

for x in range(0,ile_miast):
    all_cities.append(list(input("podaj wspolzedne miast ")))

cities = list(input("Ktore miasta"))
for x in cities:
    visited_cities.append(all_cities[x])
ile_miast_zwiedzonych = len(visited_cities)

def droga_przebyta(visited_cities):
    starting_point = visited_cities[0]
    road = 0
    for x in range(0,ile_miast_zwiedzonych):
        road = road + dlugosc(starting_point,visited_cities[x])
        starting_point=visited_cities[x]
    return road + dlugosc(visited_cities[0],starting_point)

print(droga_przebyta(visited_cities))