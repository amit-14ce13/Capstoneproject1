from re import sub
import json
with open("list1.json") as file:
    data = json.load(file)

def format_desc(pValue,sValue,pSymbol,scSymbol):
    if pValue != None or (sValue != None and sValue != ""):
        return(str(pValue) + str(pSymbol) + str(" ") + str(sValue) + str(scSymbol))
    #return specDesc
def convert_to_camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])
pdSpec = {}
for dict in data:
    #spec = {}
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        #pdSpec = {}
        for specification in dict["productDetailist"][0]["pdSpecification"]:
            #spec = {}
            group_name = specification["groupName"]
            pValue = specification["primaryDisplayValue"]
            sValue = specification["secondaryDisplayValue"]
            pSymbol = specification["primarySymbol"]
            scSymbol = specification["secondarySymbol"]
            spec1 = specification["specName"]
            spec = format_desc(pValue,sValue,pSymbol,scSymbol)
            label1 = convert_to_camel_case(specification["specName"])
            #pdSpec = {}
            if 'Engine' in group_name or 'Power Unit' in group_name:
                enginedict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                if "engine" not in pdSpec:
                    pdSpec["engine"] = enginedict
                elif "engine" in pdSpec:
                    oldjsn = pdSpec["engine"]
                    oldjsn.update(enginedict)
                    pdSpec["engine"] = oldjsn

            elif 'Dimensions' in group_name or 'Capacities' in group_name:
                 dimensiondict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                 if "dimensions" not in pdSpec:
                     pdSpec["dimensions"] = dimensiondict
                 elif "dimensions" in pdSpec:
                     oldjsn = pdSpec["dimensions"]
                     oldjsn.update(dimensiondict)
                     pdSpec["dimensions"] = oldjsn
                 #print(pdSpec["dimensions"])
            elif 'Transmission System' in group_name or 'Clutch' in group_name or 'drive system' in group_name:
                drivetraindict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                if "drivetrain" not in pdSpec:
                    pdSpec["drivetrain"] = drivetraindict
                elif "drivetrain" in pdSpec:
                    oldjsn = pdSpec["drivetrain"]
                    oldjsn.update(drivetraindict)
                    pdSpec["drivetrain"] = oldjsn

            elif 'electrical' in group_name or 'mill motor' in group_name:
                 electricaldict = {str(label1): {'label': specification['spec_name'],'desc': spec}}
                 if "electrical" not in pdSpec:
                     pdSpec["electrical"] = electricaldict
                 elif "electrical" in pdSpec:
                     oldjsn = pdSpec["electrical"]
                     oldjsn.update(electricaldict)
                     pdSpec["electrical"] = oldjsn

            elif 'Features' in group_name:
                feList = []
                feList.append(str(spec1) + str("-") + str(spec))
                if "features" not in pdSpec:
                    pdSpec["features"] = feList
                elif "features" in pdSpec:
                    oldList = pdSpec["features"]
                    oldList.append(feList)
                    pdSpec["features"] = oldList

                #print(feList)
            elif 'Option' in group_name:
                opList = []
                opList.append(str(spec1) + str("-") + str(spec))
                if "options" not in pdSpec:
                    pdSpec["options"] = opList
                elif "options" in pdSpec:
                    oldList = pdSpec["options"]
                    oldList.append(opList)
                    pdSpec["options"] = oldList

                #print(opList)
            else:
                operationaldict = {str(label1): {'label': specification['specName'], 'desc': spec}}
                if "operational" not in pdSpec:
                    pdSpec["operational"] = operationaldict
                elif "operational" in pdSpec:
                    oldjsn = pdSpec["operational"]

                    oldjsn.update(operationaldict)
                    pdSpec["operational"] = oldjsn

