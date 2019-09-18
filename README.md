# Currency_Exchange_Rate

A python program with simple currency exchange rate search function.

---Version 2---

A python program to get the real-time currency exchange rate
fucntion:
1. get currency exchange rate between CAD and CNY for the first step
2. send results to the email address or to the phone number -- send to an email address
3. create histogram based on the past rate -- not done yet
4. send a notification once the rate is over or lower than the value set
    or send a notification regularly -- send notifications regularly
5. make a prediction (optional) -- not done yet
6. GUI window



---Summary---

Learning notes:
1. forex-python project makes the whole project easier since it grabs all information needed for currency exchange rate and bitcoin price.
2. smtplib python module can be used for simple mass emails sending tasks. It also supports both plain-text and html format.
    It can also send attachments with emails.
3. In order to send emails out regularly or at a certain time slot, time.sleep(), datetime.delta(), datetime.datetime() can be combined
   and used together to accomplish the goal.
4. tkinter module can be used to do simple python GUI programming, easy to use.

What's next:
1. Fix the clear button problem.
2. Create graphs based on the past data.
3. Create an ios application. 

Reference:
1. send email regularly: https://stackoverflow.com/questions/52022134/how-do-i-schedule-an-email-to-send-at-a-certain-time-using-cron-and-smtp-in-pyt
2. send email use python: https://realpython.com/python-send-email/#getting-started
3. forex project github page: https://github.com/MicroPyramid/forex-python/blob/master/forex_python/converter.py
4. tkinter (GUI): https://www.python-course.eu/tkinter_entry_widgets.php

Useful links:
https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
