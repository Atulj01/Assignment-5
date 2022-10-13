#Square Numbers and Return Their Sum


from difflib import SequenceMatcher
from threading import BrokenBarrierError


class point:
    def __init__(self,no1,no2,no3):
        no1 = int(input("enter the value:"))
        no2 = int(input("enter the value:"))
        no3 = int(input("enter the value:"))
        square = no1 **2, no2**2 ,no3 **2
        print(square)

    def sqSum(self,no1,no2,no3):
        sum = no1 + no2 + no3
                      
point_obj = point()


