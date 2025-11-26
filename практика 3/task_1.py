#анограммы
s1=input()
s2=input()
def func(s1, s2):
    b=True;
    for i in s1:
        if i not in s2:
            b=False;
    if b==True and len(s1)==len(s2):
        return "annogramms";
    else:
        return "not annogramms";
print(func(s1,s2))

