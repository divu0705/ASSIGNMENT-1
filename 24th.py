#calculator

choice=input('Enter ur choice betwwn 1,2,3,4')
if choice =='1':
    a=int(input('Enter 1st no'))
    b=int(input('Enter 2nd no'))
    print('The sum is: ',a+b)

if choice =='2':
    a=int(input('Enter 1st no'))
    b=int(input('Enter 2nd no'))
    print('The difference is: ',a-b)

if choice =='3':
    a=int(input('Enter 1st no'))
    b=int(input('Enter 2nd no'))
    print('The multiplication is: ',a*b)

if choice =='4':
    a=int(input('Enter 1st no'))
    b=int(input('Enter 2nd no'))
    print('The division is: ',a/b)

else:
    print('Invalid choice')