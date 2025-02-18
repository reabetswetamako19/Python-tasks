import random
import time
print("Hi! welcome to the guessing game. i am going to pick a number between 1 and 100.")
time.sleep(3)
print("picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
       guess = int(input("Wrong. you need to guess higher.What is your guess?: "))
    else:
        guess = int(input("Wrong. you need to guess lower.What is your guess?: "))

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")

