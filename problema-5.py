v=''
f=open('input.txt', 'r')
for i in f.readline():
    if i in ['a','e','i','o','u']:
        v+=i
f.close()
a=open('output.txt', 'a') 
a.write(v)
a.close()