import json, sys

from utils.iputil import utils
from utils.guiutil import guiutils
from utils.history import history

class main():
    history().createHistFile()
    if len(sys.argv) == 1:
        utils().currentIPCheck()
        # Add to history file
        history().addToHistory(utils().get_ipinfo()["YourFuckingIPAddress"])
        exit()
    currentIP = utils().get_ipinfo()["YourFuckingIPAddress"]

    # CLI Arguments
    if "--check" in sys.argv:
        currentIP,ipProxyStatus = utils().forceCheck()
        if "--gui" not in sys.argv:
            if ipProxyStatus == True:
                print("Proxy.")
            elif ipProxyStatus == False:
                print("Not a proxy.")
            else:
                print("An error occured.")
            print("IP Address:",currentIP)
    if "--gui" in sys.argv:
        print("Loading GUI...")
        guiutils().createGUI(currentIP,utils().check_isproxy(currentIP))
    
    if "--clear-history" in sys.argv:
        history().clearHistory()
        exit()
    if "--history" in sys.argv:
        history().viewHistory()
        exit()
    # Add the lookup to the history json file
    history().addToHistory(currentIP)
    