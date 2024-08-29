# A--Z -> 65-90
# a -- z -> 97-122
d={'a':"z",'b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
print(d)
s='abCd'
r=''
for i in s:
    if i.isupper():
        r+=d[i.lower()].upper()
    else:
        r+=d[i]
print(r)

#method 2

s='abds'
r=''
for i in s:
    r+=chr(ord('a')+ord('z')-ord(i))
print(r)