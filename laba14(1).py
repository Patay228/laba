s =input()
new_s = []
for i in s:
    if i not in new_s:
        new_s.append(i)
a=""
for n in new_s:
    a+=n
print(a[0]+a[2:])