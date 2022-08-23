import tripy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

STAR = [(350, 75), (379, 161), (469, 161), (397, 215), (423, 301), (350, 250), (277, 301), (303, 215), (231, 161), (321, 161)]
NEW_THANG = [(-20.0, -20.0), (-10.0, -20.0), (-10.0, -30.0), (0.0, -20.0), (10.0, -20.0), (0.0, -10.0), (10.0, 0.0), (0.0, 0.0), (-10.0, -10.0), (-10.0, 0.0), (-20.0, -10.0), (-30.0, -10.0)]
NEW_EXAMPLE = [(-10.0, -20.0), (-10.0, -30.0), (0.0, -20.0), (0.0, -10.0), (-20.0, -10.0), (-20.0, -20.0)]
NO_CONCAVE_VERTEX = [(-2.0, -17.0), (-2.0, -8.0), (-8.0, -2.0), (-17.0, -2.0), (-20.0, -8.0), (-18.0, -17.0), (-12.0, -24.0), (-7.0, -22.0)]
polygon=NEW_THANG
polygon.append(polygon[0])

triangles = tripy.earclip(polygon)

print(triangles)
for i in triangles:
    for j in i:
        plt.plot(j[0],j[1],'o:r')

plt.plot(np.array([i[0] for i in polygon]),np.array([i[1] for i in polygon]),linewidth='6',color='yellow')
for j in triangles:
    plt.plot(np.array([i[0] for i in j]),np.array([i[1] for i in j]),'o-r')
    plt.plot(np.array([j[0][0],j[len(j)-1][0]]),np.array([j[0][1],j[len(j)-1][1]]),'o-r')
for i in polygon:
    plt.text(i[0],i[1]+1,'({},{})'.format(i[0],i[1]),size=12,color='black')

handles,labels=plt.gca().get_legend_handles_labels()

v=mlines.Line2D([0],[0],color='yellow',linestyle='-',label='Given Polygon')
d=mlines.Line2D([0],[0],color='red',linestyle='-',label='Triangulated Polygon')
handles.extend([d,v])
plt.legend(handles=handles,loc="lower right",prop={'size':12})
plt.show()