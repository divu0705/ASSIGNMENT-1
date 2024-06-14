#counts the frequency of each character

a=input('Enter a string ')
d={}

for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for i in d:
    print(i,d[i])
    print(end=" ")






