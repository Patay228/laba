import random
def gen(s):
    m=[]
    for i in range (s):
        row=[]
        for i in range(s):
            row.append(random.randint(-100,100))
        m.append(row)
    return m
def sum(b):
    c=0
    d=len(b)
    for i in range(d):
        for j in range(i+1,d):
            if  b[i][j]<0:
                c=c+1
    return c 
def f(x):
    try:
        int(x)
        return True
    except:
        ValueError
        return False
n=input("Введите кол-во строк и стлобцов матрицы: ")
s=0
while s==0:
    if f(n)==True and int(n)>0:
        ran=gen(int(n))
        for row in ran:
            print(row)
        print(sum(ran))
        break
    else:
        print("Ошибка")
        break