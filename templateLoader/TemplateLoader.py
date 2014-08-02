import json

from templateLoader.ParseTemplate import ParseTemplate


class TemplateLoader:
    def load(self, url):
        name = self.get_name_from_url(url)
        template = self.load_by_name(name)
        return template

    @staticmethod
    def get_name_from_url(url):
        turl = url[:]  # copy
        turl = turl.replace('http://', '')  # delete http
        turl = turl.replace('https://', '')  # delete https

        slash_index = turl.find('/')
        if slash_index != -1:
            turl = turl[:slash_index]
        return turl

    @staticmethod
    def load_by_name(name):
        file = open(name, 'r')
        jsn = json.load(file)

        template = ParseTemplate()
        template.matcher = eval(jsn['matcher'])

        return template
