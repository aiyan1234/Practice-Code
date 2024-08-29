s1=input()
s1=list(s1)
c1=input()
c2=input()
for i in range(len(s1)):
    if s1[i]==c1:
        s1[i]=c2
    elif s1[i]==c2:
        s1[i]=c1
print(''.join(s1))