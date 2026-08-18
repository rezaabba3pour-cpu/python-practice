a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b and b== c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Right Triangle")
else:
    print("None")
