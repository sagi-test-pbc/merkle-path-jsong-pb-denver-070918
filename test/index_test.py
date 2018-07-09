from unittest import TestCase
from ipynb.fs.full.index import *

class HelperTest(TestCase):

    def test_merkle_path(self):
        i = 7
        total = 11
        want = [7, 3, 1, 0]
        self.assertEqual(merkle_path(i, total), want)
