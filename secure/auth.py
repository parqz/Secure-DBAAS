import psycopg2
from passlib.hash import pbkdf2_sha256
conn_string = "host='localhost' dbname='dbas' user='DBAS' password='DBAS'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


def auth_user(username, password, key_space=''):
    cursor.execute("select * from users where username='%s';" % (username,))
    if cursor.rowcount == 1:
        memory = cursor.fetchone()
        return pbkdf2_sha256.verify(password, memory[2])
    return False


def create_user(username, password):
    hashed_password = pbkdf2_sha256.encrypt(password, rounds=100, salt_size=16)
    cursor.execute("insert into users (username, password) values ('%s', '%s');" % (username, hashed_password))
    conn.commit()

