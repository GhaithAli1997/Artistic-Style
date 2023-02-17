# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:18:36 2021

@author: ghaith
"""
from telegram.ext import MessageHandler
from PIL import ImageTk,Image
import os
import IPython.display as display
import functools
import PIL.Image
import telegram_send
import telegram
import cv2 as cv
#image=cv.imread("s4.jpg")
#telegram_send.send(images=(image),captions=("kjjj"))
with open(r"C:\Users\ghaith\Desktop\Captnnnure.PNG", "rb") as f:
    #telegram_send.send(images=[f])
    #telegram.message(message_id=882961698, text="msg")
    #telegram_send.send(messages=["095"])
    bot=telegram.Bot(token='1720921353:AAEX8ZLGVLHxrT86PNV7gneuOculqIIgcsk')
    bot.send_message(chat_id=619364621, text='USP-Python has started up!')
    bot.send_photo(chat_id=619364621, photo=f)
