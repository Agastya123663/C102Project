print('Calculator')
number1 = int(input('Please enter your first number : '))
number2 = int(input('Please enter your second number : '))
choice = int(input('type 1 to add , 2 to subtract , 3 to multiply and 4 to divide : '))

addno = number1+number2
subtractno = number1-number2
multiplyno = number1*number2
divideno = number1/number2

if(choice==1):
    print('Your number is ',addno)

elif(choice==2):
    print('Your number is ',subtractno)

elif(choice==3):
    print('Your number is ',multiplyno)

elif(choice==4):
    print('Your number is ',divideno)

else:
    print('Please insert only the given numbers')



   
