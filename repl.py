#s1=ABD
#s2=AABCCAD
#op=4
s1=input()
s2=input()
l2=list(s2)
for i in s1:
    if i in s2:
        l2.remove(i)
print(len(l2))
