import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")
# req2 = requests.get("https://www")
soup = BeautifulSoup(req.content,"html.parser")
# soup2 = BeautifulSoup(req2.content,"html.parser")
# res2 = soup2.get_text
res = soup.get_text
print(res)
print(soup.title)