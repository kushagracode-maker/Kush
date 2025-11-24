import random

def choose_level():
    print("Choose a level:")
    print("1.Easy (1–20, 5 attempts)")
    print("2.Medium (1–50, 7 attempts)")
    print("3.Hard (1–100, 5 attempts)")

    while True:
        level = input("Enter level number:")
        if level in ("1","2","3"):
            return int(level)
        print("Try again.")

def guess_game():
    level = choose_level()

    if level == 1:
        number = random.randint(1,20)
        attempts_allowed =5
    elif level ==2:
        number = random.randint(1,50)
        attempts_allowed =7
    else:
        number = random.randint(1,100)
        attempts_allowed =5

    attempts = 0
    print("Start guessing!")

    while True:
        guess = input("Your guess:")

        if not guess.isdigit():
            print("Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if attempts > attempts_allowed:
            print("Game over.")
            print(f"The number was {number}.")
            break

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_game()