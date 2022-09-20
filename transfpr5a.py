import json
with open("list1.json") as file:
    data = json.load(file)

def attachmentdata(attachmentDescription,attachmentLocation, attachmentLongDescription= "", attachmentSequence= ""):
    mydict2 = {"attachmentDescription": attachmentDescription, "attachmentLocation":attachmentLocation, "attachmentLongDescription":attachmentLongDescription
               , "attachmentSequence": attachmentSequence}
    return mydict2
for dict in data:
    attachList = []
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
         for attachment in dict["productDetailist"][0]["literatures"]:
             attachmentDescription = attachment["title"]
             attachmentLocation = attachment["literatureItem"]
             attachmentnode = attachmentdata(attachmentDescription,attachmentLocation )
             attachList.append(attachmentnode)
    print(attachList)
