import webbrowser

# print("Opening web browser")
# webbrowser.open("http://google.com")

import requests
r = requests.get("http://google.com")
print(r)