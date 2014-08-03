__author__ = 'kir'

import os

class FileSaver:
    def save(self, url, text):
        name = self.create_filename_from_url(url)

        file_dir = self.get_dir_name(name)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        if os.path.exists(name):
            os.remove(name)

        #print(text)

        with open(name, 'w', encoding='utf-8') as file:
            file.write("from: " + url
                       + "\n================================================================================\n")
            file.writelines(text)


    def create_filename_from_url(self, url):

        url = str(url).replace('http://', '').replace('https://', '')
        if url.endswith('/'):
            url = url[:-1]
        return url + ".txt"

    def get_dir_name(self, name):
        index = str(name).rfind('/')
        return name[:index]



