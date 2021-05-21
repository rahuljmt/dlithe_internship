def add(num1,num2):
    print("Sum :",num1+num2)
def sub(num1,num2):
    print("Sum :",num1-num2)    
def multi(num1,num2):
    print("Sum :",num1*num2)    
def divi(num1,num2):
    print("Sum :",num1/num2)    
print("Enter\n 1)-Addition\n 2)-Subtraction\n 3)-Multiplication\n 4)-Division")
ch = int(input())
print("Please enter the numbers:\n")
num1 = int(input())
num2 = int(input())

if ch==1:
    add(num1,num2)
elif ch==2:
    sub(num1,num2) 
elif ch==3:
    multi(num1,num2)
elif ch==4:
    divi(num1,num2)   