lst = [10, -5, 15, -4, 45, -32, 40]

positive = 0
negetive = 0

for i in lst:
    if(i<0):
        negetive += 1
    
    elif(i>0):
        positive += 1

print("List is : ",lst)
print("Count of Positive variables in the List : ",positive)
print("Count of negetive variables in the List : ",negetive)