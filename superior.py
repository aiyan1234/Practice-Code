'''n=int(input())
a=list(map(int,input().split()))
c=0
i=0
while i<n-1:
    if a[i+1]>a[i]:
        c+=1
    i+=1
print(c+1)'''
n=int(input())
a=[int(x) for x in input().split()]
sup=a[-1]
count=1
i=len(a)-2
while i>=0:
    if a[i]>sup:
        count+=1
        sup=a[i]
    i-=1
print(count)