#if 1 at k bit to 0 or 0 to 1
n=int(input())
k=int(input())
print(bin(n))
res=n^(1<<(k-1))
print(res)
print(bin(res))