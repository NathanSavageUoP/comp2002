import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi)
Y = np.sin(X)

fig, ax = plt.subplots()
ax.plot(X, Y)

fig.show()