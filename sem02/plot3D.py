import numpy as np
import matplotlib.pyplot as plt

alpha = 0.7
phi_ext = 2*np.pi*0.5

def ColorMap(phi_m, phi_p):
    return (+ alpha -2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext -2*phi_p) )

# comentário sobre a comparação do uso do comando linspace e arange
phi_m = np.linspace(0, 2*np.pi, 200)
phi_p = np.linspace(0, 2*np.pi, 200)

# meshgrid é comando para junção dos grids, no caso, phi_m e phi_p para formar uma superficie 
X,Y = np.meshgrid(phi_p, phi_m)

# transposicao dos eixos da matriz
Z = ColorMap(X,Y).T

fig = plt.figure( figsize =(8,6))

ax = fig.add_subplot(1,1,1, projection ='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

plt.show()

plt.savefig('ex_plot3D.png', format='png')