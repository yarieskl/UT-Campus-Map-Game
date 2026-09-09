# Campus Quest

A command-line adventure game set around the University of Toronto campus. Players explore familiar locations, manage a limited move budget, collect essential items, interact with characters, and solve a puzzle to recover everything needed to complete their project.

> **Team project:** Built by Keliu Yang and Junho Yoon for CSC111 at the University of Toronto.

## Highlights

- Navigate a data-driven map of U of T locations
- Collect, inspect, equip, and drop inventory items
- Earn points by finding useful items
- Track remaining moves and plan efficient routes
- Review an event log or undo the previous action
- Interact with an NPC through branching dialogue
- Complete a graphical puzzle challenge built with Tkinter and Pillow
- Simulate playthroughs with a linked event-log structure

## Tech Stack

- **Language:** Python
- **Interface:** Command line, with a Tkinter puzzle window
- **Data:** JSON-based locations, commands, and items
- **Concepts:** Object-oriented programming, data classes, linked structures, state snapshots, input validation, and event simulation

## How It Works

The game loads its world from `game_data.json`. Each location defines its description, available commands, items, and movement cost. `AdventureGame` coordinates navigation and game state, while the `Location`, `Item`, and `Player` classes model the core entities. An event logger records the player's journey, and saved state snapshots support the undo feature.

The objective is to explore campus, recover the required project supplies, and return to the player's room before running out of moves.

## Project Structure

```text
starter/
├── ex1/                         # Event-logging exercise
└── project1/
    ├── adventure.py             # Main game loop and game manager
    ├── game_data.json           # Locations, routes, and item data
    ├── game_entities.py         # Location, Item, and Player models
    ├── proj1_event_logger.py     # Linked event-log implementation
    ├── proj1_simulation.py       # Scripted playthrough simulation
    └── report.tex                # Course report template
```

## Running Locally

This archived course project currently requires a small portability fix before it can run on another computer: the puzzle image path in `adventure.py` points to a local file that is not included in the repository.

After replacing that path with an available image, install Pillow and launch the game from the project directory:

```bash
python -m pip install Pillow
cd starter/project1
python adventure.py
```

Follow the available commands printed at each location. General commands include `look`, `inventory`, `score`, `undo`, `log`, and `quit`.

## Contributors

- [Keliu Yang](https://github.com/yarieskl)
- [Junho Yoon](https://github.com/6hoyoon)

## Attribution and Academic Use

This repository contains work created collaboratively for CSC111 at the University of Toronto and includes course-provided starter material. It is presented as a team project, and authorship should be understood from the original Git history.

Before making this repository public, confirm that publication complies with the course's copyright and academic-integrity requirements. Current source-file notices state that distribution of the starter material is prohibited.
