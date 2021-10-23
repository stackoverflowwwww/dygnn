import networkx as nx
import numpy as np
g=nx.from_edgelist(np.array([[0,1],[0,2],[1,3],[1,0]]),create_using=nx.DiGraph)
print(g.edges)
print(len(g.edges))
#%%
import numpy as np
correct=np.loadtxt("correct.txt")
#%%
correct=correct.astype(np.int)
#%%
np.savetxt("correct.txt",correct,fmt="%d")
#%%
error=np.loadtxt("error.txt")
np.savetxt("error.txt",error,fmt="%d")


