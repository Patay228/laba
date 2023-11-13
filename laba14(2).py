s=input()
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
            open=stack.pop()
            if open=="(" and i==")":
                continue
            if open=="{" and i=="}":
                continue
            if open=="[" and i=="]":
                continue
            sight=False
            break
else:
    print("Ошибка")
if sight and len(stack)==0:
    print("Баланс")
else:
    print("NOOOOOOOOOOO")