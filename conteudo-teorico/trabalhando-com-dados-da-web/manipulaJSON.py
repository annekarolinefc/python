import urllib.request

import json

def ManipulaJSON():
    endereco = 'https://www.google.com'
    webUrl = urllib.request.urlopen(endereco)
    if (webUrl.getcode() == 200):
        dados = webUrl.read()
        oJSON = json.loads(dados)
        
        contagem = oJSON['metadata']['count']
        print("Contage: " + str(contagem))