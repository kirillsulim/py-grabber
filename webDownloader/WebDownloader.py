#
#
from urllib import request as urlRequest

from chardet.universaldetector import UniversalDetector



class WebDownloader:
    def __init__(self):
        pass

    def download_html(self, url):
        """Get html page as a text"""
        html = urlRequest.urlopen(url).read()
        encoding = self.detect_encoding(html)
        page = html.decode(encoding)
        return page


    @staticmethod
    def detect_encoding(html):
        u = UniversalDetector()
        u.feed(html)
        u.close()
        res = u.result['encoding']
        return res


