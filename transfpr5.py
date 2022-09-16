import json
with open("list1.json") as file:
    data = json.load(file)

for dict in data:
    list4 = []
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
         for attachment in dict["productDetailist"][0]["literatures"]:
             dict5 = {"attachmentDescription": attachment["title"], "attachmentLocation": attachment["literatureItem"],
                      "attachmentLongDescription": "", "attachmentSequence": ""}
             list4.append(dict5)
    print(list4)
