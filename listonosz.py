__author__ = 'drzewko'

all_cities = []
visited_cities_list =[]
how_many_cities = int(input("How many cities? "))
for x in range(0,how_many_cities):
    all_cities.append(list(input("Set the coordinates for city "+ str(x+1)+":\n")))

cities = list(input("To which cities the mailman will travel?\n"))
for x in cities:
    visited_cities_list.append(all_cities[x-1])
how_many_visited_cities = len(visited_cities_list)

def mod(a):
    if a > 0:
        return a
    else:
        return -a

def path(a,b):
    return mod(a[0]-b[0])+mod(a[1]-b[1])

def traveled_road(city):
    starting_point = city[0]
    road = 0
    for x in range(0,how_many_visited_cities):
        road = road + path(starting_point,city[x])
        starting_point=city[x]
    return road + path(city[x],city[0])

print(traveled_road(visited_cities_list))