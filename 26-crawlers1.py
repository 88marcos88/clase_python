import requests

from bs4 import BeautifulSoup

miReq = requests.get("https://python.beispiel.programmierenlernen.io/#")

# print(miReq.status_code)
# print(miReq.headers)


docFinal = BeautifulSoup(miReq.text, "html.parser")

iconos = docFinal.select(".card-text")

print(iconos[0].text)
