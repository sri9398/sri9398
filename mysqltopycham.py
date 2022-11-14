

import mysql.connector
cnx = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password ='6521@vinay',
    database ='sri'
)
# curses = cnx.cursor()
# curses.execute("select * from vegetables limit 2")

# print(list(curses))
curses = cnx.cursor()
curses.execute("select * from address limit 2")
for row in curses:
    print(row)
    # print(row[1])
curses.close
cnx.close


print(cnx)


