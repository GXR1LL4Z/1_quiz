import json 

with open('/home/krzysztof/python_ws/1_quiz/nauka_1/test.json') as czynnosc:
    data = json.load(czynnosc)
for n in range(10):
    print(data)