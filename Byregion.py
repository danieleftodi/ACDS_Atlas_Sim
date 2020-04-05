import requests
import json
import pandas as pd
from json2xml import json2xml

class SWEDGovCoronaAPI:
    def __init__(self):
        self.OCasecountsDaily='https://api.apify.com/v2/key-value-stores/8mRFdwyukavRNCr42/records/LATEST?disableRedirect=true'
        self.OCasecountsAll='https://api.apify.com/v2/datasets/Nq3XwHX262iDwsFJS/items?format=json&clean=1'
AllApi=SWEDGovCoronaAPI()

class SWEDCovid19:
    def ByregionCountDaily(oparam='JSON'):
        TotalCaseCount=requests.get(AllApi.OCasecountsDaily)
        TotalCaseCount=json.loads(TotalCaseCount.content)
        if oparam=='JSON':
            #for region in TotalCaseCount["infectedByRegion"]: 
            #    alist=(region['region'],region['infectedCount'],region['deathCount'],region['intensiveCareCount'])
            #    print(alist)
                return TotalCaseCount["infectedByRegion"]
        elif oparam=='DF':
            return pd.DataFrame(TotalCaseCount['infectedByRegion'])
        
        else:
            return 'Param missing'
    def ByregionCountAll(oparam='JSON'):
        TotalCaseCount=requests.get(AllApi.OCasecountsAll)
        TotalCaseCount=json.loads(TotalCaseCount.content)
        store_list = []
        for item in TotalCaseCount:
            store_list.append(item)
            
        if oparam=='JSON':
            #for region in TotalCaseCount["infectedByRegion"]: 
            #    alist=(region['region'],region['infectedCount'],region['deathCount'],region['intensiveCareCount'])
            #print(item["infectedByRegion"])
            #print(store_list[6])
                return store_list
        elif oparam=='DF':
            return pd.DataFrame(store_list)
        
        else:
            return 'Param missing'        
#print (SWEDCovid19.ByregionCountDaily('JSON'))
#print (SWEDCovid19.ByregionCountDaily('DF'))
#print (SWEDCovid19.ByregionCountAll('JSON'))
#print (SWEDCovid19.ByregionCountAll('DF'))