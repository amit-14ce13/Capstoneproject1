import requests
import json


class MakeApiCall:

    def get_data(self, url):
        # response = requests.get(f"{api}", headers= headers)
        headers = {
            "Accept": "application/json",
            "keyid": "5e5951bf-ebde-443e-a40d-a4e24c4b9103"
        }
        response = requests.get(f"{url}", headers=headers)
        if response.status_code == 200:
            print("sucessfully fetched the data")
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
                        productDetails = list(product["products"])
                        for productDetail in productDetails:
                            productDetailId = productDetail["nodeID"]
                            #print(productDetailId)
                            prductDetailUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/products/"+str(productDetailId)+"?documentculture=en-us&regions=NorthAmerica"
                            pdDetails = list(self.get_data(prductDetailUrl))
                            #print((pdDetails))
                            for pdDetail in pdDetails:
                                eqipId = (pdDetail["equipmentID"])
                                #print(eqipId)
                                pdSpecificationUrl = "https://webapi.vermeer.com/integrations/external/vcom/v1/equipment/"+str(eqipId)+"/specifications?cmsLanguageID=1&displayFilter=0"
                                #print(pdSpecificationUrl)
                                pdSpecification = list(self.get_data(pdSpecificationUrl))
                                print(pdSpecification)



            #print(productLineUrl)

            print("******************************************************")


    # print(length)

    def __init__(self, api):
        self.Central_method(api)


if __name__ == "__main__":
    api_call = MakeApiCall(
        "https://webapi.vermeer.com/integrations/external/vcom/v1/industries?documentculture=en-us&regions=NorthAmerica")
    # api_call1 = MakeApiCall("https://webapi.vermeer.com/integrations/external/vcom/v1/industries/7196?documentculture=en-us&regions=NorthAmerica")