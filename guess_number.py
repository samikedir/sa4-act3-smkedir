number = 10
print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ")

    if guess.isdigit() and int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    if guess == "q":
        print(f"The right number was {number}! Maybe next time!")
        break    
    else:
        print("Sorry! That's not quite right, try again! (Enter 'q' if you'd like to quit)")


