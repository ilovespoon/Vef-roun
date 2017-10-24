import json

with open("bekkur.json","r") as skra:
    gogn = json.load(skra)


skra.close()

val = " "
while val != 2:
    print("\n--------------------------------------")
    print("Json dæmi...")
    print("ýttu á 1 til þessað prenta")
    print("--------------------------------------")
    val = int(input("Press 1 and then enter: "))


    if val == 1:
        print(gogn)


