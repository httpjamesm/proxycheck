import pingparsing, subprocess, json, requests

class utils():
    # Utility
    def get_ipinfo():
        # Get IP address in JSON format
        wtfismyip_r = requests.get('https://wtfismyip.com/json')
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
    # Execution
    currentIP = utils.get_ipinfo()["YourFuckingIPAddress"] # Get IP address and store the IP in a var.
    status = utils.check_isproxy(currentIP) # Check if the IP is a proxy
    if status == True:
        print("Proxy.")
    elif status == "Failed":
        print("An error occured.")
    else:
        print("Not a proxy.")