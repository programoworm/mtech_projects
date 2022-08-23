import random
points=[divmod(elem,101) for elem in random.sample(range(101*101),5)]
for i in points:
    print(i)
