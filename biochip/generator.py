n=5
p0=0.29
p90=0.1
v=0
for i in range(1,n+1):
    v+=p0*i
    print("{} {} {}".format(i,round(v,2),round(i*p90,2)))

print("\n\n\n")  
data = [1,0.29,0.1]
    
for i in range(2,n+1):
    print(data[0],data[1],data[2])
    data[0]+=1
    data[1]=round(data[1]+i*0.29,2)
    data[2]=round(i*0.1,2)