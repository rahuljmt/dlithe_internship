a=int(input('Enter the first number:'))
b=int(input('enter the second number'))
c=int(input('enter the third number'))
d=int(input('enter the fouth number'))
num_list=[a,b,c,d]
num_list.sort(reverse=True)
for i in range(0,3,1):
    print(num_list[i],end='>')
print(num_list[-1])