from tqdm import tqdm
import time
import requests

with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")
endereco_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    if cidade == "Rio de Janeiro":
        endereco_entrega.append((cep, bairro))
print(endereco_entrega)

