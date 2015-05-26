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

class TestSpace(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_property(source)
        self.assertEqual(output, expected)

    def test_unparseables(self):
        self.expect('m', 'margin:')

if __name__ == '__main__':
    unittest.main()
