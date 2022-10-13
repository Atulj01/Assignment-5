# Implement the Complete Student Class


class student:
    
    # def __init__(self):
    #     self.__name = "atul"
        
    def __set_name(self,name):
        self.name = name
    
    def __get_name(self):
        return self.name
    
    def __set_rollno(self,rollno):
        self.rollno = rollno

    def __get_rollno(self):
        return self.rollno

obj = student()

obj.set_name("Edyoda")
print("Name : ",obj.get_name())

obj.set_rollno("27")
print("RollNumber : ",obj.get_rollno())