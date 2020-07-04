import hashlib
import  json

def generator(file):
    dict = {}
    counter = 1
    with open(file, encoding='utf-8') as fi:
        res = json.load(fi)
    for item in res:
        dict['country'] = item['country']
        hash_lib = hashlib.md5(b'item["url"]')
        dict['url'] = hash_lib.hexdigest()
        yield f'{counter}) {dict}'
        counter += 1


file = 'countru.json'

for i in generator(file):
    print(i)

