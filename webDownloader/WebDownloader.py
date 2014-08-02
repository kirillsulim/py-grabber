#
#
from urllib import request as urlRequest


class WebDownloader:
    def __init__(self):
        pass

    def download_html(self, url):
        """Get html page as a text"""

        page = urlRequest.urlopen(url).read().decode("utf-8")
        return page


    # Add if have time
    def detect_and_decode(self, page):
        temp = str()
        temp += page.decode("ascii")
        temp.find()
        return None

