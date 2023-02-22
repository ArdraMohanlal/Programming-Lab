#3. Create a class Rectangle with private attributes length and width.
#Overload ‘<’  operator to compare the area of 2 rectangles.
class rectangle:
    def __init__(self):
        self.__l = int(input("enter the length of the rectangle"))
        self.__b =int(input("enter the breadth of the rectangle"))
    def __lt__(self,obj2):
        area1=self.__l*self.__b
        area2=obj2.__l*obj2.__b
        print("area of the rectangle1 is",area1)
        print("area of the rectangle2 is",area2)
        return area1<area2
print("enter the length and breadth of the object:")
obj1 = rectangle()
print("enter the length and breadth of the object:")
obj2 = rectangle()
if obj1<obj2:
    print("Area of object1 is less than object2")
else:
    print("Area ofobject1 is greater than object2")

    