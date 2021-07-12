import hashlib

arquivo1 = "texto1.txt"
arquivo2 = "texto2.txt"

hash_arquivo1 = hashlib.new("ripemd160")
hash_arquivo1.update(open(arquivo1, "rb").read()) # "rb" (r = read e b = binary) = leitura no modo binário

hash_arquivo2 = hashlib.new("ripemd160")
hash_arquivo2.update(open(arquivo2, "rb").read())

if hash_arquivo1.digest() != hash_arquivo2.digest():
    print(f"O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}")
else:
    print(f"O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}")

print(f"O hash do arquivo '{arquivo1}' é: {hash_arquivo1.hexdigest()}")
print(f"O hash do arquivo '{arquivo2}' é: {hash_arquivo2.hexdigest()}")