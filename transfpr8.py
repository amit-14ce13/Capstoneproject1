import json
with open("list1.json") as file:
    data = json.load(file)
#fealist= []
for dict in data:
    #spec = {}
    pdlist = dict["productDetailist"]
    if (len(pdlist)!= 0):
        for specification in dict["productDetailist"][0]["pdSpecification"]:
            spec = {}
            group_name = specification["groupName"]
            pValue = specification["primaryDisplayValue"]
            sValue = specification["secondaryDisplayValue"]
            pSymbol = specification["primarySymbol"]
            scSymbol = specification["secondarySymbol"]
            spec1 = specification["specName"]
            if pValue!= None or (sValue!= None and sValue!= ""):
                specDesc = str(pValue)+ str(pSymbol) +str(" ") +str(sValue)+str(scSymbol)

                if 'Features' in group_name:
                    #spec = {}
                    feList= []
                    feList.append(str(spec1)+ str("-")+ str(specDesc))
                    #fealist.append(feList)
                    spec = {"features":feList}
                    print(spec)