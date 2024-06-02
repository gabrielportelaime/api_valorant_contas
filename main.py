#SCRIPT PARA VERIFICAR OS ELOS DAS MINHAS CONTAS
import requests

for i in range(1, 7):
    url = "https://api.kyroskoh.xyz/valorant/v1/mmr/br/galux/0" + str(i) + "01?display=0"
    response = requests.get(url)
    print("Galux#0" + str(i) + "01" + " - " + response.text)
