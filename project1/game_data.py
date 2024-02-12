"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO, Any
import random


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: is name of item
        - start: starting position of item
        - target: where item needs to be taken
        - target_points: how many points you get for picking up the item


    Representation Invariants:
        - self.name != ''
        - -1 <= self.start_position <= 17

    >>> item = Item("Sword", 1, 5, 10)
    >>> item.name
    'Sword'
    >>> item.start_position
    1
    >>> item.target_position
    5
    >>> item.target_points
    10
    """
    name: str
    start_position: int
    target_position: int
    target_points: int

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """
        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - location_name: The name of the location
        - location_value: Integer on the map that refers to the location
        - small_description: Short description when player visits a location that they have already visited
        - long_description: Long description that is printed when the player visits a new location.

    Representation Invariants:
        - len(self.location_coord)=2
    >>> location = Location("Garden", 1, "A dense garden.", "You find yourself in a dense garden.")
    >>> location.location_name
    'Garden'
    >>> location.location_value
    1
    >>> location.small_description
    'A dense garden.'
    >>> location.large_description
    'You find yourself in a dense garden.'
    """

    # location_coord: list[int]
    location_name: str
    location_value: int
    small_description: str
    large_description: str

    item: Optional[Item]

    def __init__(self, location_name: str, location_value: int, small_description: str, large_description: str) -> None:
        """Initialize a new location.

        """
        # self.location_coord = location_coord
        self.location_name = location_name
        self.location_value = location_value
        self.small_description = small_description
        self.large_description = large_description
        self.item = None
        # location_coord: Optional[list[int]]
        # items: list[Item]

    def give_short_description(self) -> str:
        """ Returns short description"""

        return self.small_description

    def give_long_description(self) -> str:
        """ Returns long description"""
        return self.large_description

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

    def available_actions(self) -> list:
        """Gives a list of available actions
        >>> location = Location("Northern Area", 5, "You see a path to the north and south.", "You are in a northern area.")
        >>> location.available_actions()
        ['menu', 'north', 'south', 'west']
        """
        available_actions = ['menu']
        if self.location_value == -1:
            available_actions.append('This area is blocked! Go back!')
        elif self.location_value == 16:
            available_actions.append('north')
            available_actions.append('east')
        elif self.location_value in [13, 14, 15]:
            available_actions.append('north')
            available_actions.append('south')
            available_actions.append('east')
        elif self.location_value in [9, 10, 11]:
            available_actions.append('south')
            available_actions.append('east')
            available_actions.append('west')
        elif self.location_value in [5, 7]:
            available_actions.append('north')
            available_actions.append('south')
            available_actions.append('west')
        else:
            available_actions.append('north')
            available_actions.append('south')
            available_actions.append('east')
            available_actions.append('west')
        return available_actions
    # #
    #     # NOTE: This is just a suggested method
    #     # i.e. You may remove/modify/rename this as you like, and complete the
    #     # function header (e.g. add in parameters, complete the type contract) as needed
    #


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: x-coordinate of the player
        - y: y-coordinate of the player
        - invenstory: set storing all of the items the player has
        - victory: bool checking the players victory status

    """
    x: int
    y: int
    inventory: set
    victory: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = set()
        self.victory = False

    def move_west(self) -> None:
        """  Moves the player west
        >>> player = Player(3, 3)
        >>> player.move_west()
        >>> player.x
        2
        """
        self.x -= 1

    def move_east(self) -> None:
        """  Moves the player east
        >>> player = Player(3, 3)
        >>> player.move_east()
        >>> player.x
        4
        """
        self.x += 1

    def move_south(self) -> None:
        """  Moves the player south
        >>> player = Player(3, 3)
        >>> player.move_south()
        >>> player.y
        4
        """
        self.y += 1

    def move_north(self) -> None:
        """  Moves the player north
        >>> player = Player(3, 3)
        >>> player.move_north()
        >>> player.y
        2
        """
        self.y -= 1

    def pick_up(self, item: Item) -> None:
        """ Allows player to pick up item"""
        if len(self.inventory) <= 5:
            self.inventory.add(item)

    def drop_item(self, item: Item) -> None:
        """ Allows player to drop item"""
        if item in self.inventory:
            self.inventory.remove(item)


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - location_dict: a dictionary containing different details of the location
        - item_dict: a dictionary containing info about the item

    Representation Invariants:
        - Map cannot be empty
        - Location list cannot be empty
        - Item dicionary cannot be empty
    """
    map: list[list[int]]
    location_lst: list[Location]
    item_dict: set[Item]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.location_lst = self.load_location(location_data)
        self.item_dict = self.load_items(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """

        read = map_data.readlines()
        return make_list(read)

    def load_location(self, location_data: TextIO) -> list[Location]:
        """
        loads the location of the file
        """

        list1 = []
        line1 = location_data.readlines()
        # for i in range(len(line1)):
        #     c = line1[i].strip().split(' $ ')
        #     location_acc = Location(location_name=c[0], location_value=int(c[1]), small_description=c[2],
        #                             large_description=c[3])
        #     list1.append(location_acc)
        # return list1
        for i in line1:
            c = i.strip().split(' $ ')
            location_acc = Location(location_name=c[0], location_value=int(c[1]), small_description=c[2],
                                    large_description=c[3])
            list1.append(location_acc)
        return list1

    def load_items(self, item_data: TextIO) -> set[Item]:
        """loads the item"""
        set1 = set()
        line2 = item_data.readlines()
        for i in line2:
            c = i.strip().split(' ')
            item_acc = Item(str(c[0]), int(c[1]), int(c[2]), int(c[3]))
            set1.add(item_acc)
        return set1

    def mutate_map(self, location_value: int) -> None:
        """ Changes the map"""
        for i in range(len(self.map)):
            for y in range(len(self.map[i])):
                if self.map[i][y] == location_value:
                    self.map[i][y] = -1

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        map1 = self.map
        val = map1[y][x]
        for loc in self.location_lst:
            if val == loc.location_value and val > 0:
                return loc
        return None

    def get_coordinates(self, loc_value: int) -> tuple[int, int]:
        """ Takes location value as input and changes the file"""
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y] == loc_value:
                    return y, x
        return -1, -1


