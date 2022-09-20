import json
from re import sub
transList = []
class Transform:
    def __init__(self, file):
        self.get_gneralData(file)
        self.get_ImgeData(file)
        self.get_VideoData(file)
        self.get_attachData(file)
        self.get_specData(file)
    def listData(self,file2):
        with open(file2) as file3:
            data = json.load(file3)
            return data

    def generalData(self,model, category, subcategory, description, manufacturer="Vermeer", msrp=0, year=2021,
                    countries=["US"]):
        gendict =  {
            "manufacturer": manufacturer,
            "model": model,
            "category": category,
            "subcategory": subcategory,
            "msrp": msrp,
            "description": description,
            "year": year,
            "countries": countries
        }

        return gendict
    def get_gneralData(self,file1):
        extractData = self.listData(file1)
        #genList = []
        for entry in extractData:
            if entry["productDetailist"]:
                model = entry["productDetailist"][0]["title"]
                category = entry["industry"]["title"]
                subcategory = entry["product"]["title"]
                description = entry["productDetailist"][0]["description"]
                generalNode = self.generalData(model, category, subcategory, description)
                #genList.append(generalNode)
        #print(genList[0])

    def transformImgeData(self,src, dec="", longdec=""):
        mydict = {"dec": dec, "longdec": longdec, "src": src}
        return mydict
    def get_ImgeData(self,file4):
        extractData1 = self.listData(file4)
        for entry in extractData1:
            Imgelist = []
            if entry["productDetailist"]:
                src = entry["productDetailist"][0]["baseImage"]
                bseImgNode = self.transformImgeData(src)
                Imgelist.append(bseImgNode)
                for media in entry["productDetailist"][0]["medias"]:
                    if media["mediaType"] == "Image":
                        dec = media['title']
                        src = media['image']
                        mediaNode = self.transformImgeData(src, dec)
                        Imgelist.append(mediaNode)

            #print(Imgelist)

    def transformVideoData(self,src, dec="", longdec=""):
        mydict1 = {"dec": dec, "longdec": longdec, "src": src}
        return mydict1
    def get_VideoData(self,file5):
        extractData2 = self.listData(file5)
        for entry in extractData2:
            videoList = []
            if entry["productDetailist"]:
                for media in entry["productDetailist"][0]["medias"]:
                    if media["mediaType"] == "Video":
                        dec = media['title']
                        src = media['videoCode']
                        mediaNode = self.transformVideoData(src, dec)
                        videoList.append(mediaNode)
            #print(videoList)

    def attachmentData(self,attachmentDescription, attachmentLocation, attachmentLongDescription="", attachmentSequence=""):
        mydict2 = {"attachmentDescription": attachmentDescription, "attachmentLocation": attachmentLocation,
                   "attachmentLongDescription": attachmentLongDescription, "attachmentSequence": attachmentSequence}
        return mydict2
    def get_attachData(self,file6):
        extractData3 = self.listData(file6)
        for entry in extractData3:
            attachList = []
            if entry["productDetailist"]:
                for attachment in entry["productDetailist"][0]["literatures"]:
                    attachmentDescription = attachment["title"]
                    attachmentLocation = attachment["literatureItem"]
                    attachmentnode = self.attachmentData(attachmentDescription, attachmentLocation)
                    attachList.append(attachmentnode)
            #print(attachList)

    def format_desc(self,pValue, sValue, pSymbol, scSymbol):
        if pValue != None or (sValue != None and sValue != ""):
            return (str(pValue) + str(pSymbol) + str(" ") + str(sValue) + str(scSymbol)

    def convert_to_camel_case(self,s):
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return ''.join([s[0].lower(), s[1:]])
    def get_specData(self,file7):
        extractData4 = self.listData(file7)
        for entry in extractData4:
            if entry["productDetailist"]:
                for specification in entry["productDetailist"][0]["pdSpecification"]:
                    group_name = specification["groupName"]
                    pValue = specification["primaryDisplayValue"]
                    sValue = specification["secondaryDisplayValue"]
                    pSymbol = specification["primarySymbol"]
                    scSymbol = specification["secondarySymbol"]
                    spec1 = specification["specName"]
                    spec = self.format_desc(pValue, sValue, pSymbol, scSymbol)
                    label1 = self.convert_to_camel_case(specification["specName"])
                    if 'Engine' in group_name or 'Power Unit' in group_name:
                        enginedict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                    elif 'Dimensions' in group_name or 'Capacities' in group_name:
                        dimensiondict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                        print(dimensiondict)
                    elif 'Transmission System' in group_name or 'Clutch' in group_name or 'drive system' in group_name:
                        drivetraindict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                    elif 'Features' in group_name:
                        feList = []
                        feList.append(str(spec1) + str("-") + str(spec))
                        # print(feList)
                    elif 'Option' in group_name:
                        opList = []
                        opList.append(str(spec1) + str("-") + str(spec))
                    else:
                        operationaldict = {str(label1): {'label': specification['specName'], 'desc': spec}}








if __name__ == "__main__":
    transform1 = Transform("list1.json")


