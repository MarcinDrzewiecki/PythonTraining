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
    all_cities.append(list(input("Set the coordinates for city "+ str(x+1)+":\n")))

cities = list(input("To which cities the mailman will travel?\n"))
for x in cities:
    visited_cities.append(all_cities[x-1])
ile_miast_zwiedzonych = len(visited_cities)

def droga_przebyta(city):
    starting_point = city[0]
    road = 0
    for x in range(0,ile_miast_zwiedzonych):
        road = road + dlugosc(starting_point,city[x])
        starting_point=city[x]
    return road + dlugosc(city[x],city[0])

print(droga_przebyta(visited_cities))