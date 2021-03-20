import json,sys,os

class history():
    def write_json(self,data, filename="history.json"):
        # Helper function to write json data to the history file
        with open(filename,'w') as f:
            json.dump(data, f, indent=4)

    def addToHistory(self,host):
        # Add a host lookup to the history file
        with open("history.json") as json_file:
            data = json.load(json_file)
            temp = data["lookups"]
            temp.append(host)
        
        self.write_json(data)

    def createHistFile(self):
        # Create a history file if there is none
        try:
            file = open("history.json", "xt")
        except:
            return
        
        emptydict = {
            "lookups":[]
        }
        self.write_json(emptydict)
    
    def viewHistory(self, pageNum=None):
        if pageNum == None:
            # Get page number by looking at the text right after the --history argument
            index = sys.argv.index("--history")
            try:
                pageNum = sys.argv[index + 1]
            except:
                # if no page number was provided, just set it to 1.
                pageNum = 1

        # Load the history file
        histfile = open('history.json','r')
        # Load the json from the history file
        file = json.load(histfile)
        # Store all the history
        allHistory = file["lookups"]
        # Truncate the history for pagination
        first15Items = allHistory[int(pageNum)*15-15:int(pageNum)*15]
        counter = 1
        historyDisplay = []
        for x in first15Items:
            # Format the history items so they are enumerated
            historyDisplay.append(str(counter) + ". " + x)
            counter += 1
        historyDisplay = "\n".join(historyDisplay)
        print("Lookup History (Page " + str(pageNum) + ")\n" + str(historyDisplay))
    
    def clearHistory(self):
        # Delete the history file
        os.remove("history.json")
        print("[v] History cleared successfully.")
