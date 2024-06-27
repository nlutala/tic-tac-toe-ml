# tic-tac-toe-ml
A tic-tac-toe game where the CPU uses machine learning to play the game against you.

## Description
This program was created to help me build on object-oriented programming concepts, automated testing, using directories as well as using the scikit-learn library to introduce me to machine learning concepts.

For this project, I not only implemented a Naive CPU (naive as it makes random decisions on where to place its X), but I also implemented a CPU that uses a decision tree classifier (using the data in assets/ttt_good_moves.txt) to try make informed decisions as to where to move. **It is not perfect, but it does a better job of trying not to lose than the Naive CPU.**

## Getting Started
### Dependencies
Please ensure that you have Python version 3 installed on your computer.

Ypu can find the latest version of Python available using this link: https://www.python.org/downloads/

### Installing
* Open https://github.com/nlutala/tic-tac-toe-ml/ in a new tab.
* Press the green "<> Code" button and press "Download ZIP"
* Once downloaded, extract all files to a new folder
* Open your preferred terminal (command prompt, windows powershell etc.) in the directory where the requirements.txt file is located and write: ``` pip install -r requirements.txt ```
* Now you should the required library (scikit-learn) to run the project

### Executing the program
* To play the game against the Naive CPU, write the following command in the terminal: ``` python play_ttt.py ``` (You will then start and be prompted to enter a number between, and including, 0 and 9 for where you would like to put your O on the grid).
* To play the game against the CPU that uses machine learning, write the following command in the terminal: ``` python play_ttt_ml.py ``` (You will then start and be prompted to enter a number between, and including, 0 and 9 for where you would like to put your O on the grid).

#### Other comments
If you would like to play against the CPU that uses machine learning, you must ensure that the ttt_good_moves.txt data exists in the assets/ folder and that there is data in there that helps the CPU make a decision. If not, you will not be able to play against it.

You can also ignore the create_game_results_ttt.py and the create_ttt_good_moves.py files. But please find a brief description of these files below:

* create_game_results_ttt.py - simulates a game between two naive CPUs and writes the resulting grid and the outcome (W, D or L) to a file in the assets/ directory called game_results_ttt.py.
* create_ttt_good_moves.py - was written to help me go through each of the games the CPU using the X symbol lost and removes some symbols before the loss. The program then prompts me (or whoever executes it) to enter what move should have been made before they lost to help it learn for the next time it plays against a human. **It is not perfect, but it made it easier for me to train the CPU that uses machine learning better than if I was to do this process much more manually.**

I hope you enjoy!

### Author
Nathan Lutala, nlutala

## Version History
* 0.1 - First release

## Acknowledgements
Inspiration for writing this readme file
* https://github.com/nlutala/pdf-merger/ 
