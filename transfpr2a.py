import json
with open("list1.json") as file:
    data = json.load(file)
#Imgelist=[]

def transformImgedata(src,dec="",longdec=""):
    mydict={"dec":dec,"longdec":longdec,"src":src}
    return  mydict
for entry in data:
    Imgelist = []
    if entry["productDetailist"]:
        src = entry["productDetailist"][0]["baseImage"]
        bseImgNode = transformImgedata(src)
        Imgelist.append(bseImgNode)
        for media in entry["productDetailist"][0]["medias"]:
             if media["mediaType"] == "Image":
                dec = media['title']
                src = media['image']
            #if i["mediaType"] == "Image":
                #print(i["title"])
                #dec = i["title"]
                #src = i["image"]
                mediaNode = transformImgedata(src, dec)
                Imgelist.append(mediaNode)
    print(Imgelist)