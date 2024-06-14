# returns max and min value

lst=[1,2,3,4]
max=lst[0]
min=lst[0]
for i in lst:
    if i < min:
        min=i

    if i>max:
        max=i

print('the maximum and minimum value is :', max,min)