


from py_grabber.webDownloader import WebDownloader
from py_grabber.htmlExtractor import HtmlExtractor
from py_grabber.textFormatter import TextFormatter
from py_grabber.fileSaver import FileSaver
from py_grabber.templateLoader import TemplateLoader


class Application:
    def run(self, url):
        #download page
        page = WebDownloader().download_html(url)

        #get templates if exists
        template = TemplateLoader().load(url)

        #extract elements
        elements = HtmlExtractor(page).extract(template)

        #format text
        text = TextFormatter().format_text(elements)

        #save to file
        FileSaver().save(url, text)



