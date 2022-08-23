import random
n=3
p=[]
for _ in range(n): #Random line generation
    t=[]
    for _ in range(2):
        tup=[random.randint(0,100) for _ in range(2)]
        t.append(tuple(tup))
    if t[0][0]>t[1][0]: #sorting left and right endpoints
        s=t[0]
        t[0]=t[1]
        t[1]=s
    print(t)