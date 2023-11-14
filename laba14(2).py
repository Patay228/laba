def f(y,start,stop):
    result=[]
    for q in range(start,stop):
        result.append(y[q])
    return result
def F(g):
    if len(g)==0:
        return None
    last_element=g[-1]
    g[:]=g[:-1]
    return last_element
s=input("Введите текст со скобками")
if "(" in s or ")" in s or "[" in s or "]" in s or "{" in s or "}" in s:
    stack=[]
    sight=True
    for i in s:
        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if len(stack)==0:
                sight=False
                break
            open=F(stack)
            if open=="(" and i==")":
                continue
            if open=="{" and i=="}":
                continue
            if open=="[" and i=="]":
                continue
            sight=False
            break
else:
    print("NOOOOOOOOOOO")
if sight and len(stack)==0:
    print("Баланс")
else:
    print("NOOOOOOOOOOO")