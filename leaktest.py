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

class main():
    # Main app
    if utils.get_ipinfo() != "Failed":
        currentIP = utils.get_ipinfo()["YourFuckingIPAddress"] # Get IP address and store the IP in a var.
    else:
        print("[x] Failed to get IP address.")
    status = utils.check_isproxy(currentIP) # Check if the IP is a proxy
    if status == True:
        print("Proxy.\nIP: " + currentIP)
        color = "green"
    elif status == False:
        print("Not a proxy.\nIP: " + currentIP)
        color = "red"
    else:
        print("An error occured.")
        color = "red"

    # If --gui is supplied as a cli argument
    if "--gui" in sys.argv:
        # GUI Setup
        window = tk.Tk() # Create a window object
        ip_address_txt = tk.Label(
            text = "IP Address: " + currentIP + "\n"
        ) # Create the IP address label object
        proxy_txt = tk.Label(
            text = "Proxy: " + str(status),
            foreground = "white",
            background = color
        ) # Create the proxy status label object
        
        # Add widget objects
        ip_address_txt.pack()
        proxy_txt.pack()
        # Keep the window open
        window.mainloop()