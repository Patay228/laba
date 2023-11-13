def F(w):
    try:
        int(w)
        return True
    except:
        ValueError
        return False
import random
n=input()
lst=[]
if F(n)==True:
    while len(lst)<int(n):
        lst.append(random.randint(-100,100))
    maximum=lst[0]
else:
    print("Ошибка")
if lst==[]:
    print("Ошибка")
print(lst)
def f(a):
    if a:
        return a[0]*f(a[1:])
    return 1
c=0
for i in range(1,len(lst)):
    if abs(lst[i])>abs(maximum):
        maximum=lst[i]
        c=c+1
print(f(lst[c:])/maximum)