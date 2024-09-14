number = 10
print("I'm thinking of a number...")
tries = 3
while tries >= 0:
    guess = input("What number am I thinking of? ")
    
    if guess.isdigit() and int(guess) > number:
        tries -= 1
        if tries > 1:
            print(f"Too high.. {tries} more tries! (Enter 'q' if you'd like to quit)")
        else:
            print(f"Too high.. {tries} more try! (Enter 'q' if you'd like to quit)")
    if guess.isdigit() and int(guess) < number:
        tries -= 1
        if tries > 1:    
            print(f"Too low.. {tries} more tries! (Enter 'q' if you'd like to quit)")
        else:    
            print(f"Too low.. {tries} more try! (Enter 'q' if you'd like to quit)")

    if guess.isdigit() and int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    if guess == "q":
        print(f"The right number was {number}! Maybe next time!")
        break    
    if tries == 0:
        print(f"Out of tries! The right number was {number}.")