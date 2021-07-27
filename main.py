import datetime as dt
import random
import smtplib
import pandas as pd

#check if current day match with birthday in dic
current_day = dt.datetime.today()
today = (current_day.month, current_day.day)


#convert csv to dataframe
data= pd.read_csv('birthdays.csv')


new_dic = {(rows['month'], rows['day']): rows for (index, rows) in data.iterrows()}

if today in new_dic:
    person_birthday = new_dic[today]['name']
    with open(f'./letter_templates/letter_{random.randint(1,3)}.txt') as content:
        new_content = content.read()
        new_content= new_content.replace('[NAME]', person_birthday)

#set_up_send_email
server = smtplib.SMTP('smtp.gmail.com.')
server.starttls()
username = 'nguyentangthaihoa2101@gmail.com'
password = '*******'
to_email = 'hoa.ntt5224@sinhvien.hoasen.edu.vn'
bcc = 'nguyentangthaihoa21011999@gmail.com'
subject = 'Sending from pythoneverywhere'
body = new_content
server.login(user=username, password=password)
server.sendmail(from_addr=username, to_addrs=new_dic[today]['email'], msg=f'Subject: {subject}\n\n {body}')


