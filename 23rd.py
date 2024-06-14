# conversion of temperature

choice=input('Enter ur choice in a number')

if choice =='1':
    temp=int (input('Enter your temperature in celcius'))
    f=((9/5)*temp)+32
    print ("The temperature is ",f)


if choice =='2':
    temp=int (input('Enter your temperature in fahrenhiet'))
    c=((f-32)*5)/9
    print ("The temperature is 'c' degree celcius")