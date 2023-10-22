'''
def remove(x):
    if [x[1],x[0]] in resu:
        return False
    else:
        return True
n = 10
prime = [True]*(n+1)
p= 2
while p*p <= n:
    if p:
        for i in range(p*p,n+1,p):
            prime[i] = False
    p += 1
result = [x for x in range(2,n+1) if prime[x]]
resu = [[x,n-x] for x in result if n-x in result and x<=n-x]
print(resu)'''
a , b , c = 10 ,20 , 5
i = a<b<c
print(i)