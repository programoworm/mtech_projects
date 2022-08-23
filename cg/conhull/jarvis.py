import matplotlib.pyplot as plt
import numpy as np
#Finding the left most point
def Left_index(points):
	
	minn = 0
	for i in range(1,len(points)):
		if points[i][0] < points[minn][0]:
			minn = i
		elif points[i][0] == points[minn][0]:
			if points[i][1] > points[minn][1]:
				minn = i
	return minn

'''
	To find orientation of ordered triplet (p, q, r).
	The function returns following values
	0 --> p, q and r are collinear
	1 --> Clockwise
	2 --> Counterclockwise
'''
def orientation(p, q, r):
	val = (q[1] - p[1]) * (r[0] - q[0]) - \
		(q[0] - p[0]) * (r[1] - q[1])

	if val == 0:
		return 0
	elif val > 0:
		return 1
	else:
		return 2

def convexHull(points, n):
	
	# There must be at least 3 points
	if n < 3:
		return

	# Find the leftmost point
	l = Left_index(points)

	hull = []
	
	'''
	Start from leftmost point, keep moving counterclockwise
	until reach the start point again. This loop runs O(h)
	times where h is number of points in result or output.
	'''
	p = l
	q = 0
	while(True):
		
		# Add current point to result
		hull.append(p)
		q = (p + 1) % n

		for i in range(n):
			
			# If i is more counterclockwise
			# than current q, then update q
			if(orientation(points[p],
						points[i], points[q]) == 2):
				q = i
		p = q

		# While we don't come to first point
		if(p == l):
			break
	return hull

def main():
	# Driver Code
	p=[]
	#print("The points are:")
	with open('points.txt',"r") as fp:
	    for i in fp.readlines():
	        t=eval(i.strip("\n"))
	        #print(t)
	        p.append(t)
	ind=convexHull(p, len(p))
	Hull=[p[i] for i in ind]
	Hull.append(p[ind[0]])
	for i in p:
		plt.plot(i[0],i[1],'o:r')
	for i in Hull:
	        plt.text(i[0],i[1]+1,'({},{})'.format(i[0],i[1]),size=12,color='black')
	plt.plot(np.array([i[0] for i in Hull]),np.array([i[1] for i in Hull]),'x:y')
	print(Hull)
	plt.show()

if __name__ == '__main__':
	main()