"""CSC111 Project 1: Text Adventure Game - Game Manager

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

This file is Copyright (c) 2025 CSC111 Teaching Team
"""
from __future__ import annotations
import json
from typing import Optional
import time

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from game_entities import Location, Item, Player
from proj1_event_logger import Event, EventList


# Note: You may add in other import statements here as needed

# Note: You may add helper functions, classes, etc. below as needed


class AdventureGame:
    """A text adventure game class storing all location, item and map data.

    Instance Attributes:
        - current_location_id: the ID of the location the game is currently in
        - ongoing: the status of whether the game is running
        - moves_left: showing how many moves are left in the current location

    Representation Invariants:
        - # TODO add any appropriate representation invariants as needed
    """

    # Private Instance Attributes (do NOT remove these two attributes):
    #   - _locations: a mapping from location id to Location object.
    #                       This represents all the locations in the game.
    #   - _items: a list of Item objects, representing all items in the game.

    _locations: dict[int, Location]
    _items: list[Item]
    _pic_path: str = ('/Users/yaires/Documents/University Of Toronto/2025 '
                      'Winter/csc111/assignments/starter/project1/Euclid_Pic.png')
    current_location_id: int  # Suggested attribute, can be removed
    moves_left: int = 50
    ongoing: bool  # Suggested attribute, can be removed

    def __init__(self, game_data_file: str, initial_location_id: int) -> None:
        """
        Initialize a new text adventure game, based on the data in the given file, setting starting location of game
        at the given initial location ID.
        (note: you are allowed to modify the format of the file as you see fit)

        Preconditions:
        - game_data_file is the filename of a valid game data JSON file
        """

        # NOTES:
        # You may add parameters/attributes/methods to this class as you see fit.

        # Requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

        # Suggested helper method (you can remove and load these differently if you wish to do so):
        self._locations, self._items = self._load_game_data(game_data_file)

        # Suggested attributes (you can remove and track these differently if you wish to do so):
        self.current_location_id = initial_location_id  # game begins at this location
        self.ongoing = True  # whether the game is ongoing

    @staticmethod
    def _load_game_data(filename: str) -> tuple[dict[int, Location], list[Item]]:
        """Load locations and items from a JSON file with the given filename and
        return a tuple consisting of (1) a dictionary of locations mapping each game location's ID to a Location object,
        and (2) a list of all Item objects."""

        with open(filename, 'r') as f:
            data = json.load(f)  # This loads all the data from the JSON file

        locations = {}
        for loc_data in data['locations']:  # Go through each element associated with the 'locations' key in the file
            location_obj = Location(loc_data['id'], loc_data['brief_description'], loc_data['long_description'],
                                    loc_data['available_commands'], loc_data['items'], loc_data['move_index'],
                                    loc_data['bonus_move_index'])
            locations[loc_data['id']] = location_obj

        items = []
        # TODO: Add Item objects to the items list; your code should be structured similarly to the loop above
        # YOUR CODE BELOW
        for items_data in data['items']:
            item_obj = Item(items_data['name'], items_data['description'], items_data['start_position'],
                            items_data['target_position'], items_data['target_points'])
            items.append(item_obj)

        return locations, items

    def get_location(self, loc_id: Optional[int] = None) -> Location:
        """Return Location object associated with the provided location ID.
        If no ID is provided, return the Location object associated with the current location.
        """

        # TODO: Complete this method as specified
        # YOUR CODE BELOW
        if loc_id is None:
            return self._locations[self.current_location_id]
        else:
            return self._locations[loc_id]

    def undo(self, game_log: EventList) -> None:
        """Undo command in the game."""

    def get_item(self, item_to_get: str):
        """Return the item that has the same name"""
        for i in self._items:
            if i.name == item_to_get:
                return i

    def equip(self, player_f: Player, item_name: str) -> None:
        """Add selected item to player's inventory"""
        item_f = game.get_item(item_name)
        player_f.inventory.append(item_f)
        player_f.score += item_f.target_points
        self.get_location().items.remove(item_name)

    def check_item(self) -> list[str]:
        """Return a list of items in the current location"""
        curr_loc = self.get_location()
        return curr_loc.items

    def move_left(self, prev_id: int) -> None:
        """Return the number of moves left"""
        if result == 3:
            move = (abs(self.get_location(result).move_index - self.get_location(prev_id).move_index) -
                    self.get_location(prev_id).bonus_move_index)
        elif self.current_location_id == 3 and choice in [1, 4, 5]:
            move = (abs(self.get_location(result).move_index - self.get_location(prev_id).move_index) -
                    game.get_location(result).bonus_move_index)
        else:
            move = (abs(self.get_location(result).move_index - self.get_location(prev_id).move_index))
        self.moves_left -= move

    def park_puzzle(self, image_path: str, correct_answer: str) -> int:
        """
        Displays an image puzzle where the user has three attempts to answer correctly.
        - `image_path`: Path to the puzzle question image.
        - `correct_answer`: The correct answer to the puzzle.
        - Returns 1 if solved within three attempts, otherwise 0.
        """

        def check_answer():
            """Check the user's answer and update the result."""
            nonlocal attempts
            user_answer = entry.get().strip().lower()

            if user_answer == correct_answer.lower().strip():
                messagebox.showinfo("Correct!", "You solved the puzzle!")
                self.puzzle_result = 1
                root.destroy()  # Close the GUI properly
            else:
                attempts -= 1
                attempts_label.config(text=f"Attempts Left: {attempts}")

                if attempts == 0:
                    messagebox.showerror("Game Over", "You've used all your attempts!")
                    self.puzzle_result = 0
                    root.destroy()  # Close the GUI properly
                else:
                    messagebox.showwarning("Wrong!", "Try again!")

        # Use `tk.Toplevel()` instead of `tk.Tk()` if another window already exists
        root = tk.Tk() if not hasattr(self, 'main_window') else tk.Toplevel()
        root.title("Puzzle Challenge")
        self.puzzle_result = None  # Reset before each puzzle

        # Load and display image properly
        image = Image.open(image_path)
        image = image.resize((1280, 123))  # Resize if needed
        self.photo_reference = ImageTk.PhotoImage(image)  # Store reference

        # Keep reference to avoid garbage collection
        image_label = tk.Label(root, image=self.photo_reference)
        image_label.image = self.photo_reference  # Attach reference explicitly
        image_label.pack()

        # Instruction Label
        instruction_label = tk.Label(root, text="Enter your answer below:")
        instruction_label.pack()

        # Input Box
        entry = tk.Entry(root)
        entry.pack()

        # Submit Button
        submit_button = tk.Button(root, text="Submit", command=check_answer)
        submit_button.pack()

        # Attempts Left Label
        attempts = 3
        attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}")
        attempts_label.pack()

        # Run GUI event loop inside the function
        root.mainloop()

        # Ensure an integer is always returned
        return self.puzzle_result if self.puzzle_result is not None else 0

    def park_conversation(self, player: Player) -> int:
        """The function for interactions with Park"""
        if player.park_status:
            print("Park has finished his mission, check somewhere else :)\n")
            return 3
        else:
            park1 = {
                0: "Park: Yoooo What's up bro", 'a': "Your mug? Oh wait yeah, I have it in my room...",
                'b': "Wowowow, chill a little, your mug? I think I saw it last time, I think it is in my room...",
                2: "Umm sure...wait but help me with my Eulcid Math Contest Question? It'll be quick, I think you can "
                   "absolutely solve, I heard you are a TA in CS program right?"}
            park2 = {'a': "-Aight aight, thansk a lot bro, here's the probelm...",
                     'b': "-Bruhhh, wait I won't give u the mug unless u help me with that :)))))"}
            options1 = [
                "a) What's up bro, do u know where is my mug?", "b) Where is my muggggg??"
            ]
            answer2 = 'WOOOO can u give it to me?'
            option2 = [
                "a) Sure I'll try my best...", "b) Bruhhhhh just give me that shii..."
            ]
            print(park1[0])
            # =============================
            for option in options1:
                print(option)
            choice1 = input("Enter the option only: ").lower().strip()
            print('\n')
            while choice1 not in ['a', 'b']:
                print("Invalid Choice, pleas try again.")
                choice1 = input("Enter the option only: ").lower().strip()
            time.sleep(1.5)
            print('Park: ', park1[choice1])
            # ==============================
            # time.sleep(1.5)
            print(answer2)
            # time.sleep(1.5)
            print('Park: ', park1[2])
            print('\n')
            # time.sleep(1.5)
            # ==============================
            for option in option2:
                print(option)
            choice2 = input("Enter the option only: ").lower().strip()

            while choice2 not in ['a', 'b']:
                print("Invalid Choice, pleas try again.")
                choice2 = input("Enter the option only: ").lower().strip()

            # time.sleep(0.5)
            print('\n')
            print(park2[choice2])
            print('\n')
            # time.sleep(1.5)
            correct_or_not = self.park_puzzle(self._pic_path, '3')
            while correct_or_not == 0:
                print("HAHA LOSSSSERRRRR you can't even finish the high school question. Try next time. LLLLL\n")
                print("Try again?\n")
                again = input("Enter Y for yes, N for no: ").upper().strip()
                if again == 'Y':
                    correct_or_not = self.park_puzzle(self._pic_path, '3')
                else:
                    correct_or_not = 2
            return correct_or_not


