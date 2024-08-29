s=input()
'''num='0' 
sum1=0
for i in s:
    if i.isdigit():
        num+=i
    else:
        sum1+=int(num)
        num='0'
sum1+=int(num)
print(sum1)
    '''
    
num=0
res=0
for i in s:
    if i.isdigit():
        num=num*10+int(i)
    else:
        res+=num
        num=0
res+=num
print(res)