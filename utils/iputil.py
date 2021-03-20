import json,sys,re,socket

from utils.history import history 

try:
    import requests
except:
    print("[x] Requests library is missing. Install it using \"pip install requests\"")
    exit()

class utils():
    # Main Utility
    def isip(self,ipinput):
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if re.search(regex, ipinput):
            return True
        return False

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
        index = sys.argv.index("--check") # Get index position of the check arg
        try:
            # Try to get the host specified
            self.currentIP = sys.argv[index + 1]
        except:
            print("An IP address is required for \"--check\".")
            exit()
        isip = self.isip(self.currentIP) # Check if the host is an IP address
        if isip == True:
            # If it's an IP address, proceed like normal and supply it to the API
            status = self.check_isproxy(self.currentIP)
            return self.currentIP,status
        # If it's not an IP, get the IP of the domain and supply it to the API
        self.currentIP = socket.gethostbyname(self.currentIP)
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