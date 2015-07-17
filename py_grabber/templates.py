import json
import os
from urllib.request import urlretrieve


GITHUB_TEMPLATES_URL = "https://raw.githubusercontent.com/kirillsulim/py-grabber/master/templates/"

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
        turl = url[:]
        turl = turl.replace('http://', '')
        turl = turl.replace('https://', '')

        slash_index = turl.find('/')
        if slash_index != -1:
            turl = turl[:slash_index]
        return turl

    @staticmethod
    def load_by_name(name):
        name += ".json"
        templates_dir = os.path.expanduser(os.path.join("~", "py-grabber", "templates"))
        os.makedirs(templates_dir, exist_ok=True)

        template_path = os.path.join(templates_dir, name)
        template = ParseTemplate()
        if not (os.path.exists(template_path) and os.path.isfile(template_path)):
            try:
                TemplateLoader.load_from_github(name, template_path)
            except:
                pass

        if not (os.path.exists(template_path) and os.path.isfile(template_path)):
            return template
        else:
            file = open(template_path, 'r')
            jsn = json.load(file)
            template.matcher = eval(jsn['matcher'])
            return template

    @staticmethod
    def load_from_github(name, file):
        url = GITHUB_TEMPLATES_URL + name
        urlretrieve(url, file)
