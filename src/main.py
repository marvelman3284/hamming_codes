import numpy as np
from functools import reduce
import operator as op


def hamming(data):
    data = [i for i, j in enumerate(data) if j]

    return reduce(op.xor, data)


data = np.random.randint(0, 2, 16)

print(data)

error = hamming(data)
print(error)

data[error] = not data[error]

error = hamming(data)

print(error)
