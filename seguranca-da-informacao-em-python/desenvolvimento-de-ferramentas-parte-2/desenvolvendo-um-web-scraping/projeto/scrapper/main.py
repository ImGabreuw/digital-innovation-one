from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, "html.parser")

temperatura = soup.find("p", class_="-gray _flex _align-center")

print(temperatura.string)

# Retorna a primeira tag p da página
print(soup.p)

print(soup.find("admin"))
