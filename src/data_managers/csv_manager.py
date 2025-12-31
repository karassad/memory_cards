import os
import csv
import random

class CSVManager:

    """Загрузка слов из csv файла"""

    def __init__(self, data_file_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, "..", "data", data_file_name)

        self.words = self._load_words()

    def _load_words(self):
        words = {}

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                reader.fieldnames = [name.strip() for name in reader.fieldnames]

                for row in reader:
                    key = row.get('word', '').strip()
                    value = row.get('translation', '').strip()
                    words[key] = value
                return words

        except Exception as e:
            print(e)

    def get_random_word(self):
        word = random.choice(list(self.words.keys()))
        return word, self.words[word]



