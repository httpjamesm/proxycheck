import tkinter as tk

class guiutils():
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
        # Set window title
        window.title("ProxyCheck")

        window.geometry('250x100') 
        # Keep the window open
        window.mainloop()