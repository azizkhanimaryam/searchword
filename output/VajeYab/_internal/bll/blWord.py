from tkinter import *
from be.History import History
from dal.Repository import Repository
import requests
import json

class blWord():
    def GetWord(self, querySearch):
        result = requests.get("https://api.codebazan.ir/vajehyab/?text=" + querySearch)
        parser = json.loads(result.text)
        print(parser["props"])
        if parser["props"]["pageProps"]["fallback"][querySearch + ":"] == {'error': 'not_allowed'}:
            # messagebox.showerror("خطا","واژه یافت نشد")
            return False
        else:
            #print({"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],"Text": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["WordBox"]["Amid"]})
            #print({"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],"Text": None})
            if {"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],"Text": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["WordBox"]["Amid"]}!={"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],"Text": None}:
                obj = {"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],
                       "Text": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["WordBox"]["Amid"]["description"]}
                return obj
            else:
                # messagebox.showerror("خطا", "واژه یافت نشد")
                return False


    def SaveHistory(self,obj):
        repso=Repository()
        print(obj.hs_Title)
        if obj.hs_Title != "":
            result = repso.Add(obj)
            return result

    def GetDataHistory(self):
        repso = Repository()
        return repso.Read(History)

    def GetDataById(self,id):
        repso = Repository()
        return repso.ReadById(History,id)

    def DeleteRow(self,id):
        repso = Repository()
        obj=repso.ReadById(History,id)
        return repso.Delete(obj)

