try:
    import tkinter as tk
    import tkinter.messagebox
except:
    print("[x] tkinter library is missing. Install it using \"pip install tkinter\" or \"apt install python3-tk\".")
    exit()
    
import json

# Import files
import settings
from utils.history import history

class guiutils():
    def histPopOut(self):
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
        #print("Lookup History (Page " + str(pageNum) + ")\n" + )
        tkinter.messagebox.showinfo("Lookup History (Page 1)",str(historyDisplay))

    def createGUI(self,desiredIP,status):
        # GUI Setup
        window = tk.Tk() # Create a window object
        ip_address_txt = tk.Label(
            text = "IP Address: " + desiredIP + "\n"
        ) # Create the IP address label object
        proxy_txt = tk.Label(
            text = "Proxy: " + str(status),
            foreground = "white",
            background = "green"
        ) # Create the proxy status label object
        
        # Set window title
        window.title("ProxyCheck")

        try:
            window.geometry(settings.configdata["resolution"]) 
        except:
            print("[x] Invalid resolution set in settings.json.")
            exit()
        
        histbutton = tk.Button(window, text="History",command=self.histPopOut)
        # Add widget objects
        ip_address_txt.pack()
        proxy_txt.pack()
        histbutton.pack()

        # Keep the window open
        window.mainloop()