# Problem Statement
The goal is to create an engaging and accessible basic computing application that effectively demonstrates core programming concepts, specifically control flow, function design, and user input validation. Many new programmers struggle with structuring interactive command-line applications that handle different scenarios (winning, losing, invalid input). The Number Guessing Game provides a clear, contained environment to solve these challenges by requiring the system to randomly generate a secret value and guide the user to the answer under specific constraints.


# Scope of the Project
The project is focused on a pure Python 3 implementation running exclusively in the command-line interface (CLI).

In Scope: Implementing the core game logic, including number generation, difficulty selection, guess comparison, attempt tracking, and robust numeric input validation.

Out of Scope: Graphical User Interfaces (GUIs), persistence (saving high scores or game state to a file/database), network functionality, or integration with external APIs.

# Target Users
The primary target users for this application are:

Students/Beginners: Individuals learning basic programming concepts (Python functions, loops, and conditional statements) who want a simple, interactive program to review.

Casual Users: Anyone looking for a quick, simple game to play directly in their terminal without needing additional software installation.


Evaluators: Academic staff reviewing the project's ability to meet functional and technical requirements for application development.

# High-Level Features

Selectable Difficulty Levels: User can choose between Easy, Medium, and Hard modes, which dynamically set the guessing range and the number of allowed attempts.


Interactive Gameplay Loop: The game continuously prompts the user for a guess until the correct number is found or attempts are exhausted.

Real-Time Feedback: Provides immediate directional clues ("Too low" or "Too high") after each guess to facilitate the user's progress.


Robust Input Handling: The system validates that the user's input is a valid integer before processing it.
