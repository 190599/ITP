#Enter the Price of the Chocolate bar)
vPrice=float(input("Please enter the price of the chocolate you want:"))
print(vPrice)

#Enter the Cash to pay for hte chocolate
vCash=float(input("Please enter the cash of the chocolate you want:"))
print(vCash)

##Calculat the Change DUe
vChangeDue=vPrice-vCash
vChangeGiven=round(vChangeDue,2)

#Display the Price, Cash, Change Due and ChangeGiven
print("TRANSACTION SUMMARY MY FUNCTION")
print("Price of Chocolate:",vPrice)
print("Cash Paid:",vCash)
print("Change Due:",round(vChangeDue,2))
print("Total CHange Given:",vChangeGiven)

#While the Change Due is great than -
#Give out the largest coin possible

while vChangeDue>=50:
    vChangeGiven=vChangeGiven+50
    vChangeDue=vChangeDue-50
    print("Giving out $50 note")

while vChangeDue>=20:
    vChangeGiven=vChangeGiven+20
    vChangeDue=vChangeDue-20
    print("Giving out $20 note")

while vChangeDue>=10:
    vChangeGiven=vChangeGiven+10
    vChangeDue=vChangeDue-10
    print("Giving out $10 note")

while vChangeDue>=5:
    vChangeGiven=vChangeGiven+5
    vChangeDue=vChangeDue-5
    print("Giving out $5 note")

while vChangeDue>=2:
    vChangeGiven=vChangeGiven+2
    vChangeDue=vChangeDue-2
    print("Giving out $2 note")
