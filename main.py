
import datetime as dt
import random as rd

import smtplib

now = dt.datetime.now()

day = now.weekday()

if day == 0:

    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = rd.choice(all_quotes)
    

    print(quote)



    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user="durga2458dondapati@gmail.com", password="vdex qout duzl rfbz")
        conn.sendmail(
            from_addr="durga2458dondapati@gmail.com",
            to_addrs="durga2458dondapati@gmail.com",
            msg=f'Subject:Monday Motivation\n\n{quote}'
        )
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user="durga2458dondapati@gmail.com", password="vdex qout duzl rfbz")
        conn.sendmail(
            from_addr="durga2458dondapati@gmail.com",
            to_addrs="nihithahy50@gmail.com",
            msg=f'Subject:Monday Motivation\n\n{quote}'
        )