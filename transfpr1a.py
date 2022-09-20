import json
with open("list1.json") as file:
    data = json.load(file)

def generaldata(model,category,subcategory,description,manufacturer="Vermeer",msrp = 0,year = 2021,countries= ["US"]):
    gendict = {"general":{
        "manufacturer":manufacturer,
        "model": model,
        "category": category,
        "subcategory":subcategory,
        "msrp": msrp,
        "description":description,
        "year": year,
        "countries": countries
    }
    }
    return gendict
genList = []
for entry in data:
    if entry["productDetailist"]:
        model = entry["productDetailist"][0]["title"]
        category = entry["industry"]["title"]
        subcategory = entry["product"]["title"]
        description = entry["productDetailist"][0]["description"]
        generalNode = generaldata(model,category,subcategory,description)
        genList.append(generalNode)
print(genList[0])