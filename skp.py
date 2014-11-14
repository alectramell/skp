#!/usr/bin/python

import os

def chat():
    os.system('clear')
    act = str('chat')
    os.system('CONTACT=$(zenity --entry --title="SKYPE CHAT.." --text="CONTACT: ") && skype skype:$CONTACT?' + act + '')
    os.system('clear')

def call():
    os.system('clear')
    act = str('call')
    os.system('CONTACT=$(zenity --entry --title="SKYPE CALL.." --text="CONTACT: ") && skype skype:$CONTACT?' + act + '')
    os.system('clear')
