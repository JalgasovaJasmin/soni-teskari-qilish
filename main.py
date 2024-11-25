#Foydlanuvch kiritgan sonni teskarisini chiqaradi.
n=int(input('n='))
s=0
while n>0:
    x=n%10
    s=s*10+x
    n=n//10
print(s)

