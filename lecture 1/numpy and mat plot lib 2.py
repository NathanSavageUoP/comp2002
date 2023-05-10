import numpy as np
import matplotlib.pyplot as plt

uniform = np.random.rand(100)
normal = np.random.randn(100)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.set_title('Uniform')
ax1.boxplot(uniform)

ax2.set_title('Normal')
ax2.boxplot(normal)

fig.show()