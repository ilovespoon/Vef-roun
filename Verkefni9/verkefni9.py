import urllib.request, json
with urllib.request.urlopen("http://www.apis.is/concerts") as skra:
    efni = json.loads(skra.read().decode())
    print(efni)