import numpy as np
import matplotlib.pyplot as plt

x = np.array(np.arange(10))
y = np.array(x ** 2)
plt.pie(x, y)
plt.show()