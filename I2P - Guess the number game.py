import random
number=random.randint(1,50)
print("Guess a numbe fomr 1-50")

while True:
    guess=int(input("Guess:"))
    if guess>number:
        print("lower")
        print(guess/number)
    elif guess<number:
        print("higher")
    elif guess==number:
        print("correct")
