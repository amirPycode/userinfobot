#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
create by -- @PyCode
github -- https://github.com/amirPycode
Channel -- @amirPycode
'''
import telebot
from telebot import types
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
bot = telebot.TeleBot("Token")
print("\n\n\t\tBot runed;)")
@bot.message_handler(content_types=['text'])
def user_info(m):
 try:
     if m.text:
       if not m.forward_from:
           username = ''
           username+= (("@"+m.from_user.username) if m.from_user.username else "")
           id = m.from_user.id 
           name = m.from_user.first_name
           lang = ''
           lang+= (("Lang:"+ m.from_user.language_code) if m.from_user.language_code else "")
           last = ''
           last+= (("Last:"+ m.from_user.last_name) if m.from_user.last_name else "")
           i = "{}\nId: {}\nFirst: {}\n{}\n{}".format(username,id,name,last,lang)
           bot.reply_to(m, i)
 except:
     pass
 if m.forward_from:
       username = ''
       username+= (("@"+m.forward_from.username) if m.forward_from.username else "")
       id = m.forward_from.id
       name = m.forward_from.first_name
       lang = ''
       lang+= (("Lang:"+ m.forward_from.language_code) if m.forward_from.language_code else "")
       last = ''
       last+= (("Last:"+ m.forward_from.last_name) if m.forward_from.last_name else "")
       i = "{}\nId: {}\nFirst: {}\n{}\n{}".format(username,id,name,last,lang)
       bot.reply_to(m, i)
bot.polling(True)
