from urllib.error import HTTPError
import errno
import sys

from py_grabber.webdownloader import WebDownloader
from py_grabber.htmlextractor import HtmlExtractor
from py_grabber.textformatter import TextFormatter
from py_grabber.filesaver import FileSaver
from py_grabber.templates import TemplateLoader


class Application:
    def run(self, url):
        try:
            page = WebDownloader().download_html(url)
            print('Page downloaded')
        except HTTPError:
            print('Cannot download page')
            sys.exit(errno.EHOSTUNREACH)

        try:
            template = TemplateLoader().load(url)
            elements = HtmlExtractor(page).extract(template)
            text = TextFormatter().format_text(elements)

            FileSaver().save(url, text)
            print('Page saved to file')
        except Exception as e:
            print('Some error occures. Try to save error info...')

            filename = 'error.txt'
            with open(filename) as efile:
                print(e, file=efile)
                print('Error info saved to', filename)

            sys.exit(errno.EHOSTUNREACH)




