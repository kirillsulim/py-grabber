

import re


class TextFormatter:
    def __init__(self):
        self.tag_regex = re.compile(r'<.+?>')
        self.strlen = 80

    def format_text(self, elements):
        res = []
        for el in elements:
            el_str = str(el[1])
            el_str = self.replace_a_to_brackets(el_str)
            el_str = self.cut_all_tags(el_str)
            el_str = self.split_80_chars(el_str)
            res.append(el_str)
            res.append('\n')
            if str(el[0]).startswith('h'):
                res.append('\n')

        return ''.join(res)

    def cut_all_tags(self, string):
        return re.sub(self.tag_regex, '', string)

    def split_80_chars(self, string):
        strings = []

        start = 0
        end = self.strlen

        while end < len(string):
            last_space = string.rfind(' ', start, end)

            if last_space == -1:
                last_space = string.find(' ', start)
                if last_space == -1:
                    break

            strings.append(string[start:last_space])
            strings.append('\n')

            start = last_space + 1
            end = start + self.strlen

        strings.append(string[start:])

        return ''.join(strings)

    def replace_a_to_brackets(self, string):
        string = re.sub(r'<a.+href\s*=\s*[\"\'](.+?)[\"\'].*>(.+)</a>', r'\2[\1]', string)
        string = string.replace('<a>', '[').replace('</a>', ']')
        return string




