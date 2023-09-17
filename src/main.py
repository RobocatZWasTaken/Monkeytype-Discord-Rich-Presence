print("Loading Script")

import time
import requests
from pypresence import Presence
import time
import tkinter as tk
import sys
import threading

APEKEY = None
inputtxt = None
displayError = None
 
def UpdateApeKey():
    global APEKEY
    global inputtxt
    print("Updating Ape Key")
    if inputtxt != None:
        A = inputtxt.get(1.0, "end-1c")
        APEKEY = str(A)
        print("APEKEY: ",APEKEY)
    elif displayError != None:
        displayError.config(text = "MAJOR ERROR HAS OCCURED (Error code 25)")



def ON_CLOSING():
    print("Stopping Script")
    sys.exit()

def Start1():
    global APEKEY
    global inputtxt
    global displayError
    window = tk.Tk()
    window.geometry("250x170")
    window.title("Monkeytype Discord Rich Presence")

    NameTextLabel = tk.Label(text="Monkeytype Discord Rich Presence")

    displayError = tk.Label(text="Status: Unknown")

    my_button = tk.Button(window,
                    text = "Update Ape Key",
                    command = UpdateApeKey)

    # TextBox Creation
    inputtxt = tk.Text(window,
                    height = 5,
                    width = 20)

    NameTextLabel.pack()
    inputtxt.pack()
    my_button.pack()
    displayError.pack()
    window.protocol("WM_DELETE_WINDOW", ON_CLOSING)

    def my_mainloop():
        print("The code is loaded")
        print("Code is looping")
        time.sleep(10)
        client_id = '1030564443249188925'
        RPC = Presence(client_id)
        RPC.connect() # Start the handshake loop
        DetailsValue = "Last Known WPM"

        global APEKEY
        print("Code is running.")
        print(APEKEY)
        if APEKEY != None:
            print("Requesting Data!")
            r = requests.get("https://api.monkeytype.com/results/last", headers={'Authorization': 'ApeKey {value}'.format(value=APEKEY)})
            if r.status_code == 200:
                print(r)
                print(r.json())
                DetailsValue = "Last Known WPM: {wpm}".format(wpm=r.json()['wpm'])
                RPC.update(large_text="Unofficial Monkeytype Rich Presence.",large_image="monkeytype",details=DetailsValue)
            elif r.status_code == 404:
                displayError.config(text = "Status: 404?! (monkeytype api is probably down)")
            elif r.status_code == 472:
                displayError.config(text = "Status: 472?! (not a valid ape key!)")
            else:
                print(r.status_code)
                displayError.config(text = "Status: Error! :)")
                DetailsValue = "Error Fetching WPM"
        else:
            displayError.config(text = "Status: Error! :(")
            print(APEKEY)
            DetailsValue = "Error Fetching WPM"
        RPC.update(large_text="Unofficial Monkeytype Rich Presence.",large_image="monkeytype",details=DetailsValue,buttons=[{"label": "Play", "url": "https://Monkeytype.com"}])
        my_mainloop()

    window.mainloop()

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
        sys.exit()

    def run(self):
        global APEKEY
        global inputtxt
        global displayError
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        NameTextLabel = tk.Label(text="Monkeytype Discord Rich Presence")

        displayError = tk.Label(text="Status: Unknown")

        my_button = tk.Button(self.root,
                    text = "Update Ape Key",
                    command = UpdateApeKey)

        # TextBox Creation
        inputtxt = tk.Text(self.root,
                    height = 5,
                    width = 20)
        
        NameTextLabel.pack()
        inputtxt.pack()
        my_button.pack()
        displayError.pack()

        self.root.mainloop()

    
app = App()

def my_mainloop():
        print("Loaded code made by RobocatZ!")
        while True:
            print("The code is loaded")
            print("Code is looping")
            time.sleep(10)
            client_id = '1030564443249188925'
            RPC = Presence(client_id)
            RPC.connect() # Start the handshake loop
            DetailsValue = "Last Known WPM"

            global APEKEY
            print("Code is running.")
            print(APEKEY)
            if APEKEY != None:
                print("Requesting Data!")
                r = requests.get("https://api.monkeytype.com/results/last", headers={'Authorization': 'ApeKey {value}'.format(value=APEKEY)})
                if r == "200":
                    print(r.json()['data'])
                    DetailsValue = "Last Known WPM: {wpm}".format(wpm=r.json()['data']['wpm'])
                    RPC.update(large_text="Unofficial Monkeytype Rich Presence.",large_image="monkeytype",details=DetailsValue)
                else:
                    print(r)
                    print(r.json()['data'])
                    displayError.config(text = "Status: Success! :)")
                    DetailsValue = "Error Fetching WPM"
                    DetailsValue = "Last Known WPM: {wpm}".format(wpm=r.json()['data']['wpm'])
            else:
                displayError.config(text = "Status: Error! :(")
                print(APEKEY)
                DetailsValue = "Error Fetching WPM"
                RPC.update(large_text="Unofficial Monkeytype Rich Presence.",large_image="monkeytype",details=DetailsValue,buttons=[{"label": "Play", "url": "https://Monkeytype.com"}])

my_mainloop()
