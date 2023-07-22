# Project N ° 4 "Develop a software program in Python."

## Presentation

Welcome in my P4 for Openclassrom.

This file will help you for initiate the project


## The Project

### Specifications
Click [here](https://course.oc-static.com/projects/Python+FR/P4+-+D%C3%A9veloppez+un+programme+logiciel+en+utilisant+Python/Spe%CC%81cification+technique_De%CC%81veloppez+un+programme+logiciel+en+Python.pdf) for the specifications
### Environment
First and foremost, you need to create a virtual environment (VENV) using the following command:
:point_down::point_down::point_down:

```
python3.10 -m venv $yourvenvname
```

Then, activate it:

:point_down::point_down::point_down:
```
source $yourvenvname/bin/activate
```

### Requirements
Use the following command to install all the necessary packages for this project:
:point_down::point_down::point_down:

```
pip install -r requirements.txt
```

### Application
To launch the application, use the following command:
:point_down::point_down::point_down:

```
python3 main.py
```

#### Interface

UOnce the application is running, you will have several choices:
- Create a Tournament
- Create a Player
- Play a Tournament
- Generate Reports
You can navigate through the menus using the arrow keys and confirm your selection with the "Enter" key.

:warning: Attention: For player selection in a tournament, to choose a player, use the "Right" arrow key to select the player before confirming your selection with the "Enter" key :warning:

#### Generating Player Pairs

During tournaments, player pairs are generated as follows:
- First round, completely random.
- From the second round onwards, players are sorted by their points, and the first player plays against the second, and so on, unless the two players played against each other in the previous round, in which case player 1 will play against player 3.

#### Data Saving

Player and tournament data are saved in a "json" folder, which contains sub-folders named "player" and "tournament," generated at the program's launch if necessary.

Players are saved in a single .jsonl file.

Each tournament has its own .json file.

#### Reports

The reports are formatted as .txt files stored in a folder named "report"

Here are the different types of reports:

    All players recorded in the database.
    All tournaments.
    All tournaments but only their names and start and end dates.
    The list of players in a tournament.
    The list of rounds in a tournament.

### Flake8

For generate a new flake8 report use the line below : 

:point_down::point_down::point_down:

```
flake8 --exclude=$yourvenvname --format=html --htmldir=flake-report --max-line-length=119
```