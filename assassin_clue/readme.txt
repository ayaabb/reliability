Assassin clue game:
The purpose of the game is to simulate a murder mystery scenario where the user player must deduce the identity of the murderer among the players.
Players move through different locations each round, and the user make accusations to uncover the truth and identify the murderer .


To run this project:
use terminal specified to the path of the project file named "assassin_clue" (use: cd path_of_the_project)
Then run "python __main__.py"


Maintainability:
I added a docstring file in the project describing the class game functions.


Reliability:
I added tests for class Game using unit test lib
To run the test run 'python -m unittest' in terminal


Description of some points of failure and how I handled it in Class Game :

suspect_2_players method:
Points of failure:
1-Out-of-Range Input
2-Duplicate Player Selection
3-Inputting non-numeric characters
Handling errors and input validation:
The function begins by displaying the available range of numbers representing the alive players, aiding the user in making selections.
It ensures the user provides valid input by continuously prompting them until correct choices are made, preventing the program from proceeding with invalid input.
Implemented try-except blocks catch potential errors during input conversion and range validation.
Informative error messages are provided to guide the user in correcting input mistakes, enhancing user experience.

accuse_player method:
Points of failure:
1-Inputting non-numeric characters
2-Out-of-Range Input
Handling errors and input validation:
Utilizes a while loop to continuously prompt the user until a valid choice (1 or 2) is made, ensuring correct input.
Implemented a try-except block to catch potential ValueError exceptions, providing informative error messages for incorrect input.


murder method:
Points of failure:
1-No players in murderer's last visited Places
Handling errors:
This failure indicates that the murder cannot be performed because there are no potential victims present in the murder location.
This situation is handled by raising a NoPlayersInMurderPlaceError exception
('NoPlayersInMurdererPlacesError' class is a custom exception that inherits from the built-in ValueError class.
It is raised when there are no players present in any of the places visited by the murderer)


play_round method:
Points of failure:
1-murder method raises exception NoPlayersInMurderPlaceError and there is no murder
Handling errors:
It catches NoPlayersInMurdererPlacesError exception raised by the murder method when there are no players in the murderer's last visited places.
If no murder occurred, it returns "no murder".
It returns a status message of  the game like 'game over' ,'no murder' ,'end' and 'continue'.