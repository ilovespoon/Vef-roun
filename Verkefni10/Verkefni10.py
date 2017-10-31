from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='/tmp/test.db'))



connection = pymysql.connect(host='tsuts.tskoli.is', db='v10_vþ2', user='kennitala', password='mypassword')


with connection.cursor() as cursor:

    cursor.execute("INSERT INTO user (user, pass) VALUES ('andri', '1234');") #ef þu ætlar að run-a eh sql þa verður það að vera inni i cursor.execute.
    connection.commit() # ÞETTA ER MIKILVÆGT!!!!!!!!!!!!!!! eftir að hafa gert eh sql command
    cursor.execute("INSERT INTO user VALUES ('palli', 'kaka')")

    cursor.execute("SELECT * FROM user")

    print(cursor)

    cursor.execute("SELECT * FROM user WHERE user='karl'")

    cursor.execute("INSERT INTO user (user, pass) VALUES ('Nigguh', 'watermelon')")

    connection.commit()

    cursor.execute("SELECT * FROM user")

    cursor.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2)) #notaðu þetta þegar þu ert að signup notanda
    cursor.execute("INSERT INTO user VALUES ('%s', '%s')" , ("eh variable", "eh variable"))

    # https://stackoverflow.com/questions/775296/python-mysql-parameterized-queries
    # farðu inn i þetta til að uploada variables í sql


connection.close()
