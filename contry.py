# Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.
import json

def get_country(file):
    country = []
    for item in file:
        a = item['name']['common'].replace(' ', '_')
        country.append(a)
    return country

class Iteration_country:

    def __init__(self, file):
        self.file = file
        with open(self.file, encoding='utf-8') as f:
            self.country = json.load(f)
        self.countries = get_country(self.country)
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        URL = 'https://ru.wikipedia.org/wiki/'
        if self.count == len(self.countries)-1:
            raise StopIteration
        self.count += 1
        dic = {}

        dic['country'] = self.countries[self.count]
        dic['url'] = URL + self.countries[self.count]
        return dic


sas = Iteration_country('countries.json')
print(sas)

country_list = []

for i in sas:
    country_list.append(i)

with open('countru.json', 'w', encoding='utf-8') as f:
    json.dump(country_list, f, ensure_ascii=False, indent=2)

