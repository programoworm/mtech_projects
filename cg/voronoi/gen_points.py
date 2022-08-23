import random
from Fortunes import Site,Builder

sites=[]
n=5
builder=Builder(0.0, 100.0, 0.0, 100.0)
i = 0
while i < n:
    site = Site(random.randint(0,100), random.randint(0,100))
    edge = builder.insertSite(site)
    if (edge != None):
        print((site.x, site.y))
        i += 1