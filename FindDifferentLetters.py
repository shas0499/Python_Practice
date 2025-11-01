in_str = input("Enter the string : ")

cap_let = 0
small_let = 0
space = 0
Digit = 0

for i in in_str:
    if ord(i)>=65 and ord(i)<=90:
        cap_let+=1

    if ord(i)>=97 and ord(i)<=122:
        small_let += 1

    if ord(i)== 32:
        space += 1

    if ord(i)>=48 and ord(i)<=57:
        Digit += 1

print("Total Capital Letter In The Given String Is : ", cap_let)
print("Total Small Letter In The Given String Is : ", small_let)
print("Total Digit In The Given String Is : ", Digit)
print("Total Space Present In The Given String Is : ", space)

