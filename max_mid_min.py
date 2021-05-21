#Read three integers from the keyboard a,b,c in max,mid and min
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
c=int(input('Enter the third number:'))
num_list=[a,b,c]
max_num=max(num_list)
min_num=min(num_list)
print(max_num,max_num-min_num,min_num,sep='<<')


