import requests
import json

list1 = []
list3 = []


class MakeApiCall:

    def get_data(self, url):
        # response = requests.get(f"{api}", headers= headers)
        headers = {
            "Accept": "application/json",
            "keyid": "5e5951bf-ebde-443e-a40d-a4e24c4b9103"
        }
        response = requests.get(f"{url}", headers=headers)
        if response.status_code == 200:
            #print("sucessfully fetched the data")
            #self.formatted_print(response.json())
            return response.json()
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
            return []

    def Central_method(self, obj):


        industries = list(self.get_data(obj))
        # print(industries)
        length = len(industries)
        for industry in industries:

            nodeId = (industry["nodeID"])
            productLineUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/industries/"+str(nodeId)+"?documentculture=en-us&regions=NorthAmerica"
            productLines = list(self.get_data(productLineUrl))
            for productLine in productLines:
                industryPls = list(productLine["industryProductLines"])
                for industryPl in industryPls:
                    rightNodeId = industryPl["rightNodeId"]
                    #print(rightNodeId)
                    productUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/product-lines/"+str(rightNodeId)+"?documentculture=en-us&regions=NorthAmerica"
                    products = list(self.get_data(productUrl))
                    #print((products))
                    for product in products:
                        #productDetaillist = []
                        productDetails = list(product["products"])
                        for productDetail in productDetails:
                            productDetaillist = []
                            groupNameList= []
                            productDetailId = productDetail["nodeID"]
                            #print(productDetailId)
                            prductDetailUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/products/"+str(productDetailId)+"?documentculture=en-us&regions=NorthAmerica"
                            pdDetails = list(self.get_data(prductDetailUrl))
                            #print((pdDetails))
                            for pdDetail in pdDetails:
                                eqipId = (pdDetail["equipmentID"])
                                #print(eqipId)
                                pdSpecificationUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/equipment/"+str(eqipId)+"/specifications?cmsLanguageID=1&displayFilter=0"
                                pdSpecification = []
                                #print(pdSpecificationUrl)
                                pdSpecification = list(self.get_data(pdSpecificationUrl))
                                if eqipId == 126493:
                                   print(pdSpecification)
                                #grpNameList = []

                                for i in pdSpecification:


                                    grpName= i["groupName"]
                                    specName = i["specName"]
                                    dict2 = {"gN":grpName, "sN": specName}
                                    groupNameList.append(dict2)

                                #print(pdSpecification)
                                pdDetail["pdSpecification"]=pdSpecification
                                productDetaillist.append(pdDetail)
                            dict1 = {}
                            dict1["industry"] = industry
                            dict1["productline"] =productLine
                            dict1["product"] = product
                            dict1["productDetailist"] =productDetaillist
                            list1.append(dict1)
                            list3.append(groupNameList)




            #print(productLineUrl)

            print("******************************************************")


    # print(length)

    def __init__(self, api):
        self.Central_method(api)


if __name__ == "__main__":
    api_call = MakeApiCall(
        "https://webapi.vermeer.com/integrations/external/vcom/v1/industries?documentculture=en-us&regions=NorthAmerica")
    #print(list1[-1])
    #print(len(list1))
    # api_call1 = MakeApiCall("https://webapi.vermeer.com/integrations/external/vcom/v1/industries/7196?documentculture=en-us&regions=NorthAmerica")
with open('list1.json', 'w', encoding='utf-8') as extractfile:
    json.dump(list1, extractfile, ensure_ascii=False, indent=4)
#with open('list3.json', 'w', encoding='utf-8') as file:
    #json.dump(list3, file, ensure_ascii=False, indent=4)
