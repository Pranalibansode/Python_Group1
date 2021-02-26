n=int(input("Enter your range:"))
a=3
b=1
c=0
while a<n:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
