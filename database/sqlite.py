import sqlite3


def openConnect():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    return conn, cur


def closeConnect(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


def clearDatabase():
    conn, cur = openConnect()
    cur.execute('DROP TABLE users')
    cur.execute('CREATE TABLE users ('
                'user_id INTEGER PRIMARY KEY, '
                'login text,'
                'password text,'
                'eMail text'
                ')')
    cur.execute(f'INSERT INTO users '
                f'(login, password, eMail) '
                f'VALUES '
                f'(?, ?, ?)',
                ('admin',
                 'admin1234',
                 'admin@email.ru'
                 ))
    closeConnect(conn, cur)


def putUser(user):
    conn, cur = openConnect()
    cur.execute(f'INSERT INTO users '
                f'(login, password, eMail) '
                f'VALUES '
                f'(?, ?, ?)',
                (user['login'],
                 user['password'],
                 user['eMail']
                 )
                )
    closeConnect(conn, cur)


def getUserAll():
    conn, cur = openConnect()
    cur.execute("SELECT * FROM users ")
    users = cur.fetchall()
    closeConnect(conn, cur)
    return users


def getUser(variable, inputString):
    conn, cur = openConnect()
    cur.execute(f"SELECT * "
                f"FROM users "
                f"WHERE {variable}='{inputString}'")
    user = cur.fetchall()
    closeConnect(conn, cur)
    print (user)
    return user


def updateUser(user, key, values):
    conn, cur = openConnect()
    cur.execute(f"UPDATE users SET {key} = '{values}' WHERE login='{user}'")
    closeConnect(conn, cur)
