


class TextFormatter:

    def format_text(self, elements):
        res = str()
        for el in elements:
            res += el[1] + "\n"

        return res
