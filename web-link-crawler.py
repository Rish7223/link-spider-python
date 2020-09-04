# adding beautifulSoup int he scope
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
       
# bypassing ssl cerificates errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ls = list()
sum = 0

url = input("Enter url: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
print("==================================");
print("Here are the List of LINKS: \n")

for tag in tags:
   links = re.findall('href="([A-Za-z0-9].*)">', str(tag))
   if len(links) > 0:
     data = links[0].split('"')[0]
     if data.startswith("http"):
      print(data)
print("==================================");
   

