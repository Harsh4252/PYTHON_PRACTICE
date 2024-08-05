# break the loop as soon it sees 'e' 
# or s

i=0
a='santabanta'
while i<len(a):
    if a[i]=='n':
        break
    i=i+1
print('Current Letter:',a[i],i)