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
n=input("Введите длину списка ")
lst=[]
krat2=[]
c=0
q=0
while q==0:
    if F(n)==True and int(n)>0:
        while len(lst)<int(n):
            lst.append(random.randint(-100,100))
        print(lst)
        for i in lst:
            if i%2==0:
                c+=1
                krat2.append(i)
        if krat2==[]:
            print("Ошибка")
            break
        print("Кол-воккртаных 2: ",c,"Их сумма:: ",f(krat2))
        break
    else:
        print("Ошибка")
        break
    #добавить исключение про 0
