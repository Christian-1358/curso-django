import requests
import pprint


api_key = "5e9174d934904f408e5173841261310"

link_api = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=São Marcos"


resposta = requests.get(link_api)  #tem que usar get para poder buscar a requisição, se sua api, tiver paremetros que vc quer buscar, vc tem que usar 'params=PARAMETROS '
pprint.pprint(resposta.status_code) # esse 'status_code', vai buscar o estatus do erro (ou se deu true )
pprint.pprint(resposta.content ) #esse .content, ele pode ver a requisição do erro'