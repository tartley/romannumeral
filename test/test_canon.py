import unittest

from canon import canon

class CanonTest(unittest.TestCase):

    def test_canon_zero(self):
        self.assertEqual(canon(''), '')

    def test_canon_converts_sequence_of_i(self):
        self.assertEqual(canon('i'), 'i')
        self.assertEqual(canon('ii'), 'ii')
        self.assertEqual(canon('iii'), 'iii')
        self.assertEqual(canon('iiii'), 'iv')

    def test_canon_converts_v_followed_by_sequence_of_i(self):
        self.assertEqual(canon('iv'), 'iv')
        self.assertEqual(canon('v'), 'v')
        self.assertEqual(canon('vi'), 'vi')
        self.assertEqual(canon('vii'), 'vii')
        self.assertEqual(canon('viii'), 'viii')
        self.assertEqual(canon('viiii'), 'ix')

    def test_canon_teens(self):
        self.assertEqual(canon('ix'), 'ix')
        self.assertEqual(canon('x'), 'x')
        self.assertEqual(canon('xi'), 'xi')
        self.assertEqual(canon('xii'), 'xii')
        self.assertEqual(canon('xiii'), 'xiii')
        self.assertEqual(canon('xiiii'), 'xiv')

        self.assertEqual(canon('xv'), 'xv')
        self.assertEqual(canon('xvi'), 'xvi')
        self.assertEqual(canon('xvii'), 'xvii')
        self.assertEqual(canon('xviii'), 'xviii')
        self.assertEqual(canon('xviii'), 'xviii')
        self.assertEqual(canon('xviiii'), 'xix')

    def test_canon_tens(self):
        self.assertEqual(canon('xx'), 'xx')
        self.assertEqual(canon('xxi'), 'xxi')
        self.assertEqual(canon('xxii'), 'xxii')
        self.assertEqual(canon('xxiii'), 'xxiii')
        self.assertEqual(canon('xxiiii'), 'xxiv')

        self.assertEqual(canon('xxiiii'), 'xxiv')
        self.assertEqual(canon('xxv'), 'xxv')
        self.assertEqual(canon('xxvi'), 'xxvi')
        self.assertEqual(canon('xxvii'), 'xxvii')
        self.assertEqual(canon('xxviii'), 'xxviii')
        self.assertEqual(canon('xxviiii'), 'xxix')

        self.assertEqual(canon('liiii'), 'liv')

        self.assertEqual(canon('xxxxviiii'), 'il')

    def test_canon_cent(self):
        self.assertEqual(canon('c'), 'c')
        self.assertEqual(canon('ciiii'), 'civ')

    def test_canon_rules(self):
        self.assertEqual(canon('xxxx'), 'xl')

        # "I" can be subtracted from "V" and "X" only.
        self.assertEqual(canon('xxxxv'), 'xlv')

        # "X" can be subtracted from "L" and "C" only.
        # "C" can be subtracted from "D" and "M" only.
        # "V", "L", and "D" can never be subtracted

