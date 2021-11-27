from pandas.core.reshape.concat import concat
import yagmail
import os
import time
import pandas

sender = 'gudween.code@gmail.com'
#reciever = 'greyling.goetzinger@easyonlinemail.net'
#'amandafox2000@mail.ru'

subject = 'This is the subject!'

df = pandas.read_csv('contacts.csv')

y = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

def gen_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))


for index, row in df.iterrows():
    name = row['name']
    filename = row['name'] + "'s-bill.txt"
    amount = row['amount']

    gen_file(filename, amount)
    
    y.send(to=row['mail']
         , subject=subject
         , contents=[f"""
            Hi {name}!
            You have to pay {amount}
            Bill is attached!
            """
            , filename])
    print('Email Sent! ', time.ctime())
