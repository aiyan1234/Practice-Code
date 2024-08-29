#t=[73,74,75,71,69,72,76,73]
#o=[1,1,4,2,1,1,0,0]
t = list(map(int, input().split()))  # Input temperatures
s = []  # Stack to keep indices of the temperatures
l = [0] * len(t)  # Initialize result list with zeros

# Traverse the list in reverse order
for i in range(len(t) - 1, -1, -1):
    # Pop elements from the stack while the stack is not empty and the current temperature is greater
    while s and t[s[-1]] <= t[i]:
        s.pop()
    
    # If stack is not empty, the next warmer day exists
    if s:
        l[i] = s[-1] - i  # Calculate the number of days until the next warmer temperature
    
    # Push the current index onto the stack
    s.append(i)

print(l)



#method
res=[0 for i in range(len(t))]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j]>t[i]:
            res[i]=j-i
            break
print(res)
        