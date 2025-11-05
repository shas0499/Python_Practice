year = int(input("Enter The Year : "))

if year % 400 == 0:
    print(year, " is Leap Year...")

elif year%100 == 0:
    print(year," is not a Leap Year...")

elif year%4 == 0:
    print(year," is a Leap year...")

else:
    print(year," is not a Leap Year...")