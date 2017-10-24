import json

# Skilgreinum breytuna bekkur sem geymir dict (json hlut)
bekkur = {'mynd':[{'nafn':'Rush'}]}



# Skoðum innihald bekkur breytunnar - debug
# print(bekkur)

# Lúppum i gegnum "allann bekkinn"

# dict key value 'nemandi' inniheldur lista
for i in bekkur['mynd']:
    print("Nafn :", i['nafn'])# hver i er i raun gildi í listanum 'nemandi', getum hér notað key value 'nafn'

# auð lína
print()

# Bætum við nemandi..
bekkur['mynd'].append({'nafn':'Forest Gump'})

# Bætum við annan nemandi..
bekkur['mynd'].append({'nafn':'Ninja'})

# Prentum aftur lista með nýjum nemanda
for i in bekkur['mynd']:
    print("Nafn :", i['nafn'])

# Skrifum i skránna bekkur.json, er ekkert að pæla í íslenskum stöfum en það er hægt.
with open("bekkur.json","w") as skra:
    json.dump(bekkur,skra)
skra.close()