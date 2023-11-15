import urllib
import urllib.request

try:
    site = urllib.request("https://www.gupy.io/")
except:
    print("site indisponível")
else:
    print("site disponível")