n=int(input("Enter your range:"))
a=0
b=1
c=0
while a<n:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
rev=0
while a!=0:
  rem=a%10
  rev=rev*10+rem
  a=a//10
print("reversed number is:",rev)
