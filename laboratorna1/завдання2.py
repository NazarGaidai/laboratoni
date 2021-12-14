n=int(input("n")) 
m=int(input("m")) 
while n !=0 and m !=0: 
    if n>= m: n%=m 
    else: m%=n 
print (n)