import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('ERRO: o site não esta disponivel no momento')
else:
    print('esta tudo ok')
    print(site.read())  # lêtodo o conteudo em html do site
