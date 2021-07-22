import requests
import psycopg2

pw = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kek",headers={'Metadata-Flavor': 'Google'})
sqluser = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kak",headers={'Metadata-Flavor': 'Google'})
ip = requests.get("http://metadata.google.internal/computeMetadata/v1/instance/attributes/kok",headers={'Metadata-Flavor': 'Google'})

def connect():
    con = psycopg2.connect(host=(ip.text),database="group3db",port=5432,user=(sqluser.text),password=(pw.text))
    cursor = con.cursor()
    dailydata(cursor)
    hoursum(cursor)
    con.commit()
    cursor.close()

def hoursum(cursor):

    SQL = "SELECT SUM(AGE(ended,started)) AS hoursum FROM testilog WHERE date(started) = CURRENT_DATE;"
    cursor.execute(SQL)
    row = cursor.fetchone()
    while row is not None:
        with open('dailyhour.txt', 'w') as file:
            file.write(str(row))
            file.write("\n")
        row = cursor.fetchone()

def dailydata(cursor):

    SQL = "SELECT * FROM testilog WHERE date(started) = CURRENT_DATE;"
    cursor.execute(SQL)
    row = cursor.fetchone()
    while row is not None:
        with open('dailyactivities.txt', 'w') as file:
            file.write(str(row))
            file.write("\n")
        row = cursor.fetchone()

if __name__ == '__main__':

    connect()