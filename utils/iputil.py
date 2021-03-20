import json,sys

from utils.history import history 

try:
    import requests
except:
    print("[x] Requests library is missing. Install it using \"pip install requests\"")
    exit()

class utils():
    # Main Utility
    def get_ipinfo(self):
        # Get IP address in JSON format
        try:
            wtfismyip_r = requests.get('https://wtfismyip.com/json')
        except:
            return "Failed"
        return wtfismyip_r.json()

    def check_isproxy(self,ip):
        # Check if the IP is a proxy using Database's proxynet API
        proxynet_r = requests.get('https://api.database.red/v2/proxynet/check?ip=' + ip)
        rawdata = proxynet_r.json()
        # Check raw data
        if rawdata["success"] == True:
            if rawdata["proxy"] == True:
                return True
            return False
        return "Failed"
    
    def forceCheck(self):
        index = sys.argv.index("--check")
        try:
            self.currentIP = sys.argv[index + 1]
        except:
            print("An IP address is required for \"--check\".")
            exit()
        status = self.check_isproxy(self.currentIP)
        return self.currentIP,status

    def currentIPCheck(self):
        # Check the current IP
        if self.get_ipinfo() != "Failed":
            currentIP = self.get_ipinfo()["YourFuckingIPAddress"] # Get IP address and store the IP in a var.
        else:
            print("[x] Failed to get IP address.")
            return
        status = self.check_isproxy(currentIP) # Check if the IP is a proxy
        if status == True:
            print("Proxy.\nIP: " + currentIP)
        elif status == False:
            print("Not a proxy.\nIP: " + currentIP)
        else:
            print("An error occured.")
    
    def defaultCmd(self):
        self.currentIPCheck()
        # Add to history file
        history().addToHistory(utils().get_ipinfo()["YourFuckingIPAddress"])