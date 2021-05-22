#Read three integers from the keyboard a,b,c in max,mid and min
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
c=int(input('Enter the third number:'))
num_list=[a,b,c]
num_list.sort(reverse=True)
for i in range(0,2,1):
    print(num_list[i],end=' > ')
print(num_list[-1])