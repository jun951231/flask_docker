import unittest
import os
import numpy as np
import matplotlib.pyplot as plt
from basic.numpy_lib import NumpyLib


class NumpyLibTest(object):

    mock = NumpyLib()

    def show_numpy(self):
        t = np.arange(0, 5, 0.2)
        plt.plot(t, t, 'r--', t,  t**2, 'bs', t, t**3, 'g^')
        plt.show()


    def numpy_choice(self):
        dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
        plt.hist(dice, bins=6)
        plt.show()

    def numpy_not_need_for_loop(self):
        x = np.random.randint(low=10, high=100, size=200) # low, high-None, size=None, dtype=None
        y = np.random.randint(low=10, high=100, size=200)
        size = np.random.randint(100) * 100
        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()


    def indexing_slicing(self):
        a = np.array([1, 2, 3, 4])
        print(f'list -> array: {a}') # [1, 2, 3, 4]
        print(f'indexing a[1] : {a[1]}, indexing a[-1] : {a[-1]}')
        print(f' slicing a[1] : {a[1:]}')


    def array_have_to_one_time(self):
        a = np.array([1, 2, '3', 4])
        print(f'int -> str : {a}')


    def np_zeros(self):
        print(np.zeros(10))


    def np_ones(self):
        print(np.ones(10))


    def np_eye(self):
        print(np.eye(3))


    def np_arange(self):
        print(f'[0 1 2] : {np.arange(3)}')
        print(f'[3 4 5 6] : {np.arange(start=3, stop=7)}')
        print(f'[3 5] : {np.arange(start=3, stop=7, step=2)}')
        print(f'[1.  1.2 1.4 1.6 1.8] : {np.arange(start=1, stop=2, step=0.2)}')


    def np_linspace(self):
        print(f'[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] : {np.linspace(1, 2, 11)}')
        a = np.linspace(1, 2, 11)
        print(f'{np.sqrt(a)}')

    def np_mask(self):
        a = np.arange(-5, 5)
        print(f'mask [-5 -4 -3 -2 -1] : {a[a < 0]}')
        mask1 = abs(a) > 3
        print(f'mask [-5 -4  4] : {a[mask1]}')
        mask2 = abs(a) % 2 == 0
        print(f'mask1 + mask2 {a[mask1 + mask2]}')  # Java에서 // 연산
        print(f'mask1 * mask2 {a[mask1 * mask2]}')  # Java에서 && 연산

    def np_bubble(self):
        x = np.random.randint(-100, 100, 1000)
        y = np.random.randint(-100, 100, 1000)
        size = np.random.randint(100) * 100
        mask1 = abs(x) > 50
        mask2 = abs(y) > 50
        x = x[mask1 + mask2]
        y = y[mask1 + mask2]
        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()


if __name__ == '__main__':
    unittest.main()