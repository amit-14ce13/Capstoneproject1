import json
with open("list1.json") as file:
    data = json.load(file)

def transformVideoData(src,dec="",longdec=""):
    mydict1={"dec":dec,"longdec":longdec,"src":src}
    return  mydict1
for dict in data:
    videoList = []
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        for media in dict["productDetailist"][0]["medias"]:
            if media["mediaType"] == "Video":
                dec = media['title']
                src = media['videoCode']
                mediaNode = transformVideoData(src, dec)
                videoList.append(mediaNode)
    print(videoList)