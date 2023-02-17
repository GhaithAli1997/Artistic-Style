# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:48:14 2021

@author: ghaith
"""
import cv2 as cv
import tensorflow as tf
import tensorflow_hub as hub
from numpy import *
from tkinter import *
import tkinter
from tkinter import filedialog
import cv2 as cv
from PIL import ImageTk,Image
import os
import IPython.display as display
import functools
import PIL.Image
import numpy as np
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import artist_information
#import telegram_send
#import telegram
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

root = Tk() # create root window
root.title("Artistic Style")
root.maxsize(1920,1080) # width x height
root.config(bg="gray")


listimage=os.listdir('finaloutput')
i=len(listimage)+1

s1=""
equation=StringVar()
var = StringVar()

# Create left and right frames
frame1 = Frame(root, width=200, height= 400, bg='grey')
frame1.grid(row=0, column=0, padx=5, pady=5)

frame2 = Frame(root, width=200, height=400, bg='grey')
frame2.grid(row=1, column=0, padx=5, pady=5)

frame3 = Frame(root, width=650, height=400, bg='grey')
frame3.grid(row=0, column=1, padx=5, pady=5)

frame4 = Frame(root, width=650, height=400, bg='grey')
frame4.grid(row=1, column=1, padx=5, pady=5)

frame5 = Frame(root, width=650, height=400, bg='grey')
frame5.grid(row=0, column=2,padx=5, pady=5)

frame6 = Frame(root, width=650, height=400, bg='grey')
frame6.grid(row=1, column=2,padx=5, pady=5)
##################################fram1#######
btn1 = Button(frame1,text="Add Your photo",width=30, height=4,bg='black', fg='white',command=lambda:addphoto())
btn1.grid(row=1, column=0)
    
btn2 = Button(frame1,text="select a style",width=30, height=4,bg='black', fg='white',command=lambda:addstyle())
btn2.grid(row=2, column=0)
    
btn3 = Button(frame1,text="start transform",width=30, height=4,bg='black', fg='white',command=lambda:bb(i))
btn3.grid(row=3, column=0)

btn4 = Button(frame1,text="Show image",width=30, height=4,bg='black', fg='white',command=lambda:showe())
btn4.grid(row=4, column=0)

#lable0 = Label(frame1,text="Send your image to telegram\nenter your user name",width=30, height=4,bg='black', fg='white')
#lable0.grid(row=4, column=0)

t1=Entry(frame1,textvariable= equation,width=35,)
t1.grid(row=5, column=0)
equation.set('')

btn7 = Button(frame1,text="Send",width=30, height=1,bg='purple', fg='white',command=lambda:nwindow())
btn7.grid(row=6, column=0)
###########################fram6#######
r1 = Radiobutton(frame2,bg="gray", text='Leonardo da Vinci', width=20,variable=var, value=1,command=lambda:prin())
r1.grid(row=0, column=0)
r2 = Radiobutton(frame2,bg="gray", text='Michelangelo', width=20,variable=var, value=2,command=lambda:prin())
r2.grid(row=1, column=0)
r3 =Radiobutton(frame2,bg="gray", text='John Constable',width=20, variable=var, value=3,command=lambda:prin())
r3.grid(row=3, column=0)
r4 =Radiobutton(frame2,bg="gray", text='William Hogarth',width=20, variable=var, value=4,command=lambda:prin())
r4.grid(row=4, column=0)
r5 = Radiobutton(frame2, bg="gray",text='Vincent Willem van Gogh', width=20,variable=var, value=5,command=lambda:prin())
r5.grid(row=5, column=0)
#r6 = Radiobutton(frame2, text='Option D', width=20,variable=var, value=6,command=lambda:prin())
#r6.grid(row=6, column=0)
#r7 =Radiobutton(frame2, text='Option E',width=20, variable=var, value=7,command=lambda:prin())
#r7.grid(row=7, column=0)
#r8 =Radiobutton(frame2, text='Option F',width=20, variable=var, value=8,command=lambda:prin())
#r8.grid(row=8, column=0)

lable5 = Label(frame6, bg='gray', width=100,height=25, text='empty')
lable5.grid(row=0, columnspan=100)

##############################fram2#############################
def showe():
    l1=str(i-1)
    #print(equation.get())
    phon=equation.get()
    d1="finaloutput/"+l1+".jpg"
    d2=cv.imread(d1)
    cv.imshow("printer", d2)
    cv.waitKey(0)
######################################################
def resi(im):
  n=0.5
  same=True
  background_frame3=im
  [imageSizeWidth, imageSizeHeight] = background_frame3.size
  
  if imageSizeWidth>650:
         imageSizeWidth=650
  if imageSizeHeight>400:
      imageSizeHeight=400
      
  background_frame3 = background_frame3.resize((imageSizeWidth,imageSizeHeight),Image.ANTIALIAS)
  img = ImageTk.PhotoImage(background_frame3)
  return img
##############################
ba=Image.open(r"output/1.jpg")
ba=resi(ba)
lable1=Label(frame3,image=ba)
lable1.pack(fill = BOTH, expand = 1)
##############################################################################
l2=Image.open(r"output/2.jpg")
l2=resi(l2)
lable2=Label(frame4,image=l2)
lable2.pack(fill = BOTH, expand = 1)
######################################################################################
b=str(i-1)
l3=Image.open(r"finaloutput/"+b+".jpg")
l3=resi(l3)
lable3=Label(frame5,image=l3)
lable3.pack(fill = BOTH, expand = 1)


###########################################
def addphoto():
    Root1 = tkinter.Tk()
    Root1.withdraw() # Hide the Tkinter.Tk() instance
    default_dir = "content"
    if os.path.isfile(r'output\1.jpg'):
       os.remove(r'output\1.jpg')
    file_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(default_dir)))
    image1 = Image.open(file_path)
    image1.save(r'output\1.jpg')
    photo1 = Image.open(r'output\1.jpg')
    photo1=resi(photo1)
    lable1.configure(image=photo1)
    lable1.photo = photo1
    
##########################################
def addstyle():
    Root1 = tkinter.Tk()
    Root1.withdraw() # Hide the Tkinter.Tk() instance
    default_dir = "styles/"+var.get()
    if os.path.isfile(r'output\2.jpg'):
       os.remove(r'output\2.jpg')
    file_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(default_dir)))
    image = Image.open(file_path)
    global s1
    s1=str(file_path)
    image.save(r'output\2.jpg')
    photo2 = Image.open(r'output\2.jpg')
    photo2=resi(photo2)
    lable2.configure(image=photo2)
    lable2.photo = photo2    
    x=len(s1)-4
    s1=s1[0:x]
    for inde in range(x-1,0,-1):
        if s1[inde]=='/':
            s1=s1[inde+1:x]
            break
    s=artist_information.image_dictionary[s1]
    lable5.config(text=s)
    
    
            
#################################333
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
    photo3 = Image.open(r"finaloutput/"+l+".jpg")
    photo3=resi(photo3)
    lable3.configure(image=photo3)
    lable3.photo = photo3 
####################################################3
def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)
#####################################################
def load_img(path_to_img):
  
  img2 = tf.io.read_file(path_to_img)
  img2 = tf.image.decode_image(img2, channels=3)
  img2 = tf.image.convert_image_dtype(img2, tf.float32)
  shape = tf.cast(tf.shape(img2)[:-1], tf.float32)
  max_dim =512
  long_dim = max(shape)
  scale = max_dim / long_dim
  new_shape = tf.cast(shape * scale, tf.int32)
  img2 = tf.image.resize(img2, new_shape)
  img2 = img2[tf.newaxis, :]
  return img2
###############################################333

def quit():
        root.destroy()
        
###################################
def nwindow():
    l1=str(i-1)
    #print(equation.get())
    phon=equation.get()
    d1="finaloutput/"+l1+".jpg"
    
    with open(d1, "rb") as f:
      #telegram_send.send//////////////////////////////(images=[f])
      #telegram.sendMessage(chat_id=phon, text="msg")
      #telegram_send.send(messages=[phon])
      bot=telegram.Bot(token='1720921353:AAEX8ZLGVLHxrT86PNV7gneuOculqIIgcsk')
      #bot.send_message(chat_id=phon, text='USP-Python has started up!')
      bot.send_photo(chat_id=phon, photo=f)

##############################################################
def prin():
    s=artist_information.style_dictionary[int(var.get())]
    lable5.config(text=s)

root.mainloop()