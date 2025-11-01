in_num = int(input("Enter any number : "))

def prim_func(in_num):
    for i in range(1,in_num-1):
        if(in_num % 2 == 0):
            return False

    else:
        return True
    
if(prim_func(in_num)):
    print(in_num," is a prime number...")

else:
    print(in_num," is not a prime number...")
