import re
import yaml


class RicercaRegex:

    def __init__(self, text):
        self.text = text

    def sostituire_tutti(self, regex, word):
        result = re.subn(regex, word, self.text)
        return result


class RicercaYaml:
    
    def __init__(self, filepath):
        self.filepath = filepath

    def sostituire_tutti(self, regex, word):
        result = []
        with open(self.filepath, 'r') as f:
            list_dict_values = yaml.load(f.read())

        for idx in range(len(list_dict_values)):
            new_dict = {}
            for key, value in list_dict_values[idx].items():
                match = re.subn(regex, word, str(value))
                new_dict[key] = match
            result.append(new_dict)
                

        return result
