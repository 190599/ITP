#if else
vScore=4

if vScore >= 50:
    print("PASS")
else:
    print("FAIL")

#if in

vMonth = "September"
vLetter = "e"

if vLetter in vMonth:
    print("There is a letter", vLetter, "in", vMonth)
else:
    print("There is NOT a letter", vLetter, "in", vMonth)

#elif

vChoice = raw_input("Enter Number 1 to 3:")
print()

if vChoice == "1":
    print("Chose Item 1")

elif vChoice =="2":
    print("Chose Item 2")

elif vChoice =="3":
    print("Chose Item 3")


# program that works out the score for a give word
# a = 5
# e = 4
# i = 3
# o = 2
# u = 1
vWord = raw_input("Enter a word:")

#convert tthe word into lower case

vWord = vWord.lower()

#set score to be 0

score=0

# Creat a lopp so that
# letters are looked at one by one
for letter in vWord:
    if letter =="a":
        score = score+5
        print(letter,"is worth 5")
    elif letter =="e":
        score = score+4
        print(letter, "is worth 4")
    elif letter == "i":
        score = score+3
        print(letter,"is worth 3")
    elif letter == "o":
        score = score+2
        print(letter,"is worth 2")
    elif letter == "u":
        score = score+1
        print(letter,"is worth 1")
    else:
        print(letter,"is worth 0")
#End of loop
# Print the score

print("Total schore is",score)
