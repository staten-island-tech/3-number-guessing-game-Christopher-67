import random
random_number = random.randint(1, 100)

solved = False
guess_history = []

while solved == False:
       guess = input("Enter a number between 1 and 100:")
       guess_history.append(int(guess))
       if int(guess) ==random_number:
         print("You got the right number")
         solved = True
       elif int(guess) < random_number:
         print("Guess too low")
       else:
        print("Guess too high")

print("everything you guessed:", guess_history)
