import json
from re import sub
transList = []
class Transform:
    def __init__(self, file):
        self.get_product(file)
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
    def get_gneralData(self,entry):
        #extractData = self.listData(file1)
        #genList = []
        #for entry in extractData:
            #if entry["productDetailist"]:
                model = entry["productDetailist"][0]["title"]
                category = entry["industry"]["title"]
                subcategory = entry["product"]["title"]
                description = entry["productDetailist"][0]["description"]
                generalNode = self.generalData(model, category, subcategory, description)
                return generalNode
    def transformImgeData(self,src, dec="", longdec=""):
        mydict = {"dec": dec, "longdec": longdec, "src": src}
        return mydict
    def get_ImgeData(self,entry):
        #extractData1 = self.listData(file4)
        #for entry in extractData1:
            Imgelist = []
            #if entry["productDetailist"]:
            src = entry["productDetailist"][0]["baseImage"]
            bseImgNode = self.transformImgeData(src)
            Imgelist.append(bseImgNode)
            for media in entry["productDetailist"][0]["medias"]:
                if media["mediaType"] == "Image":
                    dec = media['title']
                    src = media['image']
                    mediaNode = self.transformImgeData(src, dec)
                    Imgelist.append(mediaNode)
            return Imgelist
    def transformVideoData(self,src, dec="", longdec=""):
        mydict1 = {"dec": dec, "longdec": longdec, "src": src}
        return mydict1
    def get_VideoData(self,entry):
        #extractData2 = self.listData(file5)
        #for entry in extractData2:
            videoList = []
            #if entry["productDetailist"]:
            for media in entry["productDetailist"][0]["medias"]:
                if media["mediaType"] == "Video":
                    dec = media['title']
                    src = media['videoCode']
                    mediaNode = self.transformVideoData(src, dec)
                    videoList.append(mediaNode)
            return videoList

    def attachmentData(self, attachmentDescription, attachmentLocation, attachmentLongDescription="",
                       attachmentSequence=""):
        mydict2 = {"attachmentDescription": attachmentDescription, "attachmentLocation": attachmentLocation,
                   "attachmentLongDescription": attachmentLongDescription, "attachmentSequence": attachmentSequence}
        return mydict2
    def get_attachData(self,entry):
        #extractData3 = self.listData(file6)
        #for entry in extractData3:
            attachList = []
            #if entry["productDetailist"]:
            for attachment in entry["productDetailist"][0]["literatures"]:
                attachmentDescription = attachment["title"]
                attachmentLocation = attachment["literatureItem"]
                attachmentnode = self.attachmentData(attachmentDescription, attachmentLocation)
                attachList.append(attachmentnode)
            return attachList

    def format_desc(self, pValue, sValue, pSymbol, scSymbol, spec=""):
        if pValue != None or (sValue != None and sValue != ""):
            spec = (str(pValue) + str(pSymbol) + str(" ") + str(sValue) + str(scSymbol))
        return spec

    def convert_to_camel_case(self, s):
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return ''.join([s[0].lower(), s[1:]])

    def get_specData(self, entry):
        pdSpec = {}
        for specification in entry["productDetailist"][0]["pdSpecification"]:
            if specification["primaryDisplayValue"] != None:
                group_name = specification["groupName"]
                pValue = specification["primaryDisplayValue"]
                sValue = specification["secondaryDisplayValue"]
                pSymbol = specification["primarySymbol"]
                scSymbol = specification["secondarySymbol"]
                spec1 = specification["specName"]
                label1 = self.convert_to_camel_case(specification["specName"])
                specDesc = self.format_desc(pValue, sValue, pSymbol, scSymbol)
                if 'Engine' in group_name or 'Power Unit' in group_name:
                    enginedict = {str(label1): {'label': specification['specName'], 'desc': specDesc}}
                    if "engine" not in pdSpec:
                        pdSpec["engine"] = enginedict
                    elif "engine" in pdSpec:
                        oldjsn = pdSpec["engine"]
                        oldjsn.update(enginedict)
                        pdSpec["engine"] = oldjsn

                elif 'Dimensions' in group_name or 'Capacities' in group_name:
                    dimensiondict = {str(label1): {'label': specification['specName'], 'desc': specDesc}}
                    if "dimensions" not in pdSpec:
                        pdSpec["dimensions"] = dimensiondict
                    elif "dimensions" in pdSpec:
                        oldjsn = pdSpec["dimensions"]
                        oldjsn.update(dimensiondict)
                        pdSpec["dimensions"] = oldjsn
                    # print(dimensiondict)
                elif 'Transmission System' in group_name or 'Clutch' in group_name or 'drive system' in group_name:
                    drivetraindict = {str(label1): {'label': specification['specName'], 'desc': specDesc}}
                    if "drivetrain" not in pdSpec:
                        pdSpec["drivetrain"] = drivetraindict
                    elif "drivetrain" in pdSpec:
                        oldjsn = pdSpec["drivetrain"]
                        oldjsn.update(drivetraindict)
                        pdSpec["drivetrain"] = oldjsn

                elif 'electrical' in group_name or 'mill motor' in group_name:
                    electricaldict = {str(label1): {'label': specification['spec_name'], 'desc': specDesc}}
                    if "electrical" not in pdSpec:
                        pdSpec["electrical"] = electricaldict
                    elif "electrical" in pdSpec:
                        oldjsn = pdSpec["electrical"]
                        oldjsn.update(electricaldict)
                        pdSpec["electrical"] = oldjsn

                elif 'Features' in group_name:
                    feList = []
                    feList.append(str(spec1) + str("-") + str(specDesc))
                    if "features" not in pdSpec:
                        pdSpec["features"] = feList
                    elif "features" in pdSpec:
                        oldList = pdSpec["features"]
                        oldList.append(feList)
                        pdSpec["features"] = oldList

                    # print(feList)
                elif 'Option' in group_name:
                    opList = []
                    opList.append(str(spec1) + str("-") + str(specDesc))
                    if "options" not in pdSpec:
                        pdSpec["options"] = opList
                    elif "options" in pdSpec:
                        oldList = pdSpec["options"]
                        oldList.append(opList)
                        pdSpec["options"] = oldList

                else:
                    operationaldict = {str(label1): {'label': specification['specName'], 'desc': specDesc}}
                    if "operational" not in pdSpec:
                        pdSpec["operational"] = operationaldict
                    elif "operational" in pdSpec:
                        oldjsn = pdSpec["operational"]
                        oldjsn.update(operationaldict)
                        pdSpec["operational"] = oldjsn
        return (pdSpec)

    def get_product(self,file2):
        #pdDict = {}
        extractData1 = self.listData(file2)
        for product in extractData1:
            #pdDict = {}
            if product["productDetailist"]:
              #pdDict = {}
              genData = self.get_gneralData(product)
              ImgeData = self.get_ImgeData(product)
              vdoData = self.get_VideoData(product)
              attachData = self.get_attachData(product)
              specData = self.get_specData(product)
              pdDict = {"general":genData, "images":ImgeData, "videos":vdoData, "attachments":attachData}
              pdDict.update(specData)
              transList.append(pdDict)
        #print(transList[0])

if __name__ == "__main__":
    transform1 = Transform("list1.json")
    #print(transList[1])
with open('transform.json', 'w', encoding='utf-8') as transfrmfile:
    json.dump(transList, transfrmfile, ensure_ascii=False, indent=4)

