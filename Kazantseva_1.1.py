a = [1,2,3,4,5,6,236,237,238]
for i in range(len(a)):
    z=a.pop(0)
    if (z%2)==0:
        print(z)
    elif z==237:
        break
