import unittest
from add import add, order

class TestOrder(unittest.TestCase):
    def test_basic_order(self):
        self.assertEqual(
            order('XI'),
            'XI'
        )

class TestAdd(unittest.TestCase):

    def test_simple_adds(self):
        self.assertEqual(
            add('I', 'I'),
            'II'
        )

        self.assertEqual(
            add('I', 'II'),
            'III'
        )
        self.assertEqual(
            add('II', 'II'),
            'IIII'
        )

    def test_v(self):
        self.assertEqual(
            add('III', 'II'),
            'V'
        )
        self.assertEqual(
            add('V', 'I'),
            'VI'
        )
        self.assertEqual(
            add('V', 'II'),
            'VII'
        )

    def test_x(self):
        self.assertEqual(
            add('V', 'V'),
            'X'
        )


    def test_too_many_symbols(self):
        self.assertEqual(
            add('IIIII', 'I'),
            'VI'
        )
        self.assertEqual(
            add('VVV', 'I'),
            'XVI'
        )


    def test_ordering(self):
        self.assertEqual(
            add('I', 'V'),
            'VI'
        )
        self.assertEqual(
            add('I', 'X'),
            'XI'
        )
        self.assertEqual(
            add('V', 'X'),
            'XV'
        )
        self.assertEqual(
            add('V', 'VIII'),
            'XIII'
        )
        print 'our test' * 10
        self.assertEqual(
            add('V', 'XVVV'),
            'XXX'
        )
        self.assertEqual(
            add('I', 'VV'),
            'XI'
        )
        self.assertEqual(
            add('X', 'V'),
            'XV'
        )
        self.assertEqual(
            add('XI', 'V'),
            'XVI'
        )
        self.assertEqual(
            add('X', 'L'),
            'LX'
        )

    def test_L(self):
        self.assertEqual(
            add('L', 'II'),
            'LII'
        )
        self.assertEqual(
            add('XXXX', 'X'),
            'L'
        )


if __name__ == '__main__':
    unittest.main()
