import numpy as np

def check_bit(data: np.ndarray):
    overall_parity = data[0]
    parity_1 = data[1]
    parity_2 = data[2]
    parity_3 = data[4]
    parity_4 = data[8]

    print(overall_parity, parity_1, parity_2, parity_3, parity_4)

hamming = np.zeros(16, int)

check_bit(hamming)
