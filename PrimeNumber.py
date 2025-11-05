num = int(input("Enter the number : "))
PrimeNum = False

def CheckPrime(num):
    for i in range(2,num-1):
        if(num%i == 0):
            return False
        else:
            return True
        
if(CheckPrime(num)):
    print(num, " is a prime number...")

else:
    print(num, " is not a prime number....")