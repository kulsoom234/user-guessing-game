# project = 3: Guess the number Game in python project (user)#


import random
print("Guess The Number Between 1 to 100!")

# Generate Random Number #

number =  random.randint(1, 100)

while True:
    guess = int(input("Enter Your Guess Number:"))
    if guess < number :
        print("To Low Number! Try Another")
    elif guess > number :
        print("Too High Number! Try Another") 
    else:
        print("Hurrraaahhhh! You Got It Right!")
        break

