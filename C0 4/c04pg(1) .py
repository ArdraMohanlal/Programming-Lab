#1. Create Rectangle class with attributes length and breadth and methods to find area and
#perimeter. Compare two Rectangle objects by their area
class Rectangle:
    def __init__(self):
        self.length = length
        self.breadth = breadth
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    def get_area(self):
        self.length * self.breadth
    def compare(self,r2):
        try:
            if r1.get_area()==r2.get_area():
                print("both areas are equal")
            elif r1.get_area()>r2.get_area():
                print("obj1 has greater area")
            else:
                print("object2 has greater area")
        except:
            print("Objects not comparable")
l1=int(input("enter the length of rectangle1:"))
b1=int(input("enter the breadth of rectangle1:"))
l2=int(input("enter the length of rectangle2:"))
b2=int(input("enter the breadth of rectangle2:"))
r1 = Rectangle(l1,b1)
r2 = Rectangle(l2,b2)

print("Area of rectangle:",(r1.get_area()))
print("perimeter of rectangle:",(r1.get_perimeter()))

print("Area of rectangle:",(r2.get_area()))
print("perimeter of rectangle:",(r2.get_perimeter()))
r1.compare(r2)