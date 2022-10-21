#Square Numbers and Return Their Sum



class point:
    def __init__(self,no1=0,no2=0,no3=0):
        self.no1 = no1
        self.no2 = no2
        self.no3 = no3
      
    def sqsum(self):
        no1 = int(input("enter the value:"))
        no2 = int(input("enter the value:"))
        no3 = int(input("enter the value:"))
        square = no1 **2, no2**2 ,no3 **2
        print("Square of values : ",square)

        sum = no1 **2 + no2**2 + no3 **2
        print("sum of square : ",sum)

point_obj = point()
point_obj.sqsum()


