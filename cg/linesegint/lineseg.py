import matplotlib.pyplot as plt
from matplotlib import collections as mc
import random
import pylab as pl
import numpy as np

finter=[]
def onSegment(p, q, r):
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and 
           (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False
  
def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
      
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/ 
    # for details of below formula. 
      
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
    if (val > 0):
          
        # Clockwise orientation
        return 1
    elif (val < 0):
          
        # Counterclockwise orientation
        return 2
    else:
          
        # Collinear orientation
        return 0
  
# The main function that returns true if 
# the line segment 'p1q1' and 'p2q2' intersect.
def dointer(p1,q1,p2,q2):
      
    # Find the 4 orientations required for 
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
  
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
  
    # Special Cases
  
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
  
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
  
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
  
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
  
    # If none of the cases
    return False

def poi(line1, line2):
    if dointer(line1[0],line1[1],line2[0],line2[1]):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        if (x,y) not in finter:
            finter.append((x,y))
        return (x,y)
    else:
        return False

def isleft(x,p,n): #To check if the point is left end point or not
    for i in range(n):
        if x in p[i]:
            if x==p[i][0]:
                return True
            else:
                return False

class Event:
    def __init__(self,p,t,s):
        self.e=p
        self.t=t
        self.s=s

def main():
    p=[]
    with open('points.txt',"r") as fp:
        for i in fp.readlines():
            p.append(eval(i.strip("\n")))
    print(p)
    n=len(p)
    eq=[]
    for i in range(n):
            for j in range(2):
                t=1
                if isleft(p[i][j],p,n): # 0: left 1: right
                    t=0
                eq.append(Event(p[i][j],t,i))
    eq.sort(key=lambda eq: eq.e[0])
    for e in eq:
        print(e.e,e.t,e.s)
    sls=[] #sweepline status
    inters=[]
    l=len(eq)
    k=0
    for i in eq:
        print("sls:",sls)
        for e in eq:
            print("iter ",k,":",e.e,e.t,e.s)
        k+=1
        print("selected :",i.e,i.t,i.s)
        if i.t==0: #left end point
            sls.append([i.e,i.s])
            sls.sort(key=lambda sls: sls[0][1])
            index=sls.index([i.e,i.s])
            if len(sls)>2:
                if index==0:
                    if poi(p[sls[index][1]],p[sls[index+1][1]]):
                        pi=Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1]))))
                elif index==len(sls)-1:
                    if poi(p[sls[index-1][1]],p[sls[index][1]]):
                        pi=Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1]))))
                else:
                    if poi(p[sls[index-1][1]],p[sls[index+1][1]]):
                        pi=Event(poi(p[sls[index-1][1]],p[sls[index+1][1]]),2,(min(sls[index-1][1],sls[index+1][1]),max(sls[index-1][1],sls[index+1][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        
                    if poi(p[sls[index][1]],p[sls[index+1][1]]):
                        pi=Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1]))))
                    if poi(p[sls[index-1][1]],p[sls[index][1]]):
                        pi=Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1]))))
            if len(sls)==2:
                if index==0:
                    if poi(p[sls[index][1]],p[sls[index+1][1]]):
                        pi=Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index][1]],p[sls[index+1][1]]),2,(min(sls[index][1],sls[index+1][1]),max(sls[index][1],sls[index+1][1]))))
                else:
                    if poi(p[sls[index-1][1]],p[sls[index][1]]):
                        pi=Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1])))
                        for r in range(len(eq)):
                            if eq[r].e==pi.e:
                                del eq[r]
                                break
                        eq.append(pi)
                        #eq.append(Event(poi(p[sls[index-1][1]],p[sls[index][1]]),2,(min(sls[index-1][1],sls[index][1]),max(sls[index-1][1],sls[index][1]))))
                        #eq.append(inter[-1])

        if i.t==1: #right end point
            print(sls)
            index=0
            if [p[i.s][0],i.s] in sls:
                index=sls.index([p[i.s][0],i.s])
            elif [p[i.s][1],i.s] in sls:
                index=sls.index([p[i.s][1],i.s])
            else:
                continue
            if index>0 and index<len(sls)-1:
                if poi(p[sls[index-1][1]],p[sls[index+1][1]]):
                    pi=Event(poi(p[sls[index-1][1]],p[sls[index+1][1]]),2,(min(sls[index-1][1],sls[index+1][1]),max(sls[index-1][1],sls[index+1][1])))
                    for r in range(len(eq)):
                        if eq[r].e==pi.e:
                            del eq[r]
                            break
                    eq.append(pi)
            if len(sls)>0:
                del sls[index]
            print(sls)
        
        if i.t==2: #intersection point
            #print(sls)
            print("inter: ",i.e)
            inters.append(i.e)
            print(p[i.s[0]],p[i.s[1]])
            if [p[i.s[0]][0],i.s[0]] in sls:
                index1=sls.index([p[i.s[0]][0],i.s[0]])
            elif [p[i.s[0]][1],i.s[0]] in sls:
                index1=sls.index([p[i.s[0]][1],i.s[0]])
            else: index1=-1

            if [p[i.s[1]][0],i.s[1]] in sls:
                index2=sls.index([p[i.s[1]][0],i.s[1]])
            elif [p[i.s[1]][1],i.s[1]] in sls:
                index2=sls.index([p[i.s[1]][1],i.s[1]])
            else: index2=-1
            #index1=sls.index([p[i.s[0]][0],i.s[0]]) 
            #index2=sls.index([p[i.s[1]][0],i.s[1]])
            if index1!=-1 and index2!=-1:
                if index1>index2:
                    temp=index1
                    index1=index2
                    index2=temp
            if index1>0 and poi(p[sls[index1-1][1]],p[sls[index1][1]]):
                    pi=Event(poi(p[sls[index1-1][1]],p[sls[index1][1]]),2,(min(sls[index1-1][1],sls[index1][1]),max(sls[index1-1][1],sls[index1][1])))
                    print("index1:",pi.e,pi.t,pi.s)
                    for r in range(len(eq)):
                        if eq[r].e==pi.e:
                            del eq[r]
                            break
                    '''
                    if pi in eq:
                        print("removed")
                        eq.remove(pi)
                    '''
            if index2>=0 and index2<(len(sls)-1) and poi(p[sls[index2][1]],p[sls[index2+1][1]]):
                    pi=Event(poi(p[sls[index2][1]],p[sls[index2+1][1]]),2,(min(sls[index2][1],sls[index2+1][1]),max(sls[index2][1],sls[index2+1][1])))
                    print("index2:",pi.e,pi.t,pi.s)
                    for r in range(len(eq)):
                        if eq[r].e==pi.e:
                            del eq[r]
                            break
            temp=sls[index1]
            sls[index1]=sls[index2]
            sls[index2]=temp
            #print("poi(p[sls[{}][1]],p[sls[{}][1]]): {}".format(index1,index1-1,poi(p[sls[index1-1][1]],p[sls[index1][1]])))
            #print("poi(p[sls[{}][1]],p[sls[{}][1]]): {}".format(index2+1,index2,poi(p[sls[index2][1]],p[sls[index2+1][1]])))
            if index1>0 and poi(p[sls[index1-1][1]],p[sls[index1][1]]):
                    print("poi(p[sls[{}][1]],p[sls[{}][1]]): {}".format(index1,index1-1,poi(p[sls[index1-1][1]],p[sls[index1][1]])))
                    pi=Event(poi(p[sls[index1-1][1]],p[sls[index1][1]]),2,(min(sls[index1-1][1],sls[index1][1]),max(sls[index1-1][1],sls[index1][1])))
                    for r in range(len(eq)):
                        if eq[r].e==pi.e:
                            del eq[r]
                            break
                    eq.append(pi)
            
            if index2>=0 and index2<(len(sls)-1) and poi(p[sls[index2][1]],p[sls[index2+1][1]]):
                    pi=Event(poi(p[sls[index2][1]],p[sls[index2+1][1]]),2,(min(sls[index2][1],sls[index2+1][1]),max(sls[index2][1],sls[index2+1][1])))
                    for r in range(len(eq)):
                        if eq[r].e==pi.e:
                            del eq[r]
                            break
                    eq.append(pi)
                    print("poi(p[sls[{}][1]],p[sls[{}][1]]): {}".format(index2+1,index2,poi(p[sls[index2][1]],p[sls[index2+1][1]])))
                    #eq.append(Event(poi(p[sls[index2][1]],p[sls[index2+1][1]]),2,(min(sls[index2][1],sls[index2+1][1]),max(sls[index2][1],sls[index2+1][1]))))        
            sls[index1][0]=p[sls[index1][1]][1]
            sls[index2][0]=p[sls[index2][1]][1]
            sls.sort(key=lambda sls: sls[0][1])
            #print("index1:",index1,"index2:",index2)
            #print(sls)
            print("eq:",len(eq))
            #print(inters)
        
        eq.sort(key=lambda eq: eq.e[0])
        #l=len(eq)
        print("length of eq:",len(eq))
    print(sls)
    print(inters)
    
    #Graph plotting
    px=[]
    py=[]
    for i in range(n):
        for j in range(2):
            px.append(p[i][j][0])
            py.append(p[i][j][1])
    x=np.array(px)
    y=np.array(py)
    k=0
    def ind(p,t,n):
            for i in range(n):
                if t in p[i]:
                    return i
    for i,j in zip(x,y):
        plt.text(i,j+1,'seg{}:({},{})'.format(ind(p,(i,j),n),i,j),size=10,color='black')
    for i in range(0,2*n,2):
        plt.plot(np.array(list((px[i],px[i+1]))),np.array(list((py[i],py[i+1]))),'yo-')
    for i in finter:
        plt.text(i[0],i[1],'({:.1f},{:.1f})'.format(i[0],i[1]),size=10,color='black')
        plt.plot(i[0],i[1],'bo')
    plt.show()

if __name__=='__main__':
    main()
