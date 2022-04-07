
#!C:\Users\ASUS\python\python.exe
import mysql.connector
import smtplib
import cgi
print("content-type:text/html\n\n")
print()

form = cgi.FieldStorage()

name = form.getvalue("name1")
email = form.getvalue("email1")
date = form.getvalue("date1")
doctor = form.getvalue("doctor1")
text = form.getvalue("text")

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login('sharmameherprasad@gmail.com', 'mms1010MMS')
connection.sendmail('sharmameherprasad@gmail.com', 'rohitike73@gmail.com',
                    'subject: Appointment Details \n\n Name: Prasad Ramdham, E-mail: rogitike73@gmail.com, Date: 24-10-2019, Doctor: Dr.Shubham')
connection.quit()


con = mysql.connector.connect(
    user='root', password='', host='localhost', database='appointment')
cur = con.cursor()

cur.execute("insert into record values(%s,%s,%s,%s,%s)",
            (name, email, date, doctor, text))
con.commit()

cur.close()
con.close()
print("<h1>Your Appointment Has Been Booked Successfully.....</h1>")
print("Patient Name: ", name)
print("E-mail: ", email)
print("Date: ", date)
print("Doctor Name: ", doctor)
print("<h2>Thank You, We care for you.....</h1>")
