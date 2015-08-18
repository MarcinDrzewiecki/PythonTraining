__author__ = 'drzewko'

pull = 30

attributes = {"strength": 0,
              "dexterity": 0,
              "wisdom": 0,
              "vitality": 0}

while pull > 0:
    player_choose = raw_input("""
You have """ + str(pull) + """ points left to spare on your statistic to make the greatest hero ever!
Choose one of the following:\n
1 - Add strength to your character
2 - Add dexterity to your character
3 - Add wisdom to your character
4 - Add vitality to your character
5 - Remove points from attribute and add it to the pull\n\n
What is your choice? \n""")

    if player_choose == "1":
        strength = int(raw_input("How many points are you adding to strength ?\n"))
        if strength > pull:
            raw_input("Don't be too greedy! Press ENTER to continue...")
        else:
            attributes["strength"] += strength
            pull -= strength
            print("Your attributes are looking like that: ", attributes)
    elif player_choose == "2":
        dexterity = int(raw_input("How many points are you adding to dexterity ?\n"))
        if dexterity > pull:
            raw_input("Don't be too greedy! Press ENTER to continue...")
        else:
            attributes["dexterity"] += dexterity
            pull -= dexterity
            print("Your attributes are looking like that: ", attributes)
    elif player_choose == "3":
        wisdom = int(raw_input("How many points are you adding to wisdom ?\n"))
        if wisdom > pull:
            raw_input("Don't be too greedy! Press ENTER to continue...")
        else:
            attributes["wisdom"] += wisdom
            pull -= wisdom
            print("Your attributes are looking like that: ", attributes)
    elif player_choose == "4":
        vitality = int(raw_input("How many points are you adding to vitality ?\n"))
        if vitality > pull:
            raw_input("Don't be too greedy! Press ENTER to continue...")
        else:
            attributes["vitality"] += vitality
            pull -= vitality
            print("Your attributes are looking like that: ", attributes)
    elif player_choose == "5":
        choose_statistic = raw_input("From what statistic do you want to remove points ?\n")
        if choose_statistic in attributes:
            remove_points = int(raw_input("How many points do you want to remove ?\n"))
            attributes[choose_statistic] -= remove_points
            pull += remove_points
            print("Your attributes are looking like that: ", attributes)
        else:
            raw_input("No statistic with the name " + choose_statistic + "! Press ENTER and try again...")
    else:
        raw_input("Wrong option, press ENTER to try again")
print("You have successfully created your hero! Congratulations!")
