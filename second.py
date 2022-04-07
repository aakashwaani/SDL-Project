#!C:\Users\ASUS\python\python.exe
import mysql.connector
import cgi
print("content-type:text/html\n\n")
print()

form = cgi.FieldStorage()

email = form.getvalue("email1")


con = mysql.connector.connect(
    user='root', password='', host='localhost', database='appointment')
cur = con.cursor()

cur.execute("delete from record where email = %s", (email))
con.commit()

cur.close()
con.close()
print("<h1>Appointment Deleted Successfully </h1>")
