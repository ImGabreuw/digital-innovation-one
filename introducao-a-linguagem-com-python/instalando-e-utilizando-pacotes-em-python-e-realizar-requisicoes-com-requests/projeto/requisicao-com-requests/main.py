import requests


def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

    dados_cep = response.json()

    print(response.status_code)
    print(dados_cep)

    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))

    dados_pokemon = response.json()

    print(response.status_code)
    print(dados_pokemon)

    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)

    return response.text


if __name__ == '__main__':
    retorna_dados_cep("01001000")
    retorna_dados_pokemon("ditto")
