


from webDownloader.WebDownloader import WebDownloader
from htmlExtractor.HtmlExtractor import HtmlExtractor
from textFormatter.TextFormatter import TextFormatter
from fileSaver.FileSaver import FileSaver
from templateLoader.TemplateLoader import TemplateLoader


class Application:
    def run(self, url):
        #download page
        page = WebDownloader().download_html(url)

        #get templates if exists
        template = TemplateLoader().load(url)

        #extract elements
        elements = HtmlExtractor(page).extract(template.matcher)

        #format text
        text = TextFormatter().format_text(elements)

        #save to file
        FileSaver().save(url, text)



