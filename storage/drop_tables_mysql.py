import mysql.connector

db_conn = mysql.connector.connect(host="10.5.0.5", user="user", password="password", database="leaderboard")

db_cursor = db_conn.cursor()

try:

    db_cursor.execute('''DROP TABLE score''')
    
except Exception as e:

        print(e)
        exit(0)
db_conn.commit()
db_conn.close()