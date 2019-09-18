''' Version 2
A python program to get the real-time currency exchange rate
fucntion:
1. get currency exchange rate between CAD and CNY for the first step
2. send results to the email address or to the phone number
3. create histogram based on the past rate -- not done yet
4. send a notification once the rate is over or lower than the value set
    or send a notification regularly
5. make a prediction (optional)
6. GUI window
'''

import time
import datetime as dt
import tkinter as tk

def get_currency(from_currency, to_currency):
    from forex_python.converter import CurrencyRates

    c = CurrencyRates()
    result = c.get_rate(from_currency, to_currency) #get currency rate between CAD and CNY

    print("Result: \n","from currency", from_currency, "to currency", to_currency,
          " is ",result)

    return result

def get_bitcoin(currency):
    from forex_python.bitcoin import BtcConverter

    b = BtcConverter()
    result_bit = b.get_latest_price(currency)

    print("Result: \n", "Bitcoin in currency", currency, "is", result_bit)

# using SMTP_SSL()
def send_email(sender_email, receiver_email, subject, body):
    # import smtplib module for sending emails using SMTP
    # Simple Mail Transfer Protocol
    # smtplib uses RFC 821 protocol
    import smtplib, ssl
    # MIMEText() contains both HTML and plain-text version
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Gmail requires to connect to port 465 if using SMTP_SSL()
    port = 465
    smtp_server = "smtp.gmail.com"
    # can use getpass.getpass() which will read inputs as Password (string)
    # password = input("Type password and press enter: ")
    password = "mypassword" # write password here or create another input/getpass to
                            # enter password more secure
    
    message = MIMEMultipart() # Create a multipart message 
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email_second # for mass emails

    '''
    message = MIMEMultipart('alternative')
    # turn the plain-text version into plain MIMEText objects
    text_mime = MIMEText(text, "plain")
    html_mime = MIMEText(html, "html")

    # add plain-text to MIMEMultipart message
    message.attach(text_mime)
    message.attach(html_mime)
    '''

    # add body to email
    message.attach(MIMEText(body, "plain"))
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

'''
# create a GUI
def create_gui():
    # create a Tk root widget
    top = tk.Tk()
    top.title("Currency Exchange Rate Project")
    # label widget
    L0 = tk.Label(top, text="Hello There",).grid(row=0, column=1)
    L1 = tk.Label(top, text="from currency",).grid(row=1, column=0)
    L2 = tk.Label(top, text="to currency",).grid(row=2, column=0)
    L3 = tk.Label(top, text="Result",).grid(row=3, column=0)
    E1 = tk.Entry(top, bd=5)
    E1.grid(row=1, column=1)
    E2 = tk.Entry(top, bd=5)
    E2.grid(row=2, column=1)
    E3 = tk.Entry(top, bd=5)
    E3.grid(row=3, column=1)
    
    B = tk.Button(top, text="Enter", command=process).grid(row=4, column=1)

    top.mainloop()
'''

def process():
    from_currency = tk.Entry.get(E1)
    to_currency = tk.Entry.get(E2)
    result = get_currency(from_currency, to_currency)
    tk.Entry.insert(E4, 0, result)

if __name__ == "__main__":
    # create a Tk root widget
    top = tk.Tk()
    top.title("Currency Exchange Rate Project")
    # label widget
    L0 = tk.Label(top, text="Hello There",).grid(row=0, column=1)
    L1 = tk.Label(top, text="from currency",).grid(row=1, column=0)
    L2 = tk.Label(top, text="to currency",).grid(row=2, column=0)
    L4 = tk.Label(top, text="Result",).grid(row=4, column=0)
    E1 = tk.Entry(top, bd=5)
    E1.grid(row=1, column=1)
    E2 = tk.Entry(top, bd=5)
    E2.grid(row=2, column=1)
    E4 = tk.Entry(top, bd=5)
    E4.grid(row=4, column=1)
    
    B = tk.Button(top, text="Enter", command=process).grid(row=3, column=1)

    top.mainloop()

''' without GUI     
if __name__ == "__main__":

    print("Welcome !")
    
    # currency exchange
    user_menu_input = input("Currency Rate/Bitcoin/Quit/Email: ")

    while(user_menu_input != "Quit"):
        if user_menu_input == "Currency Rate":
            from_currency = input("currency from: ")
            to_currency = input("to currency: ")
        
        if user_menu_input == "Bitcoin":
            currency = input("Bitcoin price in currency: ")
            get_bitcoin(currency)

        # send email
        if user_menu_input == "Email":
            sender_email = "my@gmail.com"
            receiver_email = "your@gmail.com"
            receiver_email_second = "another@mcmaster.ca"
            subject = "Currency Exchange Rate Update"

            # get currency information
            from_currency = input("currency from: ")
            to_currency = input("to currency: ")
            result = get_currency(from_currency, to_currency)
            body = "The currency rate between " + from_currency + " and " + to_currency + " is " + str(result)

            first_email_time = dt.datetime(2019,9,17,18,41,0) # sending time in UTC
            interval = dt.timedelta(minutes=10) # set interval to be 10 mins

            send_time = first_email_time
            while True:
                time.sleep(send_time.timestamp() - time.time())
                send_email(sender_email, receiver_email, subject, body)
                print("Email sent")
                send_time = send_time + interval

        user_menu_input = input("Enter Quit to quit: ")
        

    
    print("Thank you !")
'''
    
'''
Reference:
1. send email regularly: https://stackoverflow.com/questions/52022134/how-do-i-schedule-an-email-to-send-at-a-certain-time-using-cron-and-smtp-in-pyt
2. send email use python: https://realpython.com/python-send-email/#getting-started
3. forex project github page: https://github.com/MicroPyramid/forex-python/blob/master/forex_python/converter.py
4. tkinter (GUI): https://www.python-course.eu/tkinter_entry_widgets.php

'''
    

