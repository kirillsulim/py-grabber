import json
import os


class ParseTemplate:
    def __init__(self):
        self.matcher = None


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
        template_path = os.path.expanduser(os.path.join("~", "py-grabber", "templates", name + ".json"))

        template = ParseTemplate()
        if not (os.path.exists(template_path) and os.path.isfile(template_path)):
            return template
        else:
            file = open(template_path, 'r')
            jsn = json.load(file)
            template.matcher = eval(jsn['matcher'])
            return template