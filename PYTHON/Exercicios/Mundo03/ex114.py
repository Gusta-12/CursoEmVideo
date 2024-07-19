import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br') # tentar abrir uma url
except urllib.error.URLError: #exceção
    print('ERRO!')
else:
    print('Tudo OK!')
# não funciona mais