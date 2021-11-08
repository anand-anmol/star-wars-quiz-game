import mysql.connector

db_conn = mysql.connector.connect(host="localhost", user="root", password="password", database="leaderboard")

db_cursor = db_conn.cursor()

db_cursor.execute('''
        CREATE TABLE score
        (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(250) NOT NULL,
        score INT NOT NULL,
        date_created VARCHAR(100) NOT NULL)
        ''')

db_conn.commit()
db_conn.close()