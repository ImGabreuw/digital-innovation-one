import re
import json

from urllib.request import urlopen

url = "https://ipinfo.io/json"

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados["ip"]
org = dados["org"]
cidade = dados["city"]
pais = dados["country"]
regiao = dados["region"]

print(f"""
Detalhes do IP externo: 

IP: {ip}
Região: {regiao}
Cidade: {cidade}
País: {pais}
Organização: {org}
""")
