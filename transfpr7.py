import json
with open("list1.json") as file:
    data = json.load(file)
opdictlist = []
#spec = {}
for dict in data:
    #spec = {}
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        for specification in dict["productDetailist"][0]["pdSpecification"]:
            #spec = {}
            group_name = specification["groupName"]
            pValue = specification["primaryDisplayValue"]
            sValue = specification["secondaryDisplayValue"]
            pSymbol = specification["primarySymbol"]
            scSymbol = specification["secondarySymbol"]
            spec1 = specification["specName"]
            if pValue!= None or (sValue!= None and sValue!= ""):
                specDesc = str(pValue)+ str(pSymbol) +str(" " )+str(sValue)+str(scSymbol)
                spec = {}
            #elif pValue!= None and sValue == None:
                #specDesc = str(pValue)+str(pSymbol)

            #text = specification["textValue"]
                if 'Engine' in group_name or 'Power Unit' in group_name:
                    enginedict={specification['specName'] : {'label': specification['specName'],'desc': specDesc}}
                    spec['engine']:enginedict
                elif 'Dimensions' in group_name or 'Capacities' in group_name:
                    dimensiondict={specification['specName'] : {'label': specification['specName'], 'desc': specDesc}}
                    #print(dimensiondict)
                    spec['dimensions']:dimensiondict
                elif 'Transmission System' in group_name or 'Clutch' in group_name or 'drive system' in group_name:
                    drivetraindict={specification['specName'] : {'label': specification['specName'],'desc': specDesc}}
                    spec['drivetrain']:drivetraindict
                elif 'Electrical' in group_name or 'Mill motor' in group_name:
                    electricaldict={specification['specName'] : {'label': specification['specName'],'desc': specDesc}}
                    spec['electrical']:electricaldict
                elif 'Features' in group_name:
                    feList= []
                    feList.append(str(spec1) + str("-") + str(specDesc))
                    print(feList)
                    spec["features"]:feList


                elif 'Option'in group_name:
                    opList = []
                    opList.append(spec1)
                    opList.append(specDesc)
                    spec['options']:opList
                else:
                    operationaldict={specification['specName'] : {'label': specification['specName'],'desc': specDesc}}
                    #opdictlist.append(operationaldict)
                #with open('operational.json', 'w', encoding='utf-8') as file:
                    #json.dump(opdictlist, file, ensure_ascii=False, indent=4)
                    spec['operational']:operationaldict
                #print(spec)





            #list5.append(list6)
    #print(list5)


