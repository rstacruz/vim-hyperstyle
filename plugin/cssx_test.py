import cssx
import unittest

class TestCr(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_expression(source)
        self.assertEqual(output, expected)

    def test_unparseables(self):
        self.expect('hi', 'hi')

    def test_display_block(self):
        self.expect('db', 'display: block;')

    def test_display_block_with_indent(self):
        self.expect('  db', '  display: block;')

    def test_unparseables_with_indent(self):
        self.expect('  hi', '  hi')

    def test_numeric(self):
        self.expect('m0', 'margin: 0;')

    def test_skip_non_numeric_properties(self):
        self.expect('fs0', 'fs0')

    def _test_numeric_negative(self):
        self.expect('m-1', 'margin: -1px;')

    def _test_numeric_em_short(self):
        self.expect('m2m', 'margin: 2em;')

    def _test_numeric_em(self):
        self.expect('m2em', 'margin: 2em;')

    def _test_numeric_decimal_em(self):
        self.expect('m2.5m', 'margin: 2.5em;')

    def _test_auto_comma(self):
        self.expect('  font-weight: 400', '  font-weight: 400;')

class TestSpace(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_property(source)
        self.assertEqual(output, expected)

    def test_simple(self):
        self.expect('m', 'margin:')



if __name__ == '__main__':
    unittest.main()
