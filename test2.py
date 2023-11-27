import random
def gen(s):
    m=[]
    for i in range (s):
        row=[]
        for i in range(s):
            row.append(random.randint(-100,100))
        m.append(row)
    return m
def f(x):
    try:
        int(x)
        return True
    except:
        ValueError
        return False
def sor(lst):
    result = list(lst)
    for i in range(len(result)):
        for j in range(len(result)-i-1):
            if result[j]>result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result
def chet(g):
    chetko=[]
    for i in range(len(g)):
        for j in range(i+1,len(g)):
            if g[i][j]%2==0:
                chetko.append(g[i][j])
    return chetko
def my_zip(*iterables):
    lengths = [len(iterable) for iterable in iterables]
    min_length = min(lengths)
    result = []
    for i in range(min_length):
        temp_tuple = ()
        for iterable in iterables:
            temp_tuple += iterable[i],
        result.append(temp_tuple)
    return result
def p(a):
    if a:
        return a[0]+p(a[1:])
    return 0
def enumer(lst):
    index = 0
    for item in lst:
        yield index, item
        index += 1
def uslov(s):
    character=p([ t for t in s if t%2==0 and t>0])
    return character
n=input("Введите кол-во строк и стлобцов матрицы: ")
if f(n)==True and int(n)>0:
    ran=gen(int(n))
    for row in ran:
        print(row)
    characters=[uslov(row) for row in ran]
    sorted_matrix=[row for _, row in sor(my_zip(characters,ran))]
    for i, row in enumer(sorted_matrix):
        print(f"Характеристика строки{i + 1}:{uslov(row)}")
        print(row)
else:
    print("Ошибка")




