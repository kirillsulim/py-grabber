from py_grabber.webdownloader import WebDownloader
from py_grabber.htmlextractor import HtmlExtractor
from py_grabber.textformatter import TextFormatter
from py_grabber.filesaver import FileSaver
from py_grabber.templates import TemplateLoader


class Application:
    def run(self, url):
        #download page
        page = WebDownloader().download_html(url)

        #get templates_dir if exists
        template = TemplateLoader().load(url)

        #extract elements
        elements = HtmlExtractor(page).extract(template)

        #format text
        text = TextFormatter().format_text(elements)

        #save to file
        FileSaver().save(url, text)



