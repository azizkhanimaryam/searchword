from tkinter import *
from be.History import History
from dal.Repository import Repository
import requests
import json

class blWord():
    import requests
    import json

    def GetWord(self, querySearch):
        result = requests.get("https://api.codebazan.ir/vajehyab/?text=آب" + querySearch)
        #result = requests.get(f"https://api.codebazan.ir/vajehyab/?text={querySearch}")


        try:
            parser = json.loads(result.text)
        except json.JSONDecodeError as e:
            print("خطا در تبدیل به JSON:", e)
            return False

        print(parser)  # Debug: See the full response structure

        if "props" in parser and "pageProps" in parser["props"] and "fallback" in parser["props"]["pageProps"]:
            fallback = parser["props"]["pageProps"]["fallback"]
            if querySearch + ":" in fallback:
                data = fallback[querySearch + ":"]
                if "data" in data and "Query" in data["data"]:
                    query_result = data["data"]["Query"]
                    word_box = data["data"].get("WordBox", {})
                    description = word_box.get("Amid", {}).get("description", None)

                    # Create the object only if query_result and description exist
                    return {
                        "Search": query_result,
                        "Text": description
                    }
                else:
                    print("Data structure not as expected:", data)
        return False

           print(result.text)

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

