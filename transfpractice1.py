import json
with open("list1.json") as file:
    data = json.load(file)
#print(data[0])
genList = []
for entry in data:
    if entry["productDetailist"]:
        dict2 = {"general": {
            "manufacturer": "Vermeer",
            "model": entry["productDetailist"][0]["title"],
            "category": entry["industry"]["title"],
            "subcategory": entry["product"]["title"],
            "msrp": 0,
            "description": entry["productDetailist"][0]["description"],
            "year": 2021,
            "countries": [
                "US"
            ]
        }
        }
        genList.append(dict2)
print(genList[1])




