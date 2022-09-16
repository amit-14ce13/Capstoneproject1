import json
with open("list1.json") as file:
    data = json.load(file)

for dict in data:
    list3 = []
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        for media in dict["productDetailist"][0]["medias"]:
            if media["mediaType"] == "Video":
                dict4 ={"desc": media["title"], "longDesc":"", "src":media["videoCode"]}
                list3.append(dict4)
    print(list3)