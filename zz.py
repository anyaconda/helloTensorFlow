# issue: numpy error using venv myTensorflow
# error: DLL library...no module...Cannot Import numpy.core.multiarray
# fix: don't use venv

import numpy as np
print(np.version.version)

import tensorflow as tf
print (tf.__path__)
print (tf.__version__)