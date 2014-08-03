import json
import os.path as path

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
        template_path = "/templates/" + name + ".json"

        template = ParseTemplate()
        if not (path.exists(template_path) and path.isfile(template_path)):
            return template
        else:
            file = open(name, 'r')
            jsn = json.load(file)
            template.matcher = eval(jsn['matcher'])
            return template
