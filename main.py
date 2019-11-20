import re


class RegExFormatter():

    def __init__(self, text):
        self.text = text
        
    def has_numbers(self):
        matches = re.search(r'\d+', self.text)
        return matches is not None

    def count_all_words(self):
        pass

    def count_word(self, word):
        pass

    def count_word2(self, word):
        """ Same as count_word but case insensitive
        """
        pass

    def has_whole_word(self, word):
        matches = re.search(r'\b{}\b'.format(word), self.text)
        return matches is not None