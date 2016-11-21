vclass = input("Fighter or Mage")

if vclass=="Fighter":
        print("You are now a Fighter!")
if vclass=="Mage":
        print("You are now a Mage!")

print("Your first quest is to find and defeat the Donald Trump")

def fight(int1,int2):
    if vclass=="Fighter":
        vHP=int1
    if vclass=="Mage":
        vHP=int2

    vplace = input("Do you want to go north,south,east, or west?")
    if vplace == "west":
        print("Donald Trump appeared!")
    while vplace != "west":
        print("There is nothing here...")
        vplace=input("Do you want to go north,south,east, or west?")
        if vplace=="west":
            print("Donald Trump appeared!")

    vTrumpHP=50

    vmove=input("Do you want to run or fight?")
    if vmove=="run":
        vHP=vHP-5
        print("you run away")
        fight(50,100)

    if vmove=="fight":
        import random
        number=random.randint(1,10)
        print("Guess a number from 1-10 to attack")

        while True and vTrumpHP!=0:
            if vTrumpHP!=0:
                guess=int(input("Guess:"))
            if guess>number:
                print("Your number is too high")
                print("You lose 5 hp")
                vHP=vHP-5
                print("your current HP is",vHP)
                if vHP==0:
                    print("You lost")
                    print("Going back to village")
                    fight()

            elif guess<number:
                print("Your number is too low")
                print("You lose 5 hp")
                vHP=vHP-5
                print("your current HP is",vHP)
                if vHP==0:
                    print("You lost")
                    print("Going back to village")
                    fight()

            elif guess==number:
                print("You successfully attacked")
                if vclass=="Mage":
                    vdamage=20
                if vclass=="Fighter":
                    vdamage=10
                print("Trump took 10 damage")
                vTrumpHP=vTrumpHP-vdamage
                print("Trump has",vTrumpHP,"HP left")
        if vTrumpHP<0:
            print("You beat Trump!")
        if vTrumpHP==0:
            print("You beat Trump")

fight(50,100)
if vclass=="Mage":
    vitem1="Robe"
    vHP=100
if vclass=="Fighter":
    vitem1="Armour"
    vHP=150

print ("You go back to the village and receive ",vitem1)
print ("Your max HP increaesd by 50")
print("Your max HP is now",vHP)

print("Actually, Trump didn't die yet, he only faked his death. Your going to have to go and fight him again.")

fight(100,150)
print("You are half way there to saving America")
print("Now you have to go kill Clinton")

vplace = input("Do you want to go north,south,east, or west?")
if vplace == "west":
    print("Donald Trump appeared!")
while vplace != "north":
    print("There is nothing here...")
    vplace=input("Do you want to go north,south,east, or west?")
    if vplace=="north":
            print("Hillary Clinton appeared!")
            print("But she is surrounded by bodyguards and u die")
            print("GAME OVER")

