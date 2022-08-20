import matplotlib.pyplot as plt
import numpy as np

class Stack:
    def __init__(self):
        self.size=0
        self.items=[]
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.size<=0:
            print('Nothing to pop')
            return
        self.items.remove(self.items[self.size-1])
        self.size-=1
    def print(self):
        print(self.items," ",self.size)

def criteria(point):
    return point[0]

class Graham:
    def __init__(self,points):
        points.sort(key=criteria)
        self.p=points
        self.UH=Stack()
        self.LH=Stack()
        for i in self.p:
            while(self.UH.size>1 and orient(self.UH.items[self.UH.size-2],self.UH.items[self.UH.size-1],i)<0):
                self.UH.pop()
            self.UH.push(i)
            print("Upper Hull Stack: ",self.UH.items)
        
        for i in reversed(range(len(self.p))):
            while(self.LH.size>1 and orient(self.LH.items[self.LH.size-2],self.LH.items[self.LH.size-1],self.p[i])<0):
                self.LH.pop()
            self.LH.push(self.p[i])
            print("Lower Hull Stack: ",self.LH.items)
        self.Hull=union(self.LH.items,self.UH.items)
   
def orient(p,q,r):
    print(p," ",q," ",r)
    o=(q[1]-p[1])*(r[0]-q[0])-(r[1]-q[1])*(q[0]-p[0])
    print("orient",o)
    return o

def union(p1,p2):
    p=p1
    for i in p2:
        flag=True
        for j in p:
            if i==j:
                flag=False
                break
        if flag:
            p.append(i)

    p.append(p1[0])
    return p

def main():
    p=[]
    with open('50_points.txt',"r") as fp:
        for i in fp.readlines():
            p.append(eval(i.strip("\n")))

    print(p)
    g=Graham(p)
    print("The Hull points are: \n",g.Hull)
    plt.scatter(np.array([i[0] for i in p]),np.array([i[1] for i in p]),color='black') 
    xp=np.array([i[0] for i in p])
    yp=np.array([i[1] for i in p])
    for i,j in zip(xp,yp):
        plt.text(i,j+1,'({},{})'.format(i,j),size=8,color='red')
    
    plt.plot(np.array([i[0] for i in g.Hull]),np.array([i[1] for i in g.Hull]),'x:g')
    plt.show()
    
if __name__=='__main__':
    main()
