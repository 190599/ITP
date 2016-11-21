vpt=0

print("Welcome to Riot")
print("If you want to get in this company, you have to get higher grade than B on this test")
print("Good Luck")

print("Do you want to read the 'How to play'?")
vhowtoplay=input("yes or no")

if vhowtoplay=="yes":
    print("THIS IS HOW TO PLAY")
    vhtp=input("Enter 'done' when done reading")
    if vhtp=="done":
        print("Entering game...")

if vhowtoplay=="no":
    print("Entering game...")

def tquestions (int1,question,answer):
    global vpt
    print("Question",int1)
    vanswer=input(question)
    if vanswer==answer:
        vpt = vpt+5
        print("Correct!")
        print("You now have",vpt,"points")
    elif vanswer!=answer:
        vpt=vpt-5
        print("Incorrect")
        print("You now have",vpt,"points")

def mquestions (int1,ans1,ans2,ans3,ans4,question,answer):
    global vpt
    print("Question",int1)
    WORDS = (ans1,ans2,ans3,ans4)
    print(WORDS)
    vanswer=input(question)
    if vanswer==answer:
        vpt=vpt+5
        print("Correct!")
        print("You now have",vpt,"points")
    elif vanswer!=answer:
        vpt=vpt-5
        print("Incorrect")
        print("You now have",vpt,"points")





tquestions(1,"How many champions are there in league of legends?","123")
tquestions(2,"How many skins are there in league of legends?","923")
mquestions(3,"1. Vayne","2. Reksai","3. Gangplank","4. Shen","Which of the above champion has a Poolparty skin?","2")
mquestions(4,"1. Miss Fortune", "2. Illaoi","3. Ahri","4. Zyra","Which of the above champion is Gangplank's first love", "2")
