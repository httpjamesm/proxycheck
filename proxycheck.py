import json, requests, sys
import tkinter as tk

class utils():
    # Utility
    def get_ipinfo():
        # Get IP address in JSON format
        try:
            wtfismyip_r = requests.get('https://wtfismyip.com/json')
        except:
            return "Failed"
        return wtfismyip_r.json()

    def check_isproxy(ip):
        # Check if the IP is a proxy using Database's proxynet API
        proxynet_r = requests.get('https://api.database.red/v2/proxynet/check?ip=' + ip)
        rawdata = proxynet_r.json()
        # Check raw data
        if rawdata["success"] == True:
            if rawdata["proxy"] == True:
                return True
            return False
        return "Failed"
    
    def forceCheck():
        index = sys.argv.index("--check")
        currentIP = sys.argv[index + 1]
        status = utils.check_isproxy(currentIP)
        return currentIP,status

    def currentIPCheck():
        # Check the current IP
        if utils.get_ipinfo() != "Failed":
            currentIP = utils.get_ipinfo()["YourFuckingIPAddress"] # Get IP address and store the IP in a var.
        else:
            print("[x] Failed to get IP address.")
        status = utils.check_isproxy(currentIP) # Check if the IP is a proxy
        if status == True:
            print("Proxy.\nIP: " + currentIP)
        elif status == False:
            print("Not a proxy.\nIP: " + currentIP)
        else:
            print("An error occured.")

    def createGUI(desiredIP,status):
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
        
        # Add widget objects
        ip_address_txt.pack()
        proxy_txt.pack()
        # Keep the window open
        window.mainloop()

class main():
    #print(sys.argv)
    if len(sys.argv) == 1:
        utils.currentIPCheck()
        exit()
    currentIP = utils.get_ipinfo()["YourFuckingIPAddress"]

    # If --check is supplied as a cli argument
    if "--check" in sys.argv:
        currentIP,ipProxyStatus = utils.forceCheck()
    if "--gui" in sys.argv:
        utils.createGUI(currentIP,utils.check_isproxy(currentIP))
