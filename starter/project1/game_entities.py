"""CSC111 Project 1: Text Adventure Game - Game Entities

Instructions (READ THIS FIRST!)
===============================

This Python module contains the entity classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2025 CSC111 Teaching Team
"""
from dataclasses import dataclass
from operator import invert
from typing import Optional


@dataclass
class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - id_num: the unique integer assigned for each location
        - brief_description: a shorter introduction of the location, including the current status, connections to other
        locations
        - long_description: a longer introduction of the location, including the current status, connections to other
        loactions
        - items: a str list storing all the items in the location
        - move_index: an integer index to calculate the moves it will take
        - bonus_move_index: an integer index to indicate bonus moves will be given when follow a certain routine
        - visited: bool value indicating if the player has been to the location before

    Representation Invariants:
        - id_num in [1, 2, 3, 4, 5, 6, 12, 51] (these are all the location ids)
    """
    id_num: int
    brief_description: str
    long_description: str
    available_commands: dict[str, int]
    items: list[str]
    move_index: int
    bonus_move_index: int
    visited: bool = False

    # This is just a suggested starter class for Location.
    # You may change/add parameters and the data available for each Location object as you see fit.
    #
    # The only thing you must NOT change is the name of this class: Location.
    # All locations in your game MUST be represented as an instance of this class.

    def __init__(self, location_id, brief_description, long_description, available_commands, items, move_index,
                 bonus_move_index,
                 visited=False) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        self.id_num = location_id
        self.brief_description = brief_description
        self.long_description = long_description
        self.available_commands = available_commands
        self.items = items
        self.move_index = move_index
        self.bonus_move_index = bonus_move_index
        self.visited = visited

    def look(self) -> None:
        """Check the long description of the current location"""
        print(self.long_description)


@dataclass
class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: the string type name of the items
        - description: a short descriptoin of the item
        - start_position: the location id where the item is initialy stored
        - target_position: the location id where the item is targetted to put
        - target_points: the points player will get when the item is accessed

    Representation Invariants:
        - start_position in [1, 2, 3, 4, 5, 6, 12, 51](these are all the location ids)
        - start_position in [1, 2, 3, 4, 5, 6, 12, 51](these are all the location ids)
        - target_points >= 0
    """

    # NOTES:
    # This is just a suggested starter class for Item.
    # You may change these parameters and the data available for each Item object as you see fit.
    # (The current parameters correspond to the example in the handout).
    #
    # The only thing you must NOT change is the name of this class: Item.
    # All item objects in your game MUST be represented as an instance of this class.

    name: str
    description: str
    start_position: Optional[int] = None
    target_position: Optional[int] = None
    target_points: Optional[int] = None

    def __init__(self, name: str, description: str, start_position: Optional[int], target_position: Optional[int],
                 target_points: Optional[int]) -> None:
        """
        Initialize a new item.
        """
        self.name = name
        self.description = description
        self.start_position = start_position
        self.target_position = target_position
        self.target_points = target_points


# Note: Other entities you may want to add, depending on your game plan:
# - Puzzle class to represent special locations (could inherit from Location class if it seems suitable)
# - Player class
# etc.
@dataclass
class Player:
    """A player in our text adventure game world

    Instance Attributes:
        - name: the name of the player, which will be decided by the real player
        - inventory: a list containing all the items the player has equipped
        - score: the score player has earned in the game

    Representation Invariants:
        - score >= 0
    """
    _name: str
    inventory: list[Item]
    score: int
    park_status: bool = False

    def __init__(self, name: str) -> None:
        """
        Initialise the player class
        """
        phone = Item('phone', 'This is your phone -- Nokia 1100', 1, None, None)
        self._name = name
        self.inventory = [phone]
        self.score = 0

    def equip(self, item: Item) -> None:
        """Equip the given item objects into the inventory attribute"""
        self.inventory.append(item)

    def unequip(self, item: Item) -> None:
        """Unequip a selected item"""
        self.inventory.remove(item)

    def check_inventory(self) -> None:
        """Print all the items the player carrying"""
        print([item.name for item in self.inventory])


if __name__ == "__main__":
    pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'disable': ['R1705', 'E9998', 'E9999']
    # })
