vchoc=8.00
vcash=float(input("Please input the amount of money you are putting in\n \n"))

vchange=vcash-vchoc

def f_change(vcash,vchoc):
    return vcash-vchoc

print("Your change is",vchange)

while vchange>=10:
    vchange=int(vchange-10)
while 10>vchange>=5:
    vchange=int(vchange-5)
while 5>vchange>=2:
    vchange=int(vchange-2)
while 2>vchange:
    vchange=int(vchange-1)

print("Here is ")
