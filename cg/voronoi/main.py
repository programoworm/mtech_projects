import random 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from Fortunes import *

# Draw the delaunay triangles
def draw_delaunay(builder, sites):
    for site in sites:
        vpList = builder.getSiteDelaunay(site)
        for vp in vpList:
            plt.plot([site.x,vp.x], [site.y,vp.y], 'c:')



# Draw the voronoi polygons
def draw_voronoi(builder, sites):
    for site in sites:
        vpList = builder.getSiteVoronoi(site)
        vpList.append(vpList[0])
        plt.plot([p.x for p in vpList], [p.y for p in vpList], 'y-', lw=2)

# initialize the Builder with the test range of X=[0,100] and Y=[0,100]
builder = Builder(0.0, 100.0, 0.0, 100.0)

sites=[]
j=0
print("The Sites are: ")
with open('points.txt',"r") as fp:
    for i in fp.readlines():
        tup=eval(i.strip("\n"))
        site = Site(tup[0],tup[1])
        print("Site {}: {}".format(j,(site.x, site.y)))
        site.sitenum = j
        j+=1
        builder.insertSite(site)
        sites.append(site)

# output the results
draw_delaunay(builder, sites)
draw_voronoi(builder, sites)
plt.plot(sites[0].x, sites[0].y, 'ro',label="Sites")
for p in sites:
    plt.plot(p.x, p.y, 'ro')
    plt.text(p.x,p.y+1,'Site {}:({},{})'.format(p.sitenum,p.x,p.y),size=12,color='black')

handles,labels=plt.gca().get_legend_handles_labels()

v=mlines.Line2D([0],[0],color='y',linestyle='-',label='Voronoi')
d=mlines.Line2D([0],[0],color='c',linestyle=':',label='Delaunay')
handles.extend([d,v])

plt.legend(handles=handles,loc="lower right",prop={'size':12})
plt.axis([0,100,0,100])
plt.show()

