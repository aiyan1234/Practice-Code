s1=list(map(int,input().split()))
l=[-1]
s=[1]
for i in range(len(s1)-2,-1,-1):
    while len(s)>0 and s[-1]>s1[i]:
        s.pop()
    if len(s)==0:
        l.append(-1)
    else:
        l.append(s[-1])
    s.append(s1[i])
l.reverse()
print(*l)
    
'''s1 = list(map(int, input().split()))
l = []
s = []

for i in range(len(s1)-1, -1, -1):
    while len(s) > 0 and s[-1] >= s1[i]:
        s.pop()
    if len(s) == 0:
        l.append(-1)
    else:
        l.append(s[-1])
    s.append(s1[i])

l.reverse()
print(*l)
'''
    