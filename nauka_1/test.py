import json 

with open('test.json') as czynnosc:
    data = json.load(czynnosc)
for n in range(10):
    print(data)