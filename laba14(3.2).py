def F(w):
    try:
        int(w)
        return True
    except:
        ValueError
        return False
import random
def t(lst,element):
    index=None
    for i in range(len(lst)):
        if lst[i]==element:
            index=i
    return index
def f(a):
    if a:
        return a[0]*f(a[1:])
    return 1
n=input("Введите длину списка ")
lst=[]
q=0
while q==0:
    if F(n)==True and int(n)>0:
        while len(lst)<int(n):
            lst.append(random.randint(-100,100))
        maximum=lst[0]
    else:
        print("Ошибка")
        break
    breakpoint
    if lst==[]:
        print("Ошибка")
        break
    print(lst)
    for i in range(1,len(lst)):
        if abs(lst[i])>abs(maximum):
            maximum=lst[i]
    print("Кол-во произведения всех чисел, стоящих после максимального по модулю",f(lst[t(lst,maximum):])/maximum)
    break