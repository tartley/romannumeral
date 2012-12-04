import unittest

from canon import canon

class CanonTest(unittest.TestCase):

    def test_canon_zero(self):
        self.assertEqual(canon(''), '')

    def test_canon_converts_sequence_of_i(self):
        self.assertEqual(canon('i'), 'I')
        self.assertEqual(canon('ii'), 'II')
        self.assertEqual(canon('iii'), 'III')
        self.assertEqual(canon('iiii'), 'IV')

    def test_canon_converts_v_followed_by_sequence_of_i(self):
        self.assertEqual(canon('iv'), 'IV')
        self.assertEqual(canon('v'), 'V')
        self.assertEqual(canon('vi'), 'VI')
        self.assertEqual(canon('vii'), 'VII')
        self.assertEqual(canon('viii'), 'VIII')
        self.assertEqual(canon('viiii'), 'IX')

    def test_canon_teens(self):
        self.assertEqual(canon('ix'), 'IX')
        self.assertEqual(canon('x'), 'X')
        self.assertEqual(canon('xi'), 'XI')
        self.assertEqual(canon('xii'), 'XII')
        self.assertEqual(canon('xiii'), 'XIII')
        self.assertEqual(canon('xiiii'), 'XIV')

        self.assertEqual(canon('xv'), 'XV')
        self.assertEqual(canon('xvi'), 'XVI')
        self.assertEqual(canon('xvii'), 'XVII')
        self.assertEqual(canon('xviii'), 'XVIII')
        self.assertEqual(canon('xviii'), 'XVIII')
        self.assertEqual(canon('xviiii'), 'XIX')

    def test_canon_tens(self):
        self.assertEqual(canon('xx'), 'XX')
        self.assertEqual(canon('xxi'), 'XXI')
        self.assertEqual(canon('xxii'), 'XXII')
        self.assertEqual(canon('xxiii'), 'XXIII')
        self.assertEqual(canon('xxiiii'), 'XXIV')

        self.assertEqual(canon('xxiiii'), 'XXIV')
        self.assertEqual(canon('xxv'), 'XXV')
        self.assertEqual(canon('xxvi'), 'XXVI')
        self.assertEqual(canon('xxvii'), 'XXVII')
        self.assertEqual(canon('xxviii'), 'XXVIII')
        self.assertEqual(canon('xxviiii'), 'XXIX')

        self.assertEqual(canon('liiii'), 'LIV')

        self.assertEqual(canon('xxxxviiii'), 'IL')

    def test_canon_cent(self):
        self.assertEqual(canon('c'), 'C')
        self.assertEqual(canon('ciiii'), 'CIV')

    def test_canon_rules(self):

        # "I" can be subtracted from "V" and "X" only.
        self.assertEqual(canon('xxxviiii'), 'XXXIX')
        
        # "X" can be subtracted from "L" and "C" only.
        self.assertEqual(canon('xxxx'), 'XL')
        self.assertEqual(canon('xxxxv'), 'XLV')
        
        
        self.assertEqual(canon('lxxxviiii'), 'LXXXIX') # 89
        self.assertEqual(canon('lxxxx'), 'XC')
        self.assertEqual(canon('lxxxxi'), 'XCI')

        # "C" can be subtracted from "D" and "M" only.
        # "V", "L", and "D" can never be subtracted

    def test_case(self):
        self.assertEqual(canon('XXXVIIII'), 'XXXIX')