def make_list(read_data: Any) -> list[list[int]]:
    """ makes a list
    """
    k = []
    for i in read_data:
        k2 = []
        kn = i.strip().split(' ')
        for num in kn:
            k2.append(int(num))
        k.append(k2)
    return k


class Dialouge:
    """Enchancement: Abstract Class that stores dialouge of a character at a specific location.
    """

    def speak(self, character: str) -> Any:
        """Speaking method for the Dialouge class. Used for
        the character to speak at that location."""
        raise NotImplementedError


class Riddle(Dialouge):
    """Enhancement : Riddles
       Instance Attributes:
    - character_name: The name of the character.
    - character_location: The location of the character.
    - dialouge: The dialouge of that character at that location.
     """
    character_name: str
    character_location: int
    riddles_questions: dict[int:str]
    riddle_answers: list[str]

    def __init__(self, character_name: str, character_location: int, riddles_questions: dict[int:str],
                 riddle_answers: list[str]) -> None:
        self.riddles_questions = riddles_questions
        self.character_name = character_name
        self.character_location = character_location
        self.riddle_answers = riddle_answers

    def speak(self, character: str) -> tuple:
        num = random.randint(0, 7)
        ridde_retured = self.riddles_questions[num]
        return character + ': ' + ridde_retured, num


class Phone(Dialouge):
    """Enchancement: Phone"""
    character_name: str
    character_location: int
    password: int

    def __init__(self, character_name: str, character_location: int, password: int) -> None:
        self.character_name = character_name
        self.character_location = character_location
        self.password = password

    def speak(self, character: str) -> str:
        " Returns the dialogue"
        return character + ': ' + 'Enter your password.'

    def passwordcheck(self, user_input: int) -> bool:
        "Checks the password"
        return user_input == self.password


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run both pytest and PythonTA,
    # and then also test your methods manually in the console.
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120
    })
