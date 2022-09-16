import json
with open("list1.json") as file:
    data = json.load(file)

#def transformImgedata(src,dec="",longdec=""):
    #mydict={"dec":dec,"longdec":longdec,"src":src}
    #return  mydict


#dict3 = {}
for dict in data:
    list2 = []
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        for media in dict["productDetailist"][0]["medias"]:
            if media["mediaType"] == "Image":
                dict2 ={"desc": media["title"], "longDesc":"", "src":media["image"]}
                #dict3 = {"dec":"", "longDesc": "", "src": dict["productDetailist"][0]["baseImage"]}
                list2.append(dict2)
        dict3 = {"dec": "", "longDesc": "", "src": dict["productDetailist"][0]["baseImage"]}
        list2.append(dict3)



            #dict3["images"] = dict2
    print(list2)

                #dict2["images"].append({"desc": "","longDesc": "", "src": dict["productDetailist"][0]["baseImage"]})




