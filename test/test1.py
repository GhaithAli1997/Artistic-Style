# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:18:55 2021

@author: ghaith
"""
from numpy import *
from tkinter import *
import tkinter
from tkinter import filedialog
import cv2 as cv
from PIL import ImageTk,Image
import os
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import IPython.display as display
import functools
import PIL.Image

root = Tk()
root.title("artistic style")
root.minsize(width=300,height=340)
root.geometry("905x1280")
same=True
n=0.5
i=1
# Adding a background image
background_image =Image.open(r"C:\Users\ghaith\Desktop\Artistic style project\interface\photo_2021-06-08_19-35-10.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
#m1=Image.open("4.jpg") 
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
#Canvas1 = Canvas(root)
#Canvas1.create_image(300,340,image = img)      
#Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
#Canvas1.pack(expand=True,fill=BOTH)

l1=Label(root,image=img)
l1.grid(rowspan=905, columnspan=newImageSizeWidth)
#headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
#headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
#headingLabel = Label(headingFrame1, text="Welcome to \n artistic style", bg='black', fg='white', font=('Courier',15))
#headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
btn1 = Button(root,text="Add Your photo",bg='black', fg='white',command=lambda:addphoto())
btn1.place(relx=0.65,rely=0.3, relwidth=0.3,relheight=0.1)
    
btn2 = Button(root,text="select a style",bg='black', fg='white',command=lambda:addstyle())
btn2.place(relx=0.65,rely=0.4, relwidth=0.3,relheight=0.1)
    
btn3 = Button(root,text="start transform",bg='black', fg='white',command=lambda:bb(i))
btn3.place(relx=0.65,rely=0.5, relwidth=0.3,relheight=0.1)

btn4 = Button(root,text="print image",bg='black', fg='white',command=lambda:printer1())
btn4.place(relx=0.65,rely=0.6, relwidth=0.3,relheight=0.1)

btn5 = Button(root,text="close window",bg='black', fg='white',command=lambda:quit())
btn5.place(relx=0.65,rely=0.7, relwidth=0.3,relheight=0.1)

###########################

def addphoto():
    Root1 = tkinter.Tk()
    Root1.withdraw() # Hide the Tkinter.Tk() instance
    default_dir = "content"
    if os.path.isfile(r'output\1.jpg'):
       os.remove(r'output\1.jpg')
    file_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(default_dir)))
    image = Image.open(file_path)
    image.save(r'output\1.jpg')
    
###########################
def addstyle():
    Root1 = tkinter.Tk()
    Root1.withdraw() # Hide the Tkinter.Tk() instance
    default_dir = "styles"
    if os.path.isfile(r'output\2.jpg'):
       os.remove(r'output\2.jpg')
    file_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(default_dir)))
    image = Image.open(file_path)
    image.save(r'output\2.jpg')
    tkimage = ImageTk.PhotoImage(image)
    myvar=Label(Root1,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
##################################    
def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)
##########################################################
def bb(i1):
    content_path = r'output\1.jpg'
    style_path = r'output\2.jpg'
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    hub_model = hub.load('magenta_arbitrary-image-stylization-v1-256_2')
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    tensor_to_image(stylized_image)
    l=str(i1)
    tensor_to_image(stylized_image).save("finaloutput/"+l+".jpg")
    global i
    i+=1
    
####################################
def load_img(path_to_img):
  
  img2 = tf.io.read_file(path_to_img)
  img2 = tf.image.decode_image(img2, channels=3)
  img2 = tf.image.convert_image_dtype(img2, tf.float32)
  shape = tf.cast(tf.shape(img2)[:-1], tf.float32)
  max_dim = 900
  long_dim = max(shape)
  scale = max_dim / long_dim
  new_shape = tf.cast(shape * scale, tf.int32)
  img2 = tf.image.resize(img2, new_shape)
  img2 = img2[tf.newaxis, :]
  return img2
##########################################################
def printer1():
    Root2 = tkinter.Tk()
    Root2.withdraw() # Hide the Tkinter.Tk() instance
    default_dir = "finaloutput"
    file_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(default_dir)))
    image = Image.open(file_path)
    im_width, im_height = image.size
    if im_width > im_height:
            image = image.rotate(90)
    image.thumbnail((im_height, im_width), Image.ANTIALIAS)
    printer.printImage(image, False)
    printer.justify('C')
    printer.setSize('S')
    printer.println("PolaPi-Zero")
    printer.feed(3)
##################################################################
def quit():
        root.destroy()
        

mainloop()
