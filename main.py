import numpy as np
import random
import matplotlib.pyplot as plt
size=30
lattice = []
row= []
def lattice(size):
    rows=[]
    cols=[]
    
    for j in range(size):
        rows=[]
        for i in range(size):
            
            if random.random()<0.5:
                rows.append(1)
            else:
                rows.append(-1)
    
        cols.append(rows)
    
    return cols

        

    
    
latt=lattice(size)

def deltaU(i,j):
    
    if i==0:
        top=latt[size-1][j]
    else:
        top= latt[i-1][j]
    if i==(size-1):
        bottom = latt[0][j]
    else:
        bottom = latt[i+1][j]
    if j==0:
        left=latt[i][size-1]
    else:
        left=latt[i][j-1]
    if j==(size-1):
        right=latt[i][0]
    else:
        right=latt[i][j+1]
    Ediff=2*(latt[i][j])*(top+bottom+right+left)
    return Ediff
  
  def iteration(T):
    for n in range(0,1000*size**2):
        i=int(random.random()*size)
        j=int(random.random()*size)
        if deltaU(i,j) <= 0:
            latt[i][j]=-latt[i][j]
        else:
            if random.random()< np.exp(-(deltaU(i,j))/T):
                latt[i][j]=-latt[i][j]
    return latt

  fig, axes = plt.subplots(3, 3, figsize=(8,8))
ax = axes[0][0]
ax.imshow(iteration(10))
ax.set_xlabel('T=10')
ax = axes[0][1]
ax.imshow(iteration(8))
ax.set_xlabel('T=8')
ax = axes[0][2]
ax.imshow(iteration(6))
ax.set_xlabel('T=6')
ax = axes[1][0]
ax.imshow(iteration(4))
ax.set_xlabel('T=4')
ax = axes[1][1]
ax.imshow(iteration(3))
ax.set_xlabel('T=3')
ax = axes[1][2]
ax.imshow(iteration(2))
ax.set_xlabel('T=2')
ax = axes[2][0]
ax.imshow(iteration(1))
ax.set_xlabel('T=1')
ax = axes[2][1]
ax.imshow(iteration(0.5))
ax.set_xlabel('T=0.5')
ax = axes[2][2]
ax.imshow(iteration(0.2))
ax.set_xlabel('T=0.2')

fig.tight_layout()
fig.suptitle('Lattice VS Temperature', y=1.03, fontsize=25)
plt.show()
