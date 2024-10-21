#Marisa Ramautar 
#10/21/24
#period 5 and 6
#create a guessing game that allows the player to guess 
#wheather the guess is too high or low and and prints how 
#many times it took the user to get the number

import random
#Generate a random number between 1 and 10
random_num = random.randint(1,10)

#Initialize attempts = 0
def guess_num(attempt):
    num_guess = int(input("What number do you think it is between 1 and 10?"))
    #increase attempts by one
    attempt += 1
    #Is the guess equal to random number
    if num_guess == random_num:
        print(f"Correct! attempts:{attempt}")
        #Go to the step where the player is told the number
    elif  num_guess > random_num:
        print("Too high! try again.")
        guess_num(attempt)
        #if not 
    else:
        print("Too low")
        guess_num(attempt)

        
guess_num(0)

#Marisa Ramautar 
#10/21/24
#period 5 and 6
#create a guessing game that allows the player to guess 
#wheather the guess is too high or low and and prints how 
#many times it took the user to get the number

import random
#Generate a random number between 1 and 10
random_num = random.randint(1,10)

#Initialize attempts = 0
def rounds():
    round1 = int(input("How many rounds do you want to play?"))
def guess_num(attempt):
    num_guess = int(input("What number do you think it is between 1 and 10?"))
    #increase attempts by one
    attempt += 1
    #Is the guess equal to random number
    if num_guess == random_num:
        print(f"Correct! attempts:{attempt}")
        average = round1/ attempt
        #Go to the step where the player is told the number
    elif  num_guess > random_num:
        print("Too high! try again.")
        guess_num(attempt)
        #if not 
    else:
        print("Too low")
        guess_num(attempt)
    print(average)

rounds()
guess_num(0)
