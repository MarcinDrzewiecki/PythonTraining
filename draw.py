import random


def group_name(i):
    return "Group " + str(i)


team_number = int(raw_input("Number of teams: "))
group_number = int(raw_input("Number of groups: "))

groups = {}
teams = []

for i in range(1, group_number + 1):
    groups[group_name(i)] = []

for i in range(1, team_number + 1):
    team = [raw_input("Team name " + str(i) + ": ")]
    teams.append(team)

for i in range(1, len(teams) + 1):
    team = (random.choice(teams))
    teams.remove(team)
    groups[group_name(i % len(groups) + 1)].append(team)

for key, value in sorted(groups.items()):
    print("{} : {}".format(key, value))

result = open('draw_result.txt', 'w')
for key, value in sorted(groups.items()):
    result.write("{} : {}\n".format(key, value))
result.close()
