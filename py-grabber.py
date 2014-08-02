from webDownloader.WebDownloader import WebDownloader
from htmlExtractor.HtmlExtractor import HtmlExtractor


d = WebDownloader()

page = d.download_html("http://www.gazeta.ru/politics/2014/08/02_a_6155829.shtml")

extractor = HtmlExtractor(page)

for e in extractor.extract():
    print(e[1])