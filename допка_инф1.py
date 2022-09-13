import requests

cat_params = {'count': 99}

categories = requests.get(f'http://jservice.io/api/categories', params=cat_params)
print('Pick one category and write id:')
for i in categories.json():
    print(f'id: {i["id"]}, title: {i["title"]}')
id_category = int(input())
print('Write amount of questions')
count = int(input())
questions = []
category = requests.get(f'http://jservice.io/api/category', params={'id': id_category}).json()
if category['clues_count'] < count:
    count = category['clues_count']
    print(f'There are only {count} questions in this category')
for i in range(count):
    question = category['clues'][i]['question']
    questions.append(question)
    with open(f'{i}question.txt', 'w', encoding='utf-8') as f:
        f.write(question)
