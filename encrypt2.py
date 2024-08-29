a='donkey'
r=''
for i in a:
    if ord(i)+5<122:
        r+=chr(ord(i)+5)
    else:
        r+=chr(ord(i)+5-26)
print(r)


#method 2
'''s='donkey'
r=''
for i in a:
    if ord(i)<ord('v'):
        r+=chr(ord(i)+5)
    else:
        r+=chr(ord(i)+5-26)
print(r)'''