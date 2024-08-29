#clear k bit
n=int(input())
k=int(input())
res=n &(~(1<<(k-1)))
print(res)