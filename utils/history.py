import json

class history():
    def write_json(self,data, filename="history.json"):
        with open(filename,'w') as f:
            json.dump(data, f, indent=4)

    def addToHistory(self,host):
        with open("history.json") as json_file:
            data = json.load(json_file)
            temp = data["lookups"]
            temp.append(host)
        
        self.write_json(data)

    def createHistFile(self):
        try:
            file = open("history.json", "xt")
        except:
            return
        
        emptydict = {
            "lookups":[]
        }
        self.write_json(emptydict)