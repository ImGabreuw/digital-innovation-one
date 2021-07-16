import phonenumbers

from phonenumbers import geocoder

numero_telefone = input("Digite o numero_telefone no formato +551140028922: ")

telefone = phonenumbers.parse(numero_telefone)

print(geocoder.description_for_number(telefone, "pt"))
