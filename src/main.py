import numpy as np
from functools import reduce
import operator as op


def hamming(data):
    data = [i for i, j in enumerate(data) if j]

    return reduce(op.xor, data)


def print_list(list: np.ndarray) -> None:
    print(
        f"[\n  {list[0]},{list[1]},{list[2]},{list[3]},\n  {list[4]},{list[5]},{list[6]},{list[7]},\n  {list[8]},{list[9]},{list[10]},{list[11]},\n  {list[12]},{list[13]},{list[14]},{list[15]}\n]"
    )


data = np.random.randint(0, 2, 16)

print_list(data)

error = hamming(data)
print(f"Error at index: {error}")

data[error] = not data[error]

print("Updated List:")
print_list(data)

error = hamming(data)

print(f"After flipping the bit there are {error} errors")
