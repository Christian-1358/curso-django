import requests
import pprint # esse pprint, ira me dar os dados de forma "visivel"
api_key = "5e9174d934904f408e5173841261310"

link_api = "https://api.weatherapi.com/v1/current.json"


parametros = {
    "key": api_key,
    "q": "Londres",
    "lang": "pt"
}




resposta = requests.get(link_api, params=parametros) #tem que usar get para poder buscar a requisição, se sua api, tiver paremetros que vc quer buscar, vc tem que usar 'params=PARAMETROS '

'''
print(resposta.status_code) # esse 'status_code', vai buscar o estatus do erro (ou se deu true )

print(resposta.content ) #esse .content, ele pode ver a requisição do erro
'''

if resposta.status_code == 200:
    dados_requisicao = resposta.json() # fazer a contasulta e se der true (200) e ele ira buscar os dados da requiçao
    pprint.pprint(dados_requisicao) #faz o print do json mas bonito
    
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"] #comandos para poder pegar os parametros
    
    print(temp)
    print(descricao)
    
    