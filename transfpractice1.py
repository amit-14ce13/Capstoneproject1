import json
with open("list1.json") as file:
    data = json.load(file)
print(data[0])



