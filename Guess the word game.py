import random
tries = 0

print("Guess a name from: Alex, Cheng, Harry, Sid, JP")

WORDS = ("Alex", "Cheng", "Harry", "Sid","JP")
word = random.choice(WORDS)

correct = word
length = len(word)
length = str(length)

guess = raw_input("The word is " + length + " letters long. Guess a letter!:")

if guess == correct:
    print("Congrats!")
elif guess != correct:
    print("smh")

while guess!=correct:
    another = raw_input("Try again ")
    if another == correct:
        print("Congrats!")
