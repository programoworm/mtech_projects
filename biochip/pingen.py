#Generate pin numbers

import random
from copy import deepcopy

def index(x,sc):
	ind=[]
	for i in range(len(sc)):
		if x==sc[i]:
			ind.append(i)
	return ind

def score(grid):
	s=len(set(i for j in grid for i in j))*(-10)
	return s

def select(pop):
	sc=[]
	for i in pop:
		sc.append(score(i))
	
	print(sc)
	
	#print(max(sc)," ",index(max(sc),sc))
	
	i1=index(sorted(sc)[-1],sc)
	i2=index(sorted(sc)[-2],sc)

	i3=index(sorted(sc)[0],sc)
	i4=index(sorted(sc)[1],sc)
	
	if len(i1)>1 and len(i3)>1:
		return (i1[0],i1[1],i3[0],i3[1])
	elif len(i1)>1:
		return (i1[0],i1[1],i3[0],i4[0])
	elif len(i3)>1:
		return (i1[0],i2[0],i3[0],i3[1])
	else:
		return (i1[0],i2[0],i3[0],i4[0])


def crossover(pop,ind,n):
	e1=pop[ind[0]]
	e2=pop[ind[1]]
	pop.append(deepcopy(e1))
	pop.append(deepcopy(e2))
	
	selr=[random.randint(0,n-1)]
	selr.append(random.choice([e for e in range(n-1) if e not in selr]))
	selc=[random.randint(0,n-1)]
	selc.append(random.choice([e for e in range(n-1) if e not in selc]))
	print("selr:",selr," selc:",selc)

	print("e1:\n",e1)
	print("e2:\n",e2)

	for i in range(min(selc[0],selc[1]),max(selc[0],selc[1])):
		t=e1[selr[0]][i]
		e1[selr[0]][i]=e2[selr[0]][i]
		e2[selr[0]][i]=t
		t=e1[selr[1]][i]
		e1[selr[1]][i]=e2[selr[1]][i]
		e2[selr[1]][i]=t
		
	print("e1:\n",e1)
	print("e2:\n",e2)
	print("pop1\n",pop[ind[0]])
	print("pop2\n",pop[ind[1]])
	
	

def mutate():
	pass

n=int(input())

pop=[]

for _ in range(10):
	grid=[]
	for _ in range(n):
		t=[]
		for _ in range(n):
			t.append(random.randint(1,n**2))
		grid.append(t)
	
	pop.append(grid)
G=0

for _ in range(10):
	print("Generation ",G,":")
	c=1
	sc=[]

	for i in pop:
		print("pop ",c,"\t\t\t\tscore: ",score(i))
		sc.append(score(i))
		c+=1
		for j in i:
			print(j)
		print()
	print("Total Score: ",sum(sc))


	indx=select(pop)
	print(indx)
	print(pop[indx[0]])
	print(pop[indx[1]])
	crossover(pop,indx,n)

	del pop[indx[2]]
	del pop[indx[3]]

	c=1
	sc=[]
	G+=1

for i in pop:
	print("pop ",c,"\t\t\t\tscore: ",score(i))
	sc.append(score(i))
	c+=1
	for j in i:
		print(j)
	print()
print("Total Score: ",sum(sc))