if __name__ == "__main__":

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120,
    #     'disable': ['R1705', 'E9998', 'E9999']
    # })
    LOCATION_INDEX = 10
    INTER_ITEM_INDEX = 20
    INTER_NPC_INDEX = 30
    PUZZLE_INDEX = 40

    game_log = EventList()  # This is REQUIRED as one of the baseline requirements
    game = AdventureGame('game_data.json', 1)  # load data, setting initial location ID to 1
    menu = ["look", "inventory", "score", "undo", "log", "quit"]  # Regular menu options available at each location
    choice = None
    register = False

    # Note: You may modify the code below as needed; the following starter code is just a suggestion
    while game.ongoing:
        # Note: If the loop body is getting too long, you should split the body up into helper functions
        # for better organization. Part of your marks will be based on how well-organized your code is.
        # initialise player variable
        if not register:
            print('Welcome to our word adventure game!\n')
            name = input('Please enter your name: ').strip()
            player = Player(name)
            register = True
            print('Hello! ', name)

        location = game.get_location()

        # TODO: Add new Event to game log to represent current game location
        #  Note that the <choice> variable should be the command which led to this event
        # YOUR CODE HERE
        new_event = Event(location.id_num, location.long_description)
        game_log.add_event(new_event, choice)

        # TODO: Depending on whether or not it's been visited before,
        #  print either full description (first time visit) or brief description (every subsequent visit) of location
        # YOUR CODE HERE
        if location.visited:
            print(location.brief_description)
        else:
            print(location.long_description)
            location.visited = True

        # Display possible actions at this location
        print("Moves Left: ", game.moves_left)
        print("What to do? Choose from: look, inventory, score, undo, log, quit")
        print("At this location, you can also:")
        for action in location.available_commands:
            print("-", action)

        # Validate choice
        choice = input("\nEnter action: ").lower().strip()
        while choice not in location.available_commands and choice not in menu:
            print("That was an invalid option; try again.")
            choice = input("\nEnter action: ").lower().strip()

        print("========")
        print("You decided to:", choice)

        if choice in menu:
            # TODO: Handle each menu command as appropriate
            # Note: For the "undo" command, remember to manipulate the game_log event list to keep it up-to-date
            if choice == "log":
                game_log.display_events()
            # ENTER YOUR CODE BELOW to handle other menu commands (remember to use helper functions as appropriate)
            elif choice == 'look':
                print(location.long_description)
                print('========')
            elif choice == 'inventory':
                print('Your have ', [items.name for items in player.inventory])
            elif choice == 'score':
                print("Your current score is: ", player.score)
                print("========")
            elif choice == 'undo':
                if game_log.__len__() > 1:
                    game_log.remove_last_event()
                    location = game_log.last
                    game.current_location_id = location.id_num
                    print("Last Even has been removed")
                    print("========\n")
                else:
                    print("Can't undo. This is your starting location.")
                    print("========\n")
            elif choice == 'quit':
                print('Thank you for playing!! C U next time!!')
                exit()

        else:
            # Handle non-menu actions
            result = location.available_commands[choice]

            # TODO: Add in code to deal with actions which do not change the location (e.g. taking or using an item)
            # TODO: Add in code to deal with special locations (e.g. puzzles) as needed for your game
            if result <= 10:
                prev_loc_id = game.current_location_id
                game.current_location_id = result
                game.move_left(prev_loc_id)

            elif result <= 20:
                if result == 11:
                    get_mug = game.park_conversation(player)
                    if get_mug == 1:
                        game.equip(player, 'lucky mug')
                        player.park_status = True
                        print("Smart!! Park appreciated you and gave you your precoius lucky mug!! (ﾉ◕ヮ◕)ﾉ:･ﾟ✧*\n")
                    elif get_mug == 0:
                        print("HAHA LOSSSSERRRRR you can't even finish the high school question. Try next time. LLLLL")
                    elif get_mug == 2:
                        print(get_mug)
                        print("You thought you weren't in a good mood to answer the question. You want to have a good "
                              "rest and then try again later...\n")
            elif result <= 30:
                if result < 33:
                    print(game.check_item())


