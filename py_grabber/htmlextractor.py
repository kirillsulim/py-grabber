from bs4 import BeautifulSoup


class HtmlExtractor:
    def __init__(self, page):
        """pass page text as a constructor parameter"""
        self.page = page

    def extract(self, template):
        matcher = template.matcher
        if matcher is None:
            matcher = self.default_matcher

        soup = BeautifulSoup(self.page, "html.parser")

        elements = soup.find_all(matcher)

        res = []
        for el in elements:
            res.append((el.name, el))

        return res

    @staticmethod
    def default_matcher(tag):
        return tag.name == 'p' or tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']




