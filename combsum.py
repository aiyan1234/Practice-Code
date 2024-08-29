s=input()
sum1=0
for i in range(len(s)):
    for j in range(i,len(s)):
        sum1+=int(s[i:j+1])
print(sum1)