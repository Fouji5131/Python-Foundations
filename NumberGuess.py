import random

random_number = random.randint(1, 10)

user_number = int(input("Guess a number between 1 and 10: "))

while user_number != random_number:
    if user_number < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    user_number = int(input("Guess again: "))

print("🎉 Correct! You guessed the number.")
