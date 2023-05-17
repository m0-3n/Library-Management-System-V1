from bs4 import BeautifulSoup
import requests

barcode = "9780996637503"

url = "https://isbndb.com/book/" + barcode

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
tag = doc.find_all("td")[0]
print(tag.string)

