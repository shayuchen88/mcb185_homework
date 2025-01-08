# initialize
s1 = 0 # first number in sequence / previous 2 of current position 
s2 = 1 # second number in sequence / previous 1 of current position
print(s1)
print(s2)

# continue
for i in range(8): 
    current = s1 + s2 # rule of Fibonacci sequence
    print(current)
    s1 = s2 # update 
    s2 = current # update
    
    



