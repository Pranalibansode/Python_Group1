#calculate compound interest

'''formula A=p(1+(r\100))**n

where P=ptinciple
      r=rate of interest
      n= time in years'''
      
p=1000
r=10
n=2
ri=r/100
A=p*(1+ri)**n
print("A =",A)
interest=A-p
print("interest is :",interest)
