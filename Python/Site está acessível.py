import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Deu erro')
else:
    print('Tudo ok, consegui acessar o site pudim com sucesso!')
