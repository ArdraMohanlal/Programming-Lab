#11.write a lambda function to find the area of square, rectangle and triangle
l=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadh of the rectangle"))
h=int(input("Enter the height of the triangle"))
ar=lambda x,y:x*y
asq=lambda x:x*x
at= lambda x,y:0.5*x*y
print("area of rectangle",ar(l,b))
print("area of square",asq(l))
print("area of triangle",at(b,h))
