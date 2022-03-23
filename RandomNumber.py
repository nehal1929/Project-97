import random
number=random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Enter a number:")) 
    if guess == number:
        print("Congratulations You Won!")
        break
    elif guess< number:
        print("Your guess was too low:Guess a higher number than",guess)
    else:
        print("Your guess was too high:Guess a number lower than",guess)
        chances += 1
