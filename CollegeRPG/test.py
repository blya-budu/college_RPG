import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data['prologue'][0]['question'])