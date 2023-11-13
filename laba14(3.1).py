def F(w):
    try:
        int(w)
        return True
    except:
        ValueError
        return False
import random
def f(a):
    if a:
        return a[0]+f(a[1:])
    return 0
n=input()
lst=[]
krat2=[]
c=0
if F(n)==True:
    while len(lst)<int(n):
        lst.append(random.randint(-100,100))
else:
    print("Ошибка")
print(lst)
for i in lst:
    if i%2==0:
        c+=1
        krat2.append(i)
if krat2==[]:
    print("Ошибка")
print(c,f(krat2))