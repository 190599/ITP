numberList1 = [1,2,3]
numberList2 = [6,7,8]
numberList3 = [numberList1+numberList2]

print (numberList3*3)

fruitlist = ("apple", "orange","banana","grape","tomato","mango")

print(fruitlist [2:5])
print(fruitlist [:4])
print(fruitlist[5:])

fruitList = ["apple", "orange","banana","grape","tomato","mango"]
fruitList [1] = "kiwi" #change value at position 1

print (fruitList)


olympicList = [["London", 2012],["Beijing",2008],["Athens",2004]]

print(olympicList)

print (olympicList[1]) #print the first element in the list

print (olympicList[1][0]) #print the second elemnt in the list's first place

inventoryList=["sword","armour","shield","healing potion"]

print(inventoryList)

inventoryList.append("cabbage")

print (inventoryList)

inventoryList.insert(2,"hehe")

print(inventoryList)

inventoryList.sort()

print(inventoryList)

print (inventoryList.count("sword"))

inventoryList.extend(fruitlist)

print(inventoryList)

v_fruit=fruitList.pop() #remove last element
print(fruitList)
print(v_fruit)

vfruit=fruitList.pop(0) #remove first element
print(fruitList)
print(v_fruit)

fruitList.remove("banana")#remove first occuracne of an element
print(fruitList)

fruitList = ["apple", "orange","banana","grape","tomato","mango"]

v_index=fruitList.index("banana") #print postion of banana
print(v_index)

print(min(fruitList))
print(max(fruitList))
