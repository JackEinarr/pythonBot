from helpinfo import OutputInterceptor
import tkinter
import telebot

with OutputInterceptor() as output:
    help(tkinter.Place)
a = '\n'.join(output)
print(a)