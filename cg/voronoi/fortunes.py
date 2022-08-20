import matplotlib.pyplot as plt
import numpy as np

def main():
    p=[]
    with open('points.txt',"r") as fp:
        for i in fp.readlines():
            p.append(eval(i.strip("\n")))
    plt.scatter(np.array([i[0] for i in p]),np.array([i[1] for i in p]),color='black')
    plt.show()
    
if __name__=='__main__':
    main()
