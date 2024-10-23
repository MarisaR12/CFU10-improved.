import random
import time

def difficulty():
    difficulty = int(input("What's the difficulty you want to do? (1, 2, 3): "))
    if difficulty == 1:
        return random.randint(1, 10)
    elif difficulty == 2:
        return random.randint(1, 50)
    else:
        return random.randint(1, 1000)

def guess_num(attempt, max_number):
    start_time = time.time()  
    num_guess = int(input("What number do you think it is? "))
    attempt += 1  

    if num_guess == max_number:
        end_time = time.time()  
        total_time = end_time - start_time
        print(f"Correct! Attempts: {attempt}. Total time: {total_time:.2f} seconds.")
        return attempt, total_time  
    elif num_guess > max_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

   
    return guess_num(attempt, max_number)  

def rounds(rounds_left, total_attempts, total_time):
    if rounds_left <= 0:
        return total_attempts, total_time  
   
    max_number = difficulty()  
    attempts, round_time = guess_num(0, max_number)  
    return rounds(rounds_left - 1, total_attempts + attempts, total_time + round_time)  


rounds_left = int(input("How many rounds do you want to play? "))
if rounds_left > 0:
    total_attempts, total_time = rounds(rounds_left, 0, 0)  
    average_attempts = total_attempts / rounds_left  
    average_time = total_time / rounds_left  

    print(f"Average attempts per round: {average_attempts:.2f}")
    print(f"Average time per round: {average_time:.2f} seconds")
else:
    print("No rounds played.")
