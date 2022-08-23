import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
p=[]
with open('points.txt',"r") as fp:
    for i in fp.readlines():
        t=eval(i.strip("\n"))
        p.append(t)
print(p)
vor = Voronoi(p)
fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='y', point_size=10)
plt.show()