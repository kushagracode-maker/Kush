# VITYARTHI PROJECT 
# KUSHAGRA MISHRA
# 25BAI10650
# Project Title

# Number Guessing Game: A Python Implementation 

# Overview of the Project
This project is a classic command-line-based Number Guessing Game implemented in Python. It allows users to test their intuition by guessing a secret number within a specified range and a limited number of attempts. The game features three distinct difficulty levels (Easy, Medium, Hard), each with a unique number range and attempt count, to provide a varied challenge. This implementation demonstrates the application of core Python programming concepts, including functions, control flow (if/elif/else), and input validation.

# Features
The game includes the following specific features and functional requirements:

Three Difficulty Levels:

Easy: Range 1-20, 5 attempts.

Medium: Range 1-50, 7 attempts.

Hard: Range 1-100, 5 attempts.


Clear Input/Output: Provides clear prompts for level selection and guessing, and immediate feedback ("Too low," "Too high") after each guess.


Attempt Counter: Tracks the number of guesses remaining and ends the game when attempts are exhausted.


Input Validation: Ensures the user enters valid numeric input when guessing, avoiding program crashes.

Winning/Losing: Clearly announces whether the user won and in how many attempts, or reveals the secret number upon losing.

# Technologies/Tools Used

Language: Python 3.x 



Module: random (for number generation) 



Version Control: Git & GitHub

# Steps to Install & Run the Project



Ensure Python is Installed: Verify you have Python 3.x installed on your system.

Run the Game: Execute the main script from your terminal:

Bash

python guess_game.py

Follow the Prompts: The game will first prompt you to select a difficulty level (1, 2, or 3), and then you can begin guessing.

# Instructions for Testing
Basic testing can be performed manually by running the game and verifying the following functionality:

Level Selection: Ensure choosing '1', '2', or '3' correctly sets the range and attempts (e.g., Level 3 should generate a number between 1 and 100 and allow 5 guesses).

Feedback Mechanism: Verify that the game correctly provides "Too low," "Too high," and the winning message when applicable.

Loss Condition: Confirm the game ends and reveals the number when the maximum number of attempts is reached.


Input Handling: Test that entering non-numeric characters (e.g., 'a', 'hello') results in the "Enter a valid number" error message and does not consume an attempt

# SCREENSHOTS

<img width="880" height="583" alt="image" src="https://github.com/user-attachments/assets/18645a10-985b-4e3f-86fa-c424458dd488" />

<img width="883" height="612" alt="image" src="https://github.com/user-attachments/assets/728772dc-e020-44fb-9c19-f5815adcf16e" />

<img width="879" height="513" alt="image" src="https://github.com/user-attachments/assets/31d8b8d2-5c01-4ced-a1a4-77c2e305f542" />



