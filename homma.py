import requests
import psycopg2

pw = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kek",headers={'Metadata-Flavor': 'Google'})
sqluser = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kak",headers={'Metadata-Flavor': 'Google'})
ip = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kok",headers={'Metadata-Flavor': 'Google'})

def connect():
    con = psycopg2.connect(host=(ip.text),database="group3db",port=5432,user=(sqluser.text),password=(pw.text))
    cursor = con.cursor()
    select_all(cursor)
    con.commit()
    cursor.close()

def select_all(cursor):

    SQL = "SELECT SUM(AGE(ended,started)) AS hoursum FROM testilog WHERE date(started) = CURRENT_DATE;"
    cursor.execute(SQL)
    row = cursor.fetchone()
    with open('dailyhour.txt', 'w') as file:
        while row is not None:
            file.write(row)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)

if __name__ == '__main__':

    connect()