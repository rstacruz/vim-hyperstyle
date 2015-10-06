import hyperstyle as cssx
from definitions import definitions
import unittest

class TestCr(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_statement(source)
        self.assertEqual(output, expected)

    def test_unparseables(self):
        self.expect('aoeu', None)

    def test_display_block(self):
        self.expect('db', 'display: block')

    def test_ms_units(self):
        self.expect('tdur300', 'transition-duration: 300ms')

    def test_display_block_with_indent(self):
        self.expect('  db', '  display: block')

    def test_double_semicolon(self):
        self.expect('  position: fixed', '  position: fixed')

    def test_dont_expand_p(self):
        self.expect('  p', None)

    def test_mopobo(self):
        self.expect('m0', 'margin: 0')
        self.expect('b0', 'border: 0')
        self.expect('p0', 'padding: 0')

    def test_unparseables_with_indent(self):
        self.expect('  aoeu', None)

    def test_numeric(self):
        self.expect('m0', 'margin: 0')

    def test_z_index(self):
        self.expect('zi0', 'z-index: 0')
        self.expect('z0', 'z-index: 0')

    def _test_multi_numeric(self):
        self.expect('m0 3px', 'margin: 0 3px')

    def test_numeric_with_em_as_default_unit(self):
        self.expect('fs3', 'font-size: 3em')

    def test_numeric_with_unitless_values(self):
        self.expect('lh3', 'line-height: 3')

    def test_numeric_with_unitless_values_and_decimal_point(self):
        self.expect('lh1.5', 'line-height: 1.5')

    def test_numeric_with_implied_unit(self):
        self.expect('w10', 'width: 10px')

    def test_border_0(self):
        self.expect('b0', 'border: 0')

    def test_skip_non_numeric_properties(self):
        self.expect('fw0', None)

    def test_numeric_negative_with_implied_value(self):
        self.expect('w-10', 'width: -10px')

    def test_numeric_em_short(self):
        self.expect('m2m', 'margin: 2em')

    def test_numeric_em_short(self):
        self.expect('m2e', 'margin: 2em')

    def test_numeric_em(self):
        self.expect('m2em', 'margin: 2em')

    def test_numeric_decimal_em(self):
        self.expect('m2.5m', 'margin: 2.5em')

    def test_auto_comma(self):
        self.expect('  font-weight: 400', '  font-weight: 400')

    def test_auto_space(self):
        self.expect('  font-weight:400', '  font-weight: 400')

    def test_auto_space_2(self):
        self.expect('  opacity:1', '  opacity: 1')

    def test_auto_space_unknown_property(self):
        self.expect('  x-y:1', '  x-y: 1')

    def test_autocomplete_values(self):
        self.expect('  float: l', '  float: left')

    def test_flex(self):
        # should not mess with flex: property
        self.expect('flex', 'display: flex')

    def test_flex_grow(self):
        self.expect('fgrow1', 'flex-grow: 1')

    def test_flex_grow_short(self):
        self.expect('fg1', 'flex-grow: 1')

    def test_flex_grow_short(self):
        self.expect('fwrap', 'flex-wrap: wrap')

    def test_expand_units(self):
        self.expect('width: 3', 'width: 3px')

    def test_expand_units_no_space(self):
        self.expect('width:3', 'width: 3px')

    def test_position(self):
        self.expect('abs', 'position: absolute')
        self.expect('rel', 'position: relative')

    def test_z_index_number(self):
        self.expect('z9', 'z-index: 9')

    def test_opacity_number(self):
        self.expect('op0.5', 'opacity: 0.5')

    def test_rtl(self):
        self.expect('rtl', 'direction: rtl')

    def test_zoom_number(self):
        self.expect('zo1', 'zoom: 1')

    def test_font_weights(self):
        self.expect('f1', 'font-weight: 100')
        self.expect('fw1', 'font-weight: 100')
        self.expect('fw100', 'font-weight: 100')
        self.expect('f100', 'font-weight: 100')
        self.expect('under', 'text-decoration: underline')

    def test_misc(self):
        self.expect('oh', 'overflow: hidden')
        self.expect('os', 'overflow: scroll')
        self.expect('mo', 'margin: 0')
        self.expect('moa', 'margin: 0 auto')
        self.expect('fn', 'float: none')
        self.expect('fl', 'float: left')

    def test_leave_selectors_alone(self):
        self.expect('p:before', None)
        self.expect('p:hover', None)
        self.expect('p::placeholder', None)
        self.expect('cursor:w{', None)

class TestSpace(unittest.TestCase):
    def expect(self, source, expected):
        output = cssx.expand_property(source)
        self.assertEqual(output, expected)

    def test_simple(self):
        self.expect('m', 'margin:')

    def test_display(self):
        self.expect('d', 'display:')

    def test_border_right(self):
        self.expect('bri', 'border-right:')

    def test_blacklist_of_br(self):
        # Because `br` is a tag. Use `bri`.
        self.expect('br', None)

    def test_display_fuzzying(self):
        self.expect('dis', 'display:')
        self.expect('disp', 'display:')
        self.expect('displ', 'display:')

    def test_alias_fuzzying(self):
        self.expect('bgcolor', 'background-color:')

    def test_border(self):
        self.expect('bor', 'border:')

    def test_simple_2(self):
        self.expect('tt', 'text-transform:')

    def test_expansion_with_hyphens(self):
        self.expect('border-co', 'border-color:')
        self.expect('borco', 'border-color:')

    def test_font_shortcuts(self):
        self.expect('fow', 'font-weight:')
        self.expect('fw', 'font-weight:')
        self.expect('fos', 'font-size:')
        self.expect('fs', 'font-size:')
        self.expect('fost', 'font-style:')
        self.expect('fst', 'font-style:')
        self.expect('fova', 'font-variant:')
        self.expect('fov', 'font-variant:')
        self.expect('fv', 'font-variant:')
        self.expect('fvar', 'font-variant:')

    def test_padding_shortcuts(self):
        self.expect('pad', 'padding:')
        self.expect('padt', 'padding-top:')
        self.expect('padl', 'padding-left:')
        self.expect('padb', 'padding-bottom:')
        self.expect('padr', 'padding-right:')
        self.expect('padt', 'padding-top:')
        self.expect('padl', 'padding-left:')
        self.expect('padb', 'padding-bottom:')
        self.expect('padr', 'padding-right:')

    def test_margin_shortcuts(self):
        self.expect('mar', 'margin:')
        self.expect('mart', 'margin-top:')
        self.expect('marl', 'margin-left:')
        self.expect('marb', 'margin-bottom:')
        self.expect('marr', 'margin-right:')
        self.expect('mt', 'margin-top:')
        self.expect('ml', 'margin-left:')
        self.expect('mb', 'margin-bottom:')
        self.expect('mr', 'margin-right:')

    def test_border_shortcuts(self):
        self.expect('boc', 'border-color:')
        self.expect('bbo', 'border-bottom:')
        self.expect('bbot', 'border-bottom:')
        self.expect('bto', 'border-top:')
        self.expect('btop', 'border-top:')
        self.expect('bri', 'border-right:')
        self.expect('brig', 'border-right:')
        self.expect('borr', 'border-right:')
        self.expect('bs', 'box-shadow:')
        self.expect('bos', 'box-shadow:')
        self.expect('bot', 'bottom:')
        self.expect('bott', 'bottom:')
        self.expect('borr', 'border-right:')
        self.expect('borl', 'border-left:')
        self.expect('borb', 'border-bottom:')
        self.expect('bortop', 'border-top:')
        self.expect('bort', 'border-top:')
        self.expect('bsh', 'box-shadow:')
        self.expect('bs', 'box-shadow:')
        self.expect('bsi', 'box-sizing:')
        self.expect('bsize', 'box-sizing:')

    def test_misc_shortcuts(self):
        self.expect('tl', 'table-layout:')
        self.expect('ta', 'text-align:')
        self.expect('tb', None)
        self.expect('tc', None)
        self.expect('td', 'text-decoration:')
        self.expect('te', 'text-align:')
        self.expect('tf', 'transform:')
        self.expect('tg', None)
        self.expect('tr', 'transition:')

class TestSelectorLike(unittest.TestCase):
    def expect(self, input, expected):
        output = cssx.is_selectorlike(input)
        self.assertEqual(not not output, expected)

    def test_simple(self):
        self.expect("pad:10", False)

    def test_simple_2(self):
        self.expect("p:10", False)

    def test_before(self):
        self.expect("p:before", True)

class TestExpanders(unittest.TestCase):
    def keyword(self, a, b):
        return cssx.match_keyword(a, b)

    def full(self, prop, val):
        return cssx.expand_full_value(prop, val)

    def test_simple(self):
        self.assertEqual(self.keyword('l', ['left', 'right']), 'left')

    def test_prioritize_prefixes(self):
        self.assertEqual(self.keyword('r', ['lefrt', 'right']), 'right')

    def test_no_matches(self):
        self.assertEqual(self.keyword('x', ['lert', 'right']), None)

    def test_auto_unit(self):
        self.assertEqual(self.full('3', 'margin'), '3px')

    def test_keyword_for_margin(self):
        self.assertEqual(self.full('a', 'margin'), 'auto')

    def test_keyword_for_text_align(self):
        self.assertEqual(self.full('le', 'text-align'), 'left')

    def test_keyword_for_vertical_align(self):
        self.assertEqual(self.full('mid', 'vertical-align'), 'middle')

    def test_expand_unit(self):
        self.assertEqual(self.full('3x', 'margin'), '3px')

    def test_leave_alone(self):
        self.assertEqual(self.full('aoeuaoeu', 'margin'), None)

# TODO:
# - [x] autocompleting values (float: l => float: left)
# - [x] auto-uniting values (margin: 3 => margin: 3px)
# - [ ] better autocompleting values (jc:s => justify-content: flex-start)
# - [ ] multi numeric (m0 3 => margin: 0 3px)

if __name__ == '__main__':
    unittest.main()
