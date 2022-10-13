# Implement a Calculator Class
class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    
num1 = int(input("Enter first number: "))
num2=int(input("Enter second number: "))
calculator_obj = calculator(num1,num2)

print("Addition : ",calculator_obj.add()) 
print("Subtraction :",calculator_obj.sub())
print("Multiplication :",calculator_obj.mul())
print("Division :",calculator_obj.div())


