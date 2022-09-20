import json
from re import sub
transList = []
#pdSpec = {}
class Transform:
    def __init__(self, file):
        self.get_product(file)
    def listData(self,file2):
        with open(file2) as file3:
            data = json.load(file3)
            return data
    def format_desc(self,pValue, sValue, pSymbol, scSymbol,spec = ""):
        if pValue != None or (sValue != None and sValue != ""):
          spec = (str(pValue) + str(pSymbol) + str(" ") + str(sValue) + str(scSymbol))
        return spec

    def convert_to_camel_case(self,s):
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return ''.join([s[0].lower(), s[1:]])
    def get_specData(self,entry):
        #extractData4 = self.listData(file7)
        #for entry in extractData4:
            #if entry["productDetailist"]:
            pdSpec = {}

            for specification in entry["productDetailist"][0]["pdSpecification"]:
                if specification["primaryDisplayValue"]!= None:
                    group_name = specification["groupName"]
                    pValue = specification["primaryDisplayValue"]
                    sValue = specification["secondaryDisplayValue"]
                    pSymbol = specification["primarySymbol"]
                    scSymbol = specification["secondarySymbol"]
                    spec1 = specification["specName"]
                    label1 = self.convert_to_camel_case(specification["specName"])
                    specDesc = self.format_desc(pValue,sValue,pSymbol,scSymbol)
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
                        #print(dimensiondict)
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
            return(pdSpec)

    def get_product(self, file2):
        # pdDict = {}
        extractData1 = self.listData(file2)
        for product in extractData1:
            # pdDict = {}
            if product["productDetailist"]:
                specData = self.get_specData(product)
                transList.append(specData)
                #print(specData)
if __name__ == "__main__":
    transform1 = Transform("list1.json")
    print(transList[-1])