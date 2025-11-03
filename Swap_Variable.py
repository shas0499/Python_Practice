# Using Third Variable
a = 10
b = 5

c = a
a = b
b = c

print("a = ",a)
print("b = ",b)

# Without Using third Variable
x = 20
y = 30

x,y = y,x
print("x = ",x)
print("Y = ",y)