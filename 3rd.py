# factorial of a no

a = int(input('enter a number:'))
f = 1

for i in range(2,a+1):
    f=f*i

print('the factorial of number is : ',f)