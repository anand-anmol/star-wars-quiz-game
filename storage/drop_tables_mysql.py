import mysql.connector

db_conn = mysql.connector.connect(host="10.5.0.5", user="root", password="password", database="leaderboard")

db_cursor = db_conn.cursor()

db_cursor.execute('''DROP TABLE score''')

db_conn.commit()
db_conn.close()