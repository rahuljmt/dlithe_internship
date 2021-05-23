#program to calculate the EB bill
a=int(input('Enter the unit:'))
print('Adittional charges=RS 60')
print('Electricity tax=5%')
print('Rate: 0-31 unit=Rs3.75\nfor 31-100 unit=Rs5.20\nfor 101-200 unit=Rs6.75\nabove 201 unit=Rs7.8')  
if 0<=a and a<=30:
    bill=(a*3.75) + 60   
elif 31<=a and a<=100 :
    bill=(a*5.20)+60
elif 101<=a and a<=200:
     bill=(a*6.75)+60
else:
      bill=(a*7.8)+60       
e=bill+(bill*0.05)              
print('Electricity bill: Rs',e)      










    






