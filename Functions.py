print("""
Line 1
Line 2
Line 3
""")

def i2p_intro():
    print_function("""
    HKIS..
    Intro to programming
    ..with Ms Mok!! ..V2
    """)

#function

def f_sum(int1,int2):
    """This function will add two numbers"""
    return int1+int2

#main function

vTotal=f_sum(10,15)
print ("The total is",vTotal)

def f_print_largest(int1,int2):
    """This function will print the largest of two intergers"""
    if int1>int2:
        print (int1,"is the largest")
    if int1<int2:
        print (int2, "is the largest")

print (f_print_largest(10,15))

