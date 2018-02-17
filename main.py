import scipy.io
mat = scipy.io.loadmat('data/digits-train.mat')

import matplotlib.pyplot as plt
import numpy as np
x = np.array(mat['images_train'][:,0])
print(x.shape)
plt.imshow(x.reshape(28,28))
plt.show()