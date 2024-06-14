# counts occurance

lsst=['a','b','c','b','b','a']
chr='b'
count=0

for i in lsst:
    if i==chr:
        count+=1

print('The Occurance of',chr,'is : ',count)