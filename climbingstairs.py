s=int(input())
c=0
while s>0:
    n=1<<s.bit_length()-1
    c+=1
    s-=n
print(c)

#method 2
s=int(input())
k=str(bin(s))
print(k.count('1'))