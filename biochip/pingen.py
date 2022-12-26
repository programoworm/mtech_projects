#Generate pin numbers

import random

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
	
	if len(i1)>1:
		return (i1[0],i1[1])
	else:
		return (i1[0],i2[0])


def crossover(pop,ind,n):
	e1=pop[ind[0]]
	e2=pop[ind[1]]
	
	selr=[random.randint(0,n)]
	selr.append(random.choice([e for e in range(n-1) if e not in selr]))
	selc=[random.randint(0,n)]
	selc.append(random.choice([e for e in range(n-1) if e not in selc]))
	print("selr:",selr," selc:",selc)

	print("e1: ",e1[selr[0]])
	print("e1: ",e1[selr[1]])

	t=e1[selr[0]][min(selc[0],selc[1]):max(selc[0],selc[1])]
	e2[selr[0]][min(selc[0],selc[1]):max(selc[0],selc[1])]=t
	print(e2)	
	print("t: ", t)

	e1[selr[0]][selc[0]]=e1[selr[1]][selc[1]]
	e1[selr[1]][selc[1]]=t

	t=pop[selr[0]][selc[0]]
	pop[selr[0]][selc[0]]=pop[selr[1]][selc[1]]
	pop[selr[1]][selc[1]]=t

	print(pop[selr[0]])
	print(pop[selr[1]])


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

c=1

for i in pop:
	print("pop ",c,"\t\t\t\tscore: ",score(i))
	c+=1
	for j in i:
		print(j)
	print()

indx=select(pop)
print(indx)
print(pop[indx[0]])
print(pop[indx[1]])
crossover(pop,indx,n)