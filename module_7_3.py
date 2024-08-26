from typing import Dict


class WordsFinder:
    def __init__(self, *file_names: list):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                cleared_lines = ''.join(
                    char for char in content if char not in (',', '.', '=', '!', '?', ';', ':', ' - '))
                elements = cleared_lines.split()
                all_words = {file_name: elements}
        return all_words

    def find(self, word: str):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            position = words.index(word)
            if word in words:
                result[file_name] = position
        return result

    def count(self, word: str):
        word = word.lower()
        count = 0
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count += words.count(word)
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего




