# þurfum að setja pymysql upp í pyCharm (sama rútína og bottle-beaker)
import pymysql

# tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1804003030', passwd='mypassword', db='v10vþ2')
cur = conn.cursor()

# Taflan vinur, dæmi um mögulegt innihald
# kt(int)	nafn(varchar)	gsm(int)
# 1			Daniel			8981234
# 2			Hilmir			8982345

# lesa alla úr töflunni
cur.execute("SELECT * FROM user")
for row in cur:
    print(row[1])
cur.close()
conn.close()

"""
# bæta einum harðkóðuðum i töfluna vinur (fyrsta gildi pk, má ekki vera það sama 2 sinnum)
cur.execute("INSERT INTO vinur Values(5,'Arthur',3541234)")
conn.commit()
cur.close()
conn.close()
"""

"""
# eyða einum með ákv. kt
cur.execute("Delete from vinur where kt = 5")
conn.commit()
cur.close()
conn.close()
"""

"""
# breyta einum eftir ákv. kt
cur.execute("Update vinur set nafn='Andaya', gsm=7771234 where kt = 5")
conn.commit()
cur.close()
conn.close()
"""



@route("/")
def index():

    cur.exconn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1804003030', passwd='mypassword', db='v10vþ2')
    cur = conn.cursor()
    excute("SELECT * FROM user")
    for row in cur:
        print(row[1])
    cur.close()
    conn.close()
    return template("index.tpl")