import random
playing = True
number = str(random.randint(10,20))

print("I will generate the number 10 to 20 ")
print("The game will end when you get 1 hero!")

while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. \n")