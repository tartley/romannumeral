import unittest

from canon import canon

class CanonTest(unittest.TestCase):

    def test_canon_zero(self):
        self.assertEqual(canon(''), '')

    def test_canon_puts_in_i_before_v(self):
        self.assertEqual(canon('i'), 'i')
        self.assertEqual(canon('ii'), 'ii')
        self.assertEqual(canon('iii'), 'iii')
        self.assertEqual(canon('iiii'), 'iv')

