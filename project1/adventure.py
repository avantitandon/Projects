"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Player, Riddle, Phone

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(2, 2)  # set starting location of player; you may change the x, y coordinates here as appropriate
    print("Welcome to a text adventure game! \n")

    # part of new code sandwich
    r = Riddle('Evil Waterloo CS Professor', 15, riddles_questions={
        0: 'If you multiply this number by any other number, the answer will always be the same. What number is this?',
        1: 'I am an odd number. Take away a letter and I become even. What number am I?',
        2: 'Pronounced as 1 letter, '
           'And written with 3, 2 letters there are, and 2 only in me. '
           'I’m double, I’m single, I’m black blue, and gray, I’m read from both ends, '
           'and the same either way. What am I?',
        3: 'Pauls height is six feet, '
           'he is an assistant at a butchers shop, and wears size 9 shoes. What does he weigh?',
        4: 'What can go through glass without breaking it?',
        5: 'What is always on its way but never arrives?',
        6: 'What do you buy to eat but never consume?',
        7: 'Rachel goes to the supermarket and buys 10 tomatoes. Unfortunately, '
           'on the way back home, all but 9 get ruined. How many tomatoes are left in a good condition?'},
        riddle_answers=['0', '7', 'Eye', 'Meat', 'Light', 'Tomorrow', 'Cutlery', '9'])
    phone = Phone('Phone', 10, 110111)

    menu = ["look", "inventory", "score", "quit", "moves", "back", "drop item"]
    visited_before = []
    moves = 46  # first spawning at Robarts counts for this

    for loc in w.location_lst:
        for item in w.item_dict:
            if loc.location_value == item.start_position:  # code to set every item to a location. Resets every game
                loc.item = item

    while not p.victory and moves > 0:
        moves -= 1  # A move is counted for every while loop iteration. Moves are also counted for menu.
        location = w.get_location(p.x, p.y)

        if (location is not None and location.location_value not in [None, 1] and visited_before.count(
                location.location_value) >= 5):  # for when player goes to the same location 5+ times
            w.mutate_map(location.location_value)

        if location is not None:
            print(location.location_name)
            if location.location_value not in visited_before:
                print(location.large_description)

            else:
                print(location.small_description)
            visited_before.append(location.location_value)  # keeps track of location
            # Depending on whether or not it's been visited before,
            # print either full description (first time visit) or brief description (every subsequent visit)
            if location.item is not None:

                print('Oh! look at that, there is an item here. Do you want to pick it up? (yes/no)')
                c = input(':')  # for when item is available.
                if c.lower() == 'yes':
                    p.inventory.add(location.item)
                    if location.item.name == 'Phone':  # items with extra abilities
                        menu.append('Phone')
                    elif location.item.name == 'ScrapPaper':  # items with extra abilities
                        print('hm, this looks like an old note to yourself')
                        print('"I took CSC(110) and now I am in CSC(111)"')
                    print(f"You just picked up your {location.item.name}")
                    location.item = None
            print("What to do? \n")
            print('Available actions:')
            # print("[menu]")

            for action in location.available_actions():
                print(action, end="|")

            choice = input("\nEnter action: ")

            if choice == "menu":
                print("Menu Options: \n")
                for option in menu:
                    print(option, end="|")
                choice = input("\nChoose action: ")
                if choice.lower() == "look":
                    print(location.large_description)
                elif choice.lower() == 'inventory':
                    print([item1.name for item1 in p.inventory])
                elif choice.lower() == 'moves':
                    print('moves:', moves)
                    # New code sanwich
                elif 'Phone' in menu and choice == 'Phone':
                    enter = input(
                        'Warning you only have one try to enter your *6* digit password. '
                        'Do you wish to take it?(Yes/No)')
                    if enter.lower() != 'yes':
                        continue
                    else:
                        password = int(input(phone.speak(phone.character_name)))
                        if phone.passwordcheck(password):
                            d = input('YOU HAVE UBER INSTALLED ON YOUR PHONE! Take an Uber?(Yes/No)')
                            if d.lower() == 'yes':
                                p.x, p.y = 0, 4
                            else:
                                continue
                        else:
                            print('Incorrect password. Your phone is locked.')
                            menu.remove('Phone')

                    # New code sandwich

                elif choice.lower() == 'drop item':
                    c = input('What item do you want to drop?')
                    new = list(p.inventory)
                    for things in new:
                        if c == things.name:
                            p.inventory.remove(things)
                            location.item = things

                elif choice.lower() == 'score':
                    print(sum([things1.target_points for things1 in p.inventory]))

                elif choice == "quit":
                    print('Game over')
                    break
                else:
                    print('No valid choice selected.')
                    continue

            elif choice == 'north':  # direction choices
                p.move_north()
            elif choice == 'east':
                p.move_east()
            elif choice == "west":
                p.move_west()
            elif choice == "south":
                p.move_south()
            else:
                print('No valid choice selected.')
                continue

        else:
            print('This way is blocked')  # when location on map is -1, we give the player a choice to go back.
            c = input('Go back?:')
            if c.lower() == 'yes':
                x, y = w.get_coordinates(visited_before[-1])
                # print('x',x,'y',y)
                if x != -1 and y != -1:
                    p.y, p.x = y, x
                else:
                    print(
                        'You visited the same locations too many times, '
                        'got tired and passed out. Someone found you and took you back to Robarts')
                    p.y, p.x = 2, 2

        # new code sandwich
        if p.x == 0 and p.y == 3:  # Our randomly generated riddle
            print(
                'Oh No! You meet an evil Waterloo CS professor who is BLOCKING your way. '
                'You have to answer his Riddle to pass or you lose.')
            riddle_func = r.speak(r.character_name)
            riddle = riddle_func[0]
            answer = riddle_func[1]
            print(riddle)
            choice = input('Your answer: ')
            count = 0
            while count < 2:
                if choice.lower() != r.riddle_answers[answer].lower():
                    count += 1
                    choice = input('Try again: ')
                else:
                    count = 2
            if choice.lower() == r.riddle_answers[answer].lower():
                print('You are correct! Go ahead my child.')
                continue
            else:
                print('You lose!')
                break
        # new code sandwich
        if p.x < 0 or p.x > 4 or p.y < 0 or p.x > 4:
            print('You went out of the grid! Sending you back.')
            x, y = w.get_coordinates(visited_before[-1])
            if x != -1 and y != -1:
                p.y, p.x = y, x
        # new code sandwich

        if p.x == 0 and p.y == 4:
            if p.inventory == set(w.item_dict):
                p.victory = True
                print('Congrats! You won! Since you had all your items you managed to finish your exam and get a A+')
            elif p.inventory != set(w.item_dict):
                print(
                    'You made it to the exam centre on time but did not have your items. '
                    'You failed your exam. Try again next semester!')

            break

    if moves == 0:
        print('You ran out of moves! The exam got over and all your friends passed. Try again next semester!')
    # We have provided the following code to run any doctest examples that you add.
    # (We have not provided any doctest examples in the starter code, but encourage you
    # to add your own.)
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['hashlib']
    })
