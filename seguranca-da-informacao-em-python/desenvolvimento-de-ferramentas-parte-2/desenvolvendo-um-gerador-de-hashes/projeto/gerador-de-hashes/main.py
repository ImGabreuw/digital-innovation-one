import hashlib

texto = input("Digite um texto para ser gerado o hash: ")

opcao = int(input(
    """ 
    ### Opções de tipos de hash ###
    
    * MD5 (1)
    * SHA1 (2)
    * SHA256 (3)
    * SHA512 (4)
    """
))

if opcao == 1:
    resultado = hashlib.md5(texto.encode("UTF-8"))
    print(f"O hash MD5 da string é: {resultado.hexdigest()}")
elif opcao == 2:
    resultado = hashlib.sha1(texto.encode("UTF-8"))
    print(f"O hash SHA1 da string é: {resultado.hexdigest()}")
elif opcao == 3:
    resultado = hashlib.sha256(texto.encode("UTF-8"))
    print(f"O hash SHA256 da string é: {resultado.hexdigest()}")
elif opcao == 4:
    resultado = hashlib.sha512(texto.encode("UTF-8"))
    print(f"O hash SHA512 da string é: {resultado.hexdigest()}")
else:
    print("Opção inválida")
