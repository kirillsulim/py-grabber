import unittest

from textFormatter.TextFormatter import TextFormatter

class TemplateLoaderTest(unittest.TestCase):
    def setUp(self):
        self.formatter = TextFormatter()

    def test_should_cut_tags(self):
        test_data = [
            ('<a> text inside tag </a>', ' text inside tag '),
            ('<div attr="some_attr" /> text <div class="someclass">text inside </div>', ' text text inside ')]

        for test in test_data:
            self.assertEqual(test[1], self.formatter.cut_all_tags(test[0]))

    def test_should_split_more_than_80_chars(self):
        test_data = [
            ("01234567890123456789012345678901234567890123456789012345678901234567890123456789",
             "01234567890123456789012345678901234567890123456789012345678901234567890123456789"),
            ("here_exactly_80_symbols_00000000000000000000000000000000000000000000000000000000 nextword",
             "here_exactly_80_symbols_00000000000000000000000000000000000000000000000000000000\nnextword"),
            ("very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_word next_word",
             "very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_word\nnext_word"),
            ("someword someword someword someword someword someword someword someword somenextword",
             "someword someword someword someword someword someword someword someword\nsomenextword")
        ]

        for test in test_data:
            self.assertEqual(test[1], self.formatter.split_80_chars(test[0]))

    def test_should_replace_links(self):
        test_data = [
            ("<a>www.link.com</a>", "[www.link.com]"),
            ("<a href='www.link.com'>site</a>", "site[www.link.com]"),
            ('<a href="www.link.com">site</a>', "site[www.link.com]"),
            ('some text plus <a class="cla" href = "www.zzz.com" id="12">link</a>', "some text plus link[www.zzz.com]")
        ]

        for test in test_data:
            self.assertEqual(test[1], self.formatter.replace_a_to_brackets(test[0]))


if __name__ == '__main__':
    unittest.main()