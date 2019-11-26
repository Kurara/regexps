import re


class RegExFormatter():

    def __init__(self, text):
        self.text = text
        
    def has_numbers(self):
        matches = re.search(r'\d+', self.text)
        return matches is not None

    def count_all_words(self):
        found = re.split(r"\s+", self.text)
        return len(found)

    def count_word(self, word):
        """
        Abbiamo usato \W invece di \b perche
        vogliamo prendere anche le parole che afianco,
        possono avere non soltanto uno spazio ma anche
        per esempio: una virgola (')
        """
        found = re.findall("\W+{}\W+".format(word), self.text)
        return len(found)

    def count_word2(self, word):
        """ Same as count_word but case insensitive
        """
        found = re.findall("\W+{}\W+".format(word), self.text, re.IGNORECASE)
        return len(found)

    def has_whole_word(self, word):
        matches = re.search(r'\b{}\b'.format(word), self.text)
        return matches is not None

    def search_followed_by_numbers(self):
        string_founds = []
        for match in re.finditer(r'\b[n,N]el (?=\d+)', self.text):
            string_founds.append({
                match.start(): match.group(0)
            })

        return string_founds

    def sub_starts_with_ma(self, word):
        result = re.subn(r'\bma\S*', word, self.text)
        return result