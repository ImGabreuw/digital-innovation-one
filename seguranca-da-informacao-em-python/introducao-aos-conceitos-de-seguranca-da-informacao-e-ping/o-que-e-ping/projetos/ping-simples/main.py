import os

print("#" * 60)

ip_ou_host = input("Digite o IP ou host a ser verificado: ")

print("-" * 60)
os.system("ping -c 6 {}".format(ip_ou_host))
print("-" * 60)
