import unittest

from py_grabber.templateLoader.TemplateLoader import TemplateLoader


class TemplateLoaderTest(unittest.TestCase):
    def setUp(self):
        self.loader = TemplateLoader()

    def test_should_parse_name_from_url(self):
        test_data = [
            ('https://docs.python.org/2/library/unittest.html', 'docs.python.org'),
            ('http://www.crummy.com/software/BeautifulSoup/bs4/doc/', 'www.crummy.com'),
            ('http://www.gazeta.ru/politics/2014/08/02_a_6155829.shtml', 'www.gazeta.ru'),
            ('http://abracadabra.ru/fake/link/', 'abracadabra.ru'),
            ('http://abracadabra.ru', 'abracadabra.ru')]
        for test in test_data:
            self.assertEqual(test[1], self.loader.get_name_from_url(test[0]))
