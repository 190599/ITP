#DEFINING INPUTS
cash = float(input("Please input value of cash"))
price = float(input("Please input price of chocolate"))
change = (cash-price)*10

if change<0:
    print ("Insufficient funds,please enter",-change/10,"dollars")
elif change == 0:
    print ("The price of chocolate is",price,"dollars")
    print ("The amount of paid is",cash,"dollars")
    print ("No change is given.")
else:
    print ("The price of chocolate is",price,"dollars")
    print ("The amount paid is",cash,"dollars")
    print ("Change due is",change/10,"dollars")

    TenCentcoin = 0
    FiftyCentcoin = 0
    OneDollarcoin = 0
    TwoDollarcoin = 0
    FiveDollarcoin = 0
    TenDollarcoin = 0

    while change>0:
        if change>=100:
            change=change-100
            TenDollarcoin-TenDollarcoin+1
