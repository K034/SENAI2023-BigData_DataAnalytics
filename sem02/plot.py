import matplotlib.pyplot as plt 
import numpy as np

# funcao arange (min, max, intervalo)
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)

plt.show ()

plt.savefig('ex_plot.png', format='png')