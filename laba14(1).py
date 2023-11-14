s =input("Введите строку: ")
new_s = []
for i in s:
    if i not in new_s:
        new_s.append(i)
a=""
for n in new_s:
    if a!=" ":
        a+=n
x=[]
for g in a:
    if g not in x and g!=" ":
        x.append(g)
z=""
for k in x:
    z=z+k
print("Ответ: ",z)
