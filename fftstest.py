import unittest
import ffts

import numpy as np

def relerr(gold, dirt):
    return np.abs(gold - dirt) / np.abs(gold)


class TestDFSR(unittest.TestCase):
    def test8(self):
        N = 8*64
        thresh = np.spacing(1) * 1e4
        for i in range(10):
            x = np.random.randn(N)
            gold = np.fft.fft(x)
            dirt = ffts.fftDFSR(x, N)
            self.assertTrue(max(relerr(gold, dirt)) < thresh)


if __name__ == '__main__':
    unittest.main()


