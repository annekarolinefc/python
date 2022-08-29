
import urllib.request

def ConectaInternet():
    objURL = urllib.request.urlopen('http://www.google.com')
    
    if objURL.getcode() == 200:
        dados = objURL.read()
        print(dados)
        
        
ConectaInternet()