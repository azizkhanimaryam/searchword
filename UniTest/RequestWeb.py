import requests
import json

result=requests.get("https://api.codebazan.ir/vajehyab/?text=نان")

parser=json.loads(result.text)


obj = {"Search": parser["props"]["pageProps"]["fallback"]["نان"+ ":"]["data"]["Query"],
               "Text": parser["props"]["pageProps"]["fallback"]["نان"+ ":"]["data"]["WordBox"]["Amid"][
                   "description"]}


print(obj)

