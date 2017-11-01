from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='/tmp/test.db'))



connection = pymysql.connect(host='tsuts.tskoli.is', db='v10_vþ2', user='kennitala', password='mypassword')


with connection.cursor() as cursor:

    cursor.execute("INSERT INTO user (user, pass) VALUES ('andri', '1234');") 
    connection.commit() 
    cursor.execute("INSERT INTO user VALUES ('palli', 'kaka')")

    cursor.execute("SELECT * FROM user")

    print(cursor)

    cursor.execute("SELECT * FROM user WHERE user='karl'")

    cursor.execute("INSERT INTO user (user, pass) VALUES ('Nigguh', 'watermelon')")

    connection.commit()

    cursor.execute("SELECT * FROM user")

    cursor.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))
    cursor.execute("INSERT INTO user VALUES ('%s', '%s')" , ("eh variable", "eh variable"))


connection.close()
