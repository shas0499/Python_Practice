in_num = int(input("Enter any number : "))
fact = 1

for i in range(in_num,1,-1):
    fact = fact*i

print("Factorial of ",in_num," is : ",fact)