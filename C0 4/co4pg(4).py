#4. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to 
#find sum of 2 time.
class time:
    def __init__(self):
        self.__h=int(input("enter the hour"))
        self.__m=int(input("enter the minutes"))
        self.__s=int(input("enter the seconds"))
    def __add__(self,obj2):
        hours=self.__h+obj2.__h
        print("sum of hours",hours)
        minutes=self.__m+obj2.__m
        print("sum of minutes",minutes)
        seconds=self.__s+obj2.__s
        print("sum of seconds",seconds)
        if hours>24:
            hours=hours%24
        if minutes>60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours, minutes,seconds
print("enter the time for the first object")
obj1=time()
print("enter the time for the first object")
obj2=time()
sum=obj1+obj2
print("the sum is ",sum)
    