#!/usr/bin/env python
# coding: utf-8

# In[1]:


#分頁
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import  ImageTk, Image, ImageDraw
import os


#窗口
root = tk.Tk()
root.title('麥當勞午晚餐時段最低價格計算系統')
root.geometry('1100x780') # width x height
root['bg'] = 'light blue'
root.resizable(width=0, height=0)

#分頁
note = ttk.Notebook(root)
note.place(relx=0,rely=0)

#第一頁
win1 = tk.Frame()
note.add(win1,text='主頁(主餐)')
win1['bg'] = 'white'

#第二頁
win2 = tk.Frame()
note.add(win2,text='1+1')
win2['bg'] = 'white'

#第三頁
win3 = tk.Frame()
note.add(win3,text='點心')
win3['bg'] = 'white'

#第四頁
win4 = tk.Frame()
note.add(win4,text='飲料/配餐說明')
win4['bg'] = 'white'

#第五頁
win5 = tk.Frame()
note.add(win5,text='結算')
win5['bg'] = 'white'


# In[2]:


# ----------------------主餐----------------------

# Logo
logo= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/logo.jpg')).resize((120, 120), Image.ANTIALIAS))
pic_logo= tk.Label(win1,image = logo)
pic_logo.grid(row=0,column=0, sticky=W)
pic_logo['bg'] = 'white'

capation = tk.Label(win1, text='*將購買數量(阿拉伯數字)輸入下方空格，並在結算頁中按下確認點餐，系統將會計算出最便宜的組合價格*\n(不包含甜心卡、早餐、兒童餐、快樂分享餐、得來速、Mccafe)\n(圖上數字為單點價格)',font=('微軟正黑體',14))
capation.grid(row=0,column=1,columnspan=20,padx=5,pady=5, sticky=W)
capation['bg'] = 'white'



# Label
title_m = tk.Label(win1, text='主餐',font=('微軟正黑體',16))
title_m.grid(row=1,column=0,padx=5,pady=5, sticky=W)
title_m['bg'] = 'OrangeRed2'
capation_m = tk.Label(win1, text='*超值全餐配餐說明：請詳見飲料/配餐說明分頁*',font=('微軟正黑體',12))
capation_m.grid(row=1,column=1, columnspan=20,padx=5,pady=5, sticky=W)
capation_m['bg'] = 'white'

#讀取食物照片 + 調整圖片大小
m1= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/1.jpeg")).resize((120, 120), Image.ANTIALIAS))
m2= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/2.jpeg")).resize((120, 120), Image.ANTIALIAS))
m3= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/3.jpeg")).resize((120, 120), Image.ANTIALIAS))
m4= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/4.jpeg")).resize((120, 120), Image.ANTIALIAS))
m5= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/5.jpeg")).resize((120, 120), Image.ANTIALIAS))
m6= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/6.jpeg")).resize((120, 120), Image.ANTIALIAS))
m7= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/7.jpeg")).resize((120, 120), Image.ANTIALIAS))
m8= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/8.jpeg")).resize((120, 120), Image.ANTIALIAS))
m9= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/9.jpeg")).resize((120, 120), Image.ANTIALIAS))
m10= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/10.jpeg")).resize((120, 120), Image.ANTIALIAS))
m11= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/11.jpeg")).resize((120, 120), Image.ANTIALIAS))
m12= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/12.jpeg")).resize((120, 120), Image.ANTIALIAS))
m13= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/13.jpeg")).resize((120, 120), Image.ANTIALIAS))
m14= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/14.jpeg")).resize((120, 120), Image.ANTIALIAS))
m15= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/15.jpeg")).resize((120, 120), Image.ANTIALIAS))
m16= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/16.jpeg")).resize((120, 120), Image.ANTIALIAS))
m17= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/17.jpeg")).resize((120, 120), Image.ANTIALIAS))
m18= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/meal/18.jpeg")).resize((120, 120), Image.ANTIALIAS))

pic_m1= tk.Label(win1,image = m1)
pic_m2= tk.Label(win1,image = m2)
pic_m3= tk.Label(win1,image = m3)
pic_m4= tk.Label(win1,image = m4)
pic_m5= tk.Label(win1,image = m5)
pic_m6= tk.Label(win1,image = m6)
pic_m7= tk.Label(win1,image = m7)
pic_m8= tk.Label(win1,image = m8)
pic_m9= tk.Label(win1,image = m9)
pic_m10= tk.Label(win1,image = m10)
pic_m11= tk.Label(win1,image = m11)
pic_m12= tk.Label(win1,image = m12)
pic_m13= tk.Label(win1,image = m13)
pic_m14= tk.Label(win1,image = m14)
pic_m15= tk.Label(win1,image = m15)
pic_m16= tk.Label(win1,image = m16)
pic_m17= tk.Label(win1,image = m17)
pic_m18= tk.Label(win1,image = m18)


#食物名稱
name_m1 = tk.Label(win1, text='1、大麥克',font=('微軟正黑體',12), anchor='w')
name_m2 = tk.Label(win1, text='2、雙層牛肉吉事堡',font=('微軟正黑體',12), anchor='w')
name_m3 = tk.Label(win1, text='3、嫩煎鷄腿堡',font=('微軟正黑體',12), anchor='w')
name_m4 = tk.Label(win1, text='4、麥香鷄',font=('微軟正黑體',12), anchor='w')
name_m5 = tk.Label(win1, text='5、麥克鷄塊(6塊)',font=('微軟正黑體',12), anchor='w')
name_m6 = tk.Label(win1, text='6、麥克鷄塊(10塊)',font=('微軟正黑體',12), anchor='w')
name_m7 = tk.Label(win1, text='7、勁辣鷄腿堡',font=('微軟正黑體',12), anchor='w')
name_m8 = tk.Label(win1, text='8、原味麥脆鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')
name_m9 = tk.Label(win1, text='9、辣味麥脆鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')
name_m10 = tk.Label(win1, text='10、原味麥脆鷄腿(2塊)',font=('微軟正黑體',12), anchor='w')
name_m11 = tk.Label(win1, text='11、辣味麥脆鷄腿(2塊)',font=('微軟正黑體',12), anchor='w')
name_m12 = tk.Label(win1, text='12、麥香魚',font=('微軟正黑體',12), anchor='w')
name_m13 = tk.Label(win1, text='13、蕈菇安格斯黑牛堡',font=('微軟正黑體',12), anchor='w')
name_m14 = tk.Label(win1, text='14、BLT 安格斯黑牛堡',font=('微軟正黑體',12), anchor='w')
name_m15 = tk.Label(win1, text='15、BLT 辣脆鷄腿堡',font=('微軟正黑體',12), anchor='w')
name_m16 = tk.Label(win1, text='16、BLT 嫩煎鷄腿堡',font=('微軟正黑體',12), anchor='w')
name_m17 = tk.Label(win1, text='17、凱撒辣脆鷄沙拉',font=('微軟正黑體',12), anchor='w')
name_m18 = tk.Label(win1, text='18、義式烤鷄沙拉',font=('微軟正黑體',12), anchor='w')
space1 = tk.Label(win1, text=' ',font=('微軟正黑體',14), anchor='w')
space2 = tk.Label(win1, text=' ',font=('微軟正黑體',14), anchor='w')
space3 = tk.Label(win1, text=' ',font=('微軟正黑體',8), anchor='w')

#照片位置

pic_m1.grid(row=3,column=0,padx=10, sticky=W)
pic_m2.grid(row=3,column=1,padx=10, sticky=W)
pic_m3.grid(row=3,column=2,padx=10, sticky=W)
pic_m4.grid(row=3,column=3,padx=10, sticky=W)
pic_m5.grid(row=3,column=4,padx=10, sticky=W)
pic_m6.grid(row=3,column=5,padx=10, sticky=W)
pic_m7.grid(row=7,column=0,padx=10, sticky=W)
pic_m8.grid(row=7,column=1,padx=10, sticky=W)
pic_m9.grid(row=7,column=2,padx=10, sticky=W)
pic_m10.grid(row=7,column=3,padx=10, sticky=W)
pic_m11.grid(row=7,column=4,padx=10, sticky=W)
pic_m12.grid(row=7,column=5,padx=10, sticky=W)
pic_m13.grid(row=11,column=0,padx=10, sticky=W)
pic_m14.grid(row=11,column=1,padx=10, sticky=W)
pic_m15.grid(row=11,column=2,padx=10, sticky=W)
pic_m16.grid(row=11,column=3,padx=10, sticky=W)
pic_m17.grid(row=11,column=4,padx=10, sticky=W)
pic_m18.grid(row=11,column=5,padx=10, sticky=W)
space1.grid(row=5,column=0,padx=10, sticky=W)
space2.grid(row=9,column=0,padx=10, sticky=W)
space3.grid(row=13,column=0,padx=10, sticky=W)


pic_m1['bg'] = 'white'
pic_m2['bg'] = 'white'
pic_m3['bg'] = 'white'
pic_m4['bg'] = 'white'
pic_m5['bg'] = 'white'
pic_m6['bg'] = 'white'
pic_m7['bg'] = 'white'
pic_m8['bg'] = 'white'
pic_m9['bg'] = 'white'
pic_m10['bg'] = 'white'
pic_m11['bg'] = 'white'
pic_m12['bg'] = 'white'
pic_m13['bg'] = 'white'
pic_m14['bg'] = 'white'
pic_m15['bg'] = 'white'
pic_m16['bg'] = 'white'
pic_m17['bg'] = 'white'
pic_m18['bg'] = 'white'
space1['bg'] = 'white'
space2['bg'] = 'white'
space3['bg'] = 'white'


#名稱位置

name_m1.grid(row=2,column=0,padx=10, sticky=W)
name_m2.grid(row=2,column=1,padx=10, sticky=W)
name_m3.grid(row=2,column=2,padx=10, sticky=W)
name_m4.grid(row=2,column=3,padx=10, sticky=W)
name_m5.grid(row=2,column=4,padx=10, sticky=W)
name_m6.grid(row=2,column=5,padx=10, sticky=W)
name_m7.grid(row=6,column=0,padx=10, sticky=W)
name_m8.grid(row=6,column=1,padx=10, sticky=W)
name_m9.grid(row=6,column=2,padx=10, sticky=W)
name_m10.grid(row=6,column=3,padx=10, sticky=W)
name_m11.grid(row=6,column=4,padx=10, sticky=W)
name_m12.grid(row=6,column=5,padx=10, sticky=W)
name_m13.grid(row=10,column=0,padx=10, sticky=W)
name_m14.grid(row=10,column=1,padx=10, sticky=W)
name_m15.grid(row=10,column=2,padx=10, sticky=W)
name_m16.grid(row=10,column=3,padx=10, sticky=W)
name_m17.grid(row=10,column=4,padx=10, sticky=W)
name_m18.grid(row=10,column=5,padx=10, sticky=W)

name_m1['bg'] = 'white'
name_m2['bg'] = 'white'
name_m3['bg'] = 'white'
name_m4['bg'] = 'white'
name_m5['bg'] = 'white'
name_m6['bg'] = 'white'
name_m7['bg'] = 'white'
name_m8['bg'] = 'white'
name_m9['bg'] = 'white'
name_m10['bg'] = 'white'
name_m11['bg'] = 'white'
name_m12['bg'] = 'white'
name_m13['bg'] = 'white'
name_m14['bg'] = 'white'
name_m15['bg'] = 'white'
name_m16['bg'] = 'white'
name_m17['bg'] = 'white'
name_m18['bg'] = 'white'


# Text 輸入數量
text_m1 = tk.Text(win1, width = 5,height = 1)
text_m2 = tk.Text(win1, width = 5,height = 1)
text_m3 = tk.Text(win1, width = 5,height = 1)
text_m4 = tk.Text(win1, width = 5,height = 1)
text_m5 = tk.Text(win1, width = 5,height = 1)
text_m6 = tk.Text(win1, width = 5,height = 1)
text_m7 = tk.Text(win1, width = 5,height = 1)
text_m8 = tk.Text(win1, width = 5,height = 1)
text_m9 = tk.Text(win1, width = 5,height = 1)
text_m10 = tk.Text(win1, width = 5,height = 1)
text_m11 = tk.Text(win1, width = 5,height = 1)
text_m12 = tk.Text(win1, width = 5,height = 1)
text_m13 = tk.Text(win1, width = 5,height = 1)
text_m14 = tk.Text(win1, width = 5,height = 1)
text_m15 = tk.Text(win1, width = 5,height = 1)
text_m16 = tk.Text(win1, width = 5,height = 1)
text_m17 = tk.Text(win1, width = 5,height = 1)
text_m18 = tk.Text(win1, width = 5,height = 1)


# Text 位置
text_m1.grid(row=4,column=0,padx=10)
text_m2.grid(row=4,column=1,padx=10)
text_m3.grid(row=4,column=2,padx=10)
text_m4.grid(row=4,column=3,padx=10)
text_m5.grid(row=4,column=4,padx=10)
text_m6.grid(row=4,column=5,padx=10)
text_m7.grid(row=8,column=0,padx=10)
text_m8.grid(row=8,column=1,padx=10)
text_m9.grid(row=8,column=2,padx=10)
text_m10.grid(row=8,column=3,padx=10)
text_m11.grid(row=8,column=4,padx=10)
text_m12.grid(row=8,column=5,padx=10)
text_m13.grid(row=12,column=0,padx=10)
text_m14.grid(row=12,column=1,padx=10)
text_m15.grid(row=12,column=2,padx=10)
text_m16.grid(row=12,column=3,padx=10)
text_m17.grid(row=12,column=4,padx=10)
text_m18.grid(row=12,column=5,padx=10)

text_m1.insert(tk.INSERT, "0")
text_m2.insert(tk.INSERT, "0")
text_m3.insert(tk.INSERT, "0")
text_m4.insert(tk.INSERT, "0")
text_m5.insert(tk.INSERT, "0")
text_m6.insert(tk.INSERT, "0")
text_m7.insert(tk.INSERT, "0")
text_m8.insert(tk.INSERT, "0")
text_m9.insert(tk.INSERT, "0")
text_m10.insert(tk.INSERT, "0")
text_m11.insert(tk.INSERT, "0")
text_m12.insert(tk.INSERT, "0")
text_m13.insert(tk.INSERT, "0")
text_m14.insert(tk.INSERT, "0")
text_m15.insert(tk.INSERT, "0")
text_m16.insert(tk.INSERT, "0")
text_m17.insert(tk.INSERT, "0")
text_m18.insert(tk.INSERT, "0")


text_m1['bg'] = 'WhiteSmoke'
text_m2['bg'] = 'WhiteSmoke'
text_m3['bg'] = 'WhiteSmoke'
text_m4['bg'] = 'WhiteSmoke'
text_m5['bg'] = 'WhiteSmoke'
text_m6['bg'] = 'WhiteSmoke'
text_m7['bg'] = 'WhiteSmoke'
text_m8['bg'] = 'WhiteSmoke'
text_m9['bg'] = 'WhiteSmoke'
text_m10['bg'] = 'WhiteSmoke'
text_m11['bg'] = 'WhiteSmoke'
text_m12['bg'] = 'WhiteSmoke'
text_m13['bg'] = 'WhiteSmoke'
text_m14['bg'] = 'WhiteSmoke'
text_m15['bg'] = 'WhiteSmoke'
text_m16['bg'] = 'WhiteSmoke'
text_m17['bg'] = 'WhiteSmoke'
text_m18['bg'] = 'WhiteSmoke'


# In[3]:


# ----------------------1+1----------------------

# Label
title_m = tk.Label(win2, text='1+1',font=('微軟正黑體',16))
title_m.grid(row=0,column=0,padx=5,pady=5, sticky=W)
title_m['bg'] = 'OrangeRed2'
capation_1 = tk.Label(win2, text='* 食物x1 + 飲料x1 為一組，一組50元*',font=('微軟正黑體',12))
capation_1.grid(row=0,column=1,columnspan=20,padx=5,pady=5, sticky=W)
capation_1['bg'] = 'white'

size_plus = 195
#讀取食物照片 + 調整圖片大小
plus1= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/1plus1/applepie.jpeg")).resize((size_plus, size_plus), Image.ANTIALIAS))
plus2= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/cheeseburger.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus3= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/chickenmcnuggets4.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus4= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/frenchfriessmall.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus5= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/icecreamlarge.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus6= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/mcchicken.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus7= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/spicychickenwing.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))
plus8= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/1plus1/tenderchickenwing.jpeg')).resize((size_plus, size_plus), Image.ANTIALIAS))

pic_plus1= tk.Label(win2,image = plus1)
pic_plus2= tk.Label(win2,image = plus2)
pic_plus3= tk.Label(win2,image = plus3)
pic_plus4= tk.Label(win2,image = plus4)
pic_plus5= tk.Label(win2,image = plus5)
pic_plus6= tk.Label(win2,image = plus6)
pic_plus7= tk.Label(win2,image = plus7)
pic_plus8= tk.Label(win2,image = plus8)



#食物名稱
name_plus = tk.Label(win2, text='1+1食物區',font=('微軟正黑體',12), anchor='w')
name_plus1 = tk.Label(win2, text='1、蘋果派',font=('微軟正黑體',12), anchor='w')
name_plus2 = tk.Label(win2, text='2、吉事堡',font=('微軟正黑體',12), anchor='w')
name_plus3 = tk.Label(win2, text='3、麥克雞塊(4塊)',font=('微軟正黑體',12), anchor='w')
name_plus4 = tk.Label(win2, text='4、薯條(小)',font=('微軟正黑體',12), anchor='w')
name_plus5 = tk.Label(win2, text='5、大蛋捲冰淇淋',font=('微軟正黑體',12), anchor='w')
name_plus6 = tk.Label(win2, text='6、麥香鷄',font=('微軟正黑體',12), anchor='w')
name_plus7 = tk.Label(win2, text='7、勁辣香鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')
name_plus8 = tk.Label(win2, text='8、酥嫩鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')

#space_plus1 = tk.Label(win2, text=' ',font=('微軟正黑體',14), anchor='w')
space_plus2 = tk.Label(win2, text=' ',font=('微軟正黑體',14), anchor='w')


#照片位置

pic_plus1.grid(row=3,column=0,padx=10, sticky=W)
pic_plus2.grid(row=3,column=1,padx=10, sticky=W)
pic_plus3.grid(row=3,column=2,padx=10, sticky=W)
pic_plus4.grid(row=3,column=3,padx=10, sticky=W)
pic_plus5.grid(row=7,column=0,padx=10, sticky=W)
pic_plus6.grid(row=7,column=1,padx=10, sticky=W)
pic_plus7.grid(row=7,column=2,padx=10, sticky=W)
pic_plus8.grid(row=7,column=3,padx=10, sticky=W)

#space_plus1.grid(row=5,column=0,padx=10, sticky=W)
space_plus2.grid(row=9,column=0,padx=10, sticky=W)

pic_plus1['bg'] = 'white'
pic_plus2['bg'] = 'white'
pic_plus3['bg'] = 'white'
pic_plus4['bg'] = 'white'
pic_plus5['bg'] = 'white'
pic_plus6['bg'] = 'white'
pic_plus7['bg'] = 'white'
pic_plus8['bg'] = 'white'

#space_plus1['bg'] = 'white'
space_plus2['bg'] = 'white'



#名稱位置
name_plus.grid(row=1,column=0,padx=10, sticky=W)
name_plus1.grid(row=2,column=0,padx=10, sticky=W)
name_plus2.grid(row=2,column=1,padx=10, sticky=W)
name_plus3.grid(row=2,column=2,padx=10, sticky=W)
name_plus4.grid(row=2,column=3,padx=10, sticky=W)
name_plus5.grid(row=6,column=0,padx=10, sticky=W)
name_plus6.grid(row=6,column=1,padx=10, sticky=W)
name_plus7.grid(row=6,column=2,padx=10, sticky=W)
name_plus8.grid(row=6,column=3,padx=10, sticky=W)

name_plus['bg'] = 'yellow'
name_plus1['bg'] = 'white'
name_plus2['bg'] = 'white'
name_plus3['bg'] = 'white'
name_plus4['bg'] = 'white'
name_plus5['bg'] = 'white'
name_plus6['bg'] = 'white'
name_plus7['bg'] = 'white'
name_plus8['bg'] = 'white'

#飲料
name_plusd = tk.Label(win2, text='1+1飲料區',font=('微軟正黑體',12), anchor='w')
name_plusd1 = tk.Label(win2, text='1、可樂(小)',font=('微軟正黑體',12), anchor='center')
name_plusd2 = tk.Label(win2, text='2、可樂zero(小)',font=('微軟正黑體',12), anchor='center')
name_plusd3 = tk.Label(win2, text='3、雪碧(小)',font=('微軟正黑體',12), anchor='center')
name_plusd4 = tk.Label(win2, text='4、檸檬紅茶(小)',font=('微軟正黑體',12), anchor='center')
name_plusd5 = tk.Label(win2, text='5、無糖紅茶(小)',font=('微軟正黑體',12), anchor='center')
name_plusd6 = tk.Label(win2, text='6、無糖綠茶(小)',font=('微軟正黑體',12), anchor='center')
name_plusd7 = tk.Label(win2, text='7、熱紅茶(小)',font=('微軟正黑體',12), anchor='center')
name_plusd8 = tk.Label(win2, text='8、玉米湯(小)',font=('微軟正黑體',12), anchor='center')

#space_plusd1 = tk.Label(win2, text=' ',font=('微軟正黑體',14), anchor='w')
space_plusd2 = tk.Label(win2, text=' ',font=('微軟正黑體',14), anchor='w')



name_plusd.grid(row=10,column=0,padx=10, sticky=W)
name_plusd1.grid(row=11,column=0,padx=10, sticky=W+E)
name_plusd2.grid(row=11,column=1,padx=10, sticky=W+E)
name_plusd3.grid(row=11,column=2,padx=10, sticky=W+E)
name_plusd4.grid(row=11,column=3,padx=10, sticky=W+E)
name_plusd5.grid(row=14,column=0,padx=10, sticky=W+E)
name_plusd6.grid(row=14,column=1,padx=10, sticky=W+E)
name_plusd7.grid(row=14,column=2,padx=10, sticky=W+E)
name_plusd8.grid(row=14,column=3,padx=10, sticky=W+E)


#space_plusd1.grid(row=9,column=0,padx=10, sticky=W)
space_plusd2.grid(row=13,column=0,padx=10, sticky=W)



name_plusd['bg'] = 'yellow'
name_plusd1['bg'] = 'white'
name_plusd2['bg'] = 'white'
name_plusd3['bg'] = 'white'
name_plusd4['bg'] = 'white'
name_plusd5['bg'] = 'white'
name_plusd6['bg'] = 'white'
name_plusd7['bg'] = 'white'
name_plusd8['bg'] = 'white'

#space_plusd1['bg'] = 'white'
space_plusd2['bg'] = 'white'






# Text 輸入數量
text_plus1 = tk.Text(win2, width = 5,height = 1)
text_plus2 = tk.Text(win2, width = 5,height = 1)
text_plus3 = tk.Text(win2, width = 5,height = 1)
text_plus4 = tk.Text(win2, width = 5,height = 1)
text_plus5 = tk.Text(win2, width = 5,height = 1)
text_plus6 = tk.Text(win2, width = 5,height = 1)
text_plus7 = tk.Text(win2, width = 5,height = 1)
text_plus8 = tk.Text(win2, width = 5,height = 1)

text_plusd1 = tk.Text(win2, width = 5,height = 1)
text_plusd2 = tk.Text(win2, width = 5,height = 1)
text_plusd3 = tk.Text(win2, width = 5,height = 1)
text_plusd4 = tk.Text(win2, width = 5,height = 1)
text_plusd5 = tk.Text(win2, width = 5,height = 1)
text_plusd6 = tk.Text(win2, width = 5,height = 1)
text_plusd7 = tk.Text(win2, width = 5,height = 1)
text_plusd8 = tk.Text(win2, width = 5,height = 1)


# Text 位置
text_plus1.grid(row=4,column=0,padx=10)
text_plus2.grid(row=4,column=1,padx=10)
text_plus3.grid(row=4,column=2,padx=10)
text_plus4.grid(row=4,column=3,padx=10)
text_plus5.grid(row=8,column=0,padx=10)
text_plus6.grid(row=8,column=1,padx=10)
text_plus7.grid(row=8,column=2,padx=10)
text_plus8.grid(row=8,column=3,padx=10)

text_plusd1.grid(row=12,column=0,padx=10)
text_plusd2.grid(row=12,column=1,padx=10)
text_plusd3.grid(row=12,column=2,padx=10)
text_plusd4.grid(row=12,column=3,padx=10)
text_plusd5.grid(row=15,column=0,padx=10)
text_plusd6.grid(row=15,column=1,padx=10)
text_plusd7.grid(row=15,column=2,padx=10)
text_plusd8.grid(row=15,column=3,padx=10)


text_plus1.insert(tk.INSERT,"0")
text_plus2.insert(tk.INSERT,"0")
text_plus3.insert(tk.INSERT,"0")
text_plus4.insert(tk.INSERT,"0")
text_plus5.insert(tk.INSERT,"0")
text_plus6.insert(tk.INSERT,"0")
text_plus7.insert(tk.INSERT,"0")
text_plus8.insert(tk.INSERT,"0")

text_plusd1.insert(tk.INSERT,"0")
text_plusd2.insert(tk.INSERT,"0")
text_plusd3.insert(tk.INSERT,"0")
text_plusd4.insert(tk.INSERT,"0")
text_plusd5.insert(tk.INSERT,"0")
text_plusd6.insert(tk.INSERT,"0")
text_plusd7.insert(tk.INSERT,"0")
text_plusd8.insert(tk.INSERT,"0")



text_plus1['bg'] = 'WhiteSmoke'
text_plus2['bg'] = 'WhiteSmoke'
text_plus3['bg'] = 'WhiteSmoke'
text_plus4['bg'] = 'WhiteSmoke'
text_plus5['bg'] = 'WhiteSmoke'
text_plus6['bg'] = 'WhiteSmoke'
text_plus7['bg'] = 'WhiteSmoke'
text_plus8['bg'] = 'WhiteSmoke'

text_plusd1['bg'] = 'WhiteSmoke'
text_plusd2['bg'] = 'WhiteSmoke'
text_plusd3['bg'] = 'WhiteSmoke'
text_plusd4['bg'] = 'WhiteSmoke'
text_plusd5['bg'] = 'WhiteSmoke'
text_plusd6['bg'] = 'WhiteSmoke'
text_plusd7['bg'] = 'WhiteSmoke'
text_plusd8['bg'] = 'WhiteSmoke'



# In[4]:


# ----------------------點心----------------------


# Label
title_s = tk.Label(win3, text='點心',font=('微軟正黑體',16))
title_s.grid(row=1,column=0,padx=5,pady=5, sticky=W)
title_s['bg'] = 'OrangeRed2'
capation_s = tk.Label(win3, text='*本頁面僅供單點、超值全餐組合與超值加點，不含主餐與1+1*',font=('微軟正黑體',12))
capation_s.grid(row=1,column=1,columnspan=20,padx=5,pady=5, sticky=W)
capation_s['bg'] = 'white'

#讀取食物照片 + 調整圖片大小
s1= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/snack/hamburger.jpeg")).resize((120, 120), Image.ANTIALIAS))
s2= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/cheeseburger.jpeg')).resize((120, 120), Image.ANTIALIAS))
s3= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/sweetpotato.jpeg')).resize((120, 120), Image.ANTIALIAS))
s4= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/frenchfriessmall.jpeg')).resize((120, 120), Image.ANTIALIAS))
s5= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/frenchfriesmed.jpeg')).resize((120, 120), Image.ANTIALIAS))
s6= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/frenchfrieslarge.jpeg')).resize((120, 120), Image.ANTIALIAS))
s7= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/hashbrowns.jpeg')).resize((120, 120), Image.ANTIALIAS))
s8= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/spicychickenwing.jpeg')).resize((120, 120), Image.ANTIALIAS))
s9= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/spicychickenwing6.jpeg')).resize((120, 120), Image.ANTIALIAS))
s10= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/tenderchickenwing2.jpeg')).resize((120, 120), Image.ANTIALIAS))
s11= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/tenderchickenwing6.jpeg')).resize((120, 120), Image.ANTIALIAS))
s12= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/applepie.jpeg')).resize((120, 120), Image.ANTIALIAS))
s13= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/mcflurry.jpeg')).resize((120, 120), Image.ANTIALIAS))
s14= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/saladlarge.jpeg')).resize((120, 120), Image.ANTIALIAS))
s15= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/slicedapple.jpeg')).resize((120, 120), Image.ANTIALIAS))
s16= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/cornsoupsmall.jpeg')).resize((120, 120), Image.ANTIALIAS))
s17= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/cornsouplarge.jpeg')).resize((120, 120), Image.ANTIALIAS))
s18= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/icecreamcone.jpeg')).resize((120, 120), Image.ANTIALIAS))
s19= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/icecreamconelarge.jpeg')).resize((120, 120), Image.ANTIALIAS))
s20= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/chickenmcnuggets4.jpeg')).resize((120, 120), Image.ANTIALIAS))
s21= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/chickenmcnuggets6.jpeg')).resize((120, 120), Image.ANTIALIAS))
s22= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/chickenmcnuggets10.jpeg')).resize((120, 120), Image.ANTIALIAS))
s23= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/macchicken.jpeg')).resize((100, 100), Image.ANTIALIAS))
s24= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/snack/macchicken_spicy.jpeg')).resize((100, 100), Image.ANTIALIAS))


pic_s1= tk.Label(win3,image = s1)
pic_s2= tk.Label(win3,image = s2)
pic_s3= tk.Label(win3,image = s3)
pic_s4= tk.Label(win3,image = s4)
pic_s5= tk.Label(win3,image = s5)
pic_s6= tk.Label(win3,image = s6)
pic_s7= tk.Label(win3,image = s7)
pic_s8= tk.Label(win3,image = s8)
pic_s9= tk.Label(win3,image = s9)
pic_s10= tk.Label(win3,image = s10)
pic_s11= tk.Label(win3,image = s11)
pic_s12= tk.Label(win3,image = s12)
pic_s13= tk.Label(win3,image = s13)
pic_s14= tk.Label(win3,image = s14)
pic_s15= tk.Label(win3,image = s15)
pic_s16= tk.Label(win3,image = s16)
pic_s17= tk.Label(win3,image = s17)
pic_s18= tk.Label(win3,image = s18)
pic_s19= tk.Label(win3,image = s19)
pic_s20= tk.Label(win3,image = s20)
pic_s21= tk.Label(win3,image = s21)
pic_s22= tk.Label(win3,image = s22)
pic_s23= tk.Label(win3,image = s23)
pic_s24= tk.Label(win3,image = s24)


#食物名稱
name_s1 = tk.Label(win3, text='1、漢堡',font=('微軟正黑體',12), anchor='w')
name_s2 = tk.Label(win3, text='2、吉事漢堡',font=('微軟正黑體',12), anchor='w')
name_s3 = tk.Label(win3, text='3、黃金地瓜條',font=('微軟正黑體',12), anchor='w')
name_s4 = tk.Label(win3, text='4、薯條(小)',font=('微軟正黑體',12), anchor='w')
name_s5 = tk.Label(win3, text='5、薯條(中)',font=('微軟正黑體',12), anchor='w')
name_s6 = tk.Label(win3, text='6、薯條(大)',font=('微軟正黑體',12), anchor='w')
name_s7 = tk.Label(win3, text='7、薯餅',font=('微軟正黑體',12), anchor='w')
name_s8 = tk.Label(win3, text='8、勁辣香鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')
name_s9 = tk.Label(win3, text='9、勁辣香鷄翅(6塊)',font=('微軟正黑體',12), anchor='w')
name_s10 = tk.Label(win3, text='10、酥嫩鷄翅(2塊)',font=('微軟正黑體',12), anchor='w')
name_s11 = tk.Label(win3, text='11、酥嫩鷄翅(6塊)',font=('微軟正黑體',12), anchor='w')
name_s12 = tk.Label(win3, text='12、蘋果派',font=('微軟正黑體',12), anchor='w')
name_s13 = tk.Label(win3, text='13、冰炫風(OREO)',font=('微軟正黑體',12), anchor='w')
name_s14 = tk.Label(win3, text='14、四季沙拉',font=('微軟正黑體',12), anchor='w')
name_s15 = tk.Label(win3, text='15、水果袋',font=('微軟正黑體',12), anchor='w')
name_s16 = tk.Label(win3, text='16、玉米湯(小)',font=('微軟正黑體',12), anchor='w')
name_s17 = tk.Label(win3, text='17、玉米湯(大)',font=('微軟正黑體',12), anchor='w')
name_s18 = tk.Label(win3, text='18、蛋捲冰淇淋',font=('微軟正黑體',12), anchor='w')
name_s19 = tk.Label(win3, text='19、大蛋捲冰淇淋',font=('微軟正黑體',12), anchor='w')
name_s20 = tk.Label(win3, text='20、麥克雞塊(4塊)',font=('微軟正黑體',12), anchor='w')
name_s21 = tk.Label(win3, text='21、麥克雞塊(6塊)',font=('微軟正黑體',12), anchor='w')
name_s22 = tk.Label(win3, text='22、麥克雞塊(10塊)',font=('微軟正黑體',12), anchor='w')
name_s23 = tk.Label(win3, text='23、原味麥脆雞腿',font=('微軟正黑體',12), anchor='w')
name_s24 = tk.Label(win3, text='24、辣味麥脆雞腿',font=('微軟正黑體',12), anchor='w')

#space_s1 = tk.Label(win3, text=' ',font=('微軟正黑體',14), anchor='w')
#space_s2 = tk.Label(win3, text=' ',font=('微軟正黑體',14), anchor='w')
#space_s3 = tk.Label(win3, text=' ',font=('微軟正黑體',14), anchor='w')

#照片位置

pic_s1.grid(row=3,column=0,padx=10, sticky=W)
pic_s2.grid(row=3,column=1,padx=10, sticky=W)
pic_s3.grid(row=3,column=2,padx=10, sticky=W)
pic_s4.grid(row=3,column=3,padx=10, sticky=W)
pic_s5.grid(row=3,column=4,padx=10, sticky=W)
pic_s6.grid(row=3,column=5,padx=10, sticky=W)
pic_s7.grid(row=7,column=0,padx=10, sticky=W)
pic_s8.grid(row=7,column=1,padx=10, sticky=W)
pic_s9.grid(row=7,column=2,padx=10, sticky=W)
pic_s10.grid(row=7,column=3,padx=10, sticky=W)
pic_s11.grid(row=7,column=4,padx=10, sticky=W)
pic_s12.grid(row=7,column=5,padx=10, sticky=W)
pic_s13.grid(row=11,column=0,padx=10, sticky=W)
pic_s14.grid(row=11,column=1,padx=10, sticky=W)
pic_s15.grid(row=11,column=2,padx=10, sticky=W)
pic_s16.grid(row=11,column=3,padx=10, sticky=W)
pic_s17.grid(row=11,column=4,padx=10, sticky=W)
pic_s18.grid(row=11,column=5,padx=10, sticky=W)
pic_s19.grid(row=15,column=0,padx=10, sticky=W)
pic_s20.grid(row=15,column=1,padx=10, sticky=W)
pic_s21.grid(row=15,column=2,padx=10, sticky=W)
pic_s22.grid(row=15,column=3,padx=10, sticky=W)
pic_s23.grid(row=15,column=4,padx=10, sticky=W)
pic_s24.grid(row=15,column=5,padx=10, sticky=W)

#space_s1.grid(row=5,column=0,padx=10, sticky=W)
#space_s2.grid(row=9,column=0,padx=10, sticky=W)
#space_s3.grid(row=13,column=0,padx=10, sticky=W)


pic_s1['bg'] = 'white'
pic_s2['bg'] = 'white'
pic_s3['bg'] = 'white'
pic_s4['bg'] = 'white'
pic_s5['bg'] = 'white'
pic_s6['bg'] = 'white'
pic_s7['bg'] = 'white'
pic_s8['bg'] = 'white'
pic_s9['bg'] = 'white'
pic_s10['bg'] = 'white'
pic_s11['bg'] = 'white'
pic_s12['bg'] = 'white'
pic_s13['bg'] = 'white'
pic_s14['bg'] = 'white'
pic_s15['bg'] = 'white'
pic_s16['bg'] = 'white'
pic_s17['bg'] = 'white'
pic_s18['bg'] = 'white'
pic_s19['bg'] = 'white'
pic_s20['bg'] = 'white'
pic_s21['bg'] = 'white'
pic_s22['bg'] = 'white'
pic_s23['bg'] = 'white'
pic_s24['bg'] = 'white'

#space_s1['bg'] = 'white'
#space_s2['bg'] = 'white'
#space_s3['bg'] = 'white'


#名稱位置

name_s1.grid(row=2,column=0,padx=10, sticky=W)
name_s2.grid(row=2,column=1,padx=10, sticky=W)
name_s3.grid(row=2,column=2,padx=10, sticky=W)
name_s4.grid(row=2,column=3,padx=10, sticky=W)
name_s5.grid(row=2,column=4,padx=10, sticky=W)
name_s6.grid(row=2,column=5,padx=10, sticky=W)
name_s7.grid(row=6,column=0,padx=10, sticky=W)
name_s8.grid(row=6,column=1,padx=10, sticky=W)
name_s9.grid(row=6,column=2,padx=10, sticky=W)
name_s10.grid(row=6,column=3,padx=10, sticky=W)
name_s11.grid(row=6,column=4,padx=10, sticky=W)
name_s12.grid(row=6,column=5,padx=10, sticky=W)
name_s13.grid(row=10,column=0,padx=10, sticky=W)
name_s14.grid(row=10,column=1,padx=10, sticky=W)
name_s15.grid(row=10,column=2,padx=10, sticky=W)
name_s16.grid(row=10,column=3,padx=10, sticky=W)
name_s17.grid(row=10,column=4,padx=10, sticky=W)
name_s18.grid(row=10,column=5,padx=10, sticky=W)
name_s19.grid(row=14,column=0,padx=10, sticky=W)
name_s20.grid(row=14,column=1,padx=10, sticky=W)
name_s21.grid(row=14,column=2,padx=10, sticky=W)
name_s22.grid(row=14,column=3,padx=10, sticky=W)
name_s23.grid(row=14,column=4,padx=10, sticky=W)
name_s24.grid(row=14,column=5,padx=10, sticky=W)

name_s1['bg'] = 'white'
name_s2['bg'] = 'white'
name_s3['bg'] = 'white'
name_s4['bg'] = 'white'
name_s5['bg'] = 'white'
name_s6['bg'] = 'white'
name_s7['bg'] = 'white'
name_s8['bg'] = 'white'
name_s9['bg'] = 'white'
name_s10['bg'] = 'white'
name_s11['bg'] = 'white'
name_s12['bg'] = 'white'
name_s13['bg'] = 'white'
name_s14['bg'] = 'white'
name_s15['bg'] = 'white'
name_s16['bg'] = 'white'
name_s17['bg'] = 'white'
name_s18['bg'] = 'white'
name_s19['bg'] = 'white'
name_s20['bg'] = 'white'
name_s21['bg'] = 'white'
name_s22['bg'] = 'white'
name_s23['bg'] = 'white'
name_s24['bg'] = 'white'


# Text 輸入數量
text_s1 = tk.Text(win3, width = 5,height = 1)
text_s2 = tk.Text(win3, width = 5,height = 1)
text_s3 = tk.Text(win3, width = 5,height = 1)
text_s4 = tk.Text(win3, width = 5,height = 1)
text_s5 = tk.Text(win3, width = 5,height = 1)
text_s6 = tk.Text(win3, width = 5,height = 1)
text_s7 = tk.Text(win3, width = 5,height = 1)
text_s8 = tk.Text(win3, width = 5,height = 1)
text_s9 = tk.Text(win3, width = 5,height = 1)
text_s10 = tk.Text(win3, width = 5,height = 1)
text_s11 = tk.Text(win3, width = 5,height = 1)
text_s12 = tk.Text(win3, width = 5,height = 1)
text_s13 = tk.Text(win3, width = 5,height = 1)
text_s14 = tk.Text(win3, width = 5,height = 1)
text_s15 = tk.Text(win3, width = 5,height = 1)
text_s16 = tk.Text(win3, width = 5,height = 1)
text_s17 = tk.Text(win3, width = 5,height = 1)
text_s18 = tk.Text(win3, width = 5,height = 1)
text_s19 = tk.Text(win3, width = 5,height = 1)
text_s20 = tk.Text(win3, width = 5,height = 1)
text_s21 = tk.Text(win3, width = 5,height = 1)
text_s22 = tk.Text(win3, width = 5,height = 1)
text_s23 = tk.Text(win3, width = 5,height = 1)
text_s24 = tk.Text(win3, width = 5,height = 1)


# Text 位置
text_s1.grid(row=4,column=0,padx=10)
text_s2.grid(row=4,column=1,padx=10)
text_s3.grid(row=4,column=2,padx=10)
text_s4.grid(row=4,column=3,padx=10)
text_s5.grid(row=4,column=4,padx=10)
text_s6.grid(row=4,column=5,padx=10)
text_s7.grid(row=8,column=0,padx=10)
text_s8.grid(row=8,column=1,padx=10)
text_s9.grid(row=8,column=2,padx=10)
text_s10.grid(row=8,column=3,padx=10)
text_s11.grid(row=8,column=4,padx=10)
text_s12.grid(row=8,column=5,padx=10)
text_s13.grid(row=12,column=0,padx=10)
text_s14.grid(row=12,column=1,padx=10)
text_s15.grid(row=12,column=2,padx=10)
text_s16.grid(row=12,column=3,padx=10)
text_s17.grid(row=12,column=4,padx=10)
text_s18.grid(row=12,column=5,padx=10)
text_s19.grid(row=16,column=0,padx=10)
text_s20.grid(row=16,column=1,padx=10)
text_s21.grid(row=16,column=2,padx=10)
text_s22.grid(row=16,column=3,padx=10)
text_s23.grid(row=16,column=4,padx=10)
text_s24.grid(row=16,column=5,padx=10)

text_s1.insert(tk.INSERT,"0")
text_s2.insert(tk.INSERT,"0")
text_s3.insert(tk.INSERT,"0")
text_s4.insert(tk.INSERT,"0")
text_s5.insert(tk.INSERT,"0")
text_s6.insert(tk.INSERT,"0")
text_s7.insert(tk.INSERT,"0")
text_s8.insert(tk.INSERT,"0")
text_s9.insert(tk.INSERT,"0")
text_s10.insert(tk.INSERT,"0")
text_s11.insert(tk.INSERT,"0")
text_s12.insert(tk.INSERT,"0")
text_s13.insert(tk.INSERT,"0")
text_s14.insert(tk.INSERT,"0")
text_s15.insert(tk.INSERT,"0")
text_s16.insert(tk.INSERT,"0")
text_s17.insert(tk.INSERT,"0")
text_s18.insert(tk.INSERT,"0")
text_s19.insert(tk.INSERT,"0")
text_s20.insert(tk.INSERT,"0")
text_s21.insert(tk.INSERT,"0")
text_s22.insert(tk.INSERT,"0")
text_s23.insert(tk.INSERT,"0")
text_s24.insert(tk.INSERT,"0")



text_s1['bg'] = 'WhiteSmoke'
text_s2['bg'] = 'WhiteSmoke'
text_s3['bg'] = 'WhiteSmoke'
text_s4['bg'] = 'WhiteSmoke'
text_s5['bg'] = 'WhiteSmoke'
text_s6['bg'] = 'WhiteSmoke'
text_s7['bg'] = 'WhiteSmoke'
text_s8['bg'] = 'WhiteSmoke'
text_s9['bg'] = 'WhiteSmoke'
text_s10['bg'] = 'WhiteSmoke'
text_s11['bg'] = 'WhiteSmoke'
text_s12['bg'] = 'WhiteSmoke'
text_s13['bg'] = 'WhiteSmoke'
text_s14['bg'] = 'WhiteSmoke'
text_s15['bg'] = 'WhiteSmoke'
text_s16['bg'] = 'WhiteSmoke'
text_s17['bg'] = 'WhiteSmoke'
text_s18['bg'] = 'WhiteSmoke'
text_s19['bg'] = 'WhiteSmoke'
text_s20['bg'] = 'WhiteSmoke'
text_s21['bg'] = 'WhiteSmoke'
text_s22['bg'] = 'WhiteSmoke'
text_s23['bg'] = 'WhiteSmoke'
text_s24['bg'] = 'WhiteSmoke'


# In[5]:


# ----------------------飲料/配餐說明----------------------

# Label
title_d = tk.Label(win4, text='飲料/配餐說明',font=('微軟正黑體',16))
title_d.grid(row=0,column=0,padx=5,pady=5, sticky=W)
title_d['bg'] = 'OrangeRed2'
capation_d = tk.Label(win4, text='*括弧內為單點價格*',font=('微軟正黑體',12))
capation_d.grid(row=0,column=1,columnspan=20,padx=5,pady=5, sticky=W)
capation_d['bg'] = 'white'

size_d = 100
#讀取食物照片 + 調整圖片大小
d1= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/drink/blacktea_nosugar.jpeg")).resize((size_d, size_d), Image.ANTIALIAS))
d2= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/greentea_nosugar.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d3= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/cola.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d4= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/lemonblacktea.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d5= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/sprite.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d6= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/zerocola.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d7= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/orangejuice.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d8= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/hotmilktea.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d9= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/hotblacktea.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d10= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/coldmilktea.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))
d11= ImageTk.PhotoImage(Image.open(os.path.relpath('picture/drink/milk.jpeg')).resize((size_d, size_d), Image.ANTIALIAS))


pic_d1= tk.Label(win4,image = d1)
pic_d2= tk.Label(win4,image = d2)
pic_d3= tk.Label(win4,image = d3)
pic_d4= tk.Label(win4,image = d4)
pic_d5= tk.Label(win4,image = d5)
pic_d6= tk.Label(win4,image = d6)
pic_d7= tk.Label(win4,image = d7)
pic_d8= tk.Label(win4,image = d8)
pic_d9= tk.Label(win4,image = d9)
pic_d10= tk.Label(win4,image = d10)
pic_d11= tk.Label(win4,image = d11)



#飲料小杯
name_d = tk.Label(win4, text='飲料區',font=('微軟正黑體',12), anchor='w')
name_d1_1 = tk.Label(win4, text='無糖冰紅茶\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d2_1 = tk.Label(win4, text='無糖冰綠茶\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d3_1 = tk.Label(win4, text='可口可樂\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d4_1 = tk.Label(win4, text='檸檬紅茶\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d5_1 = tk.Label(win4, text='雪碧\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d6_1 = tk.Label(win4, text='零卡可樂\n小(33元)',font=('微軟正黑體',12), anchor='w')
name_d7_1 = tk.Label(win4, text='柳橙汁\n(55元)',font=('微軟正黑體',12), anchor='w')
name_d8_1 = tk.Label(win4, text='熱奶茶\n小(38元)',font=('微軟正黑體',12), anchor='w')
name_d9_1 = tk.Label(win4, text='熱紅茶\n(38元)',font=('微軟正黑體',12), anchor='w')
name_d10_1 = tk.Label(win4, text='冰奶茶\n小(38元)',font=('微軟正黑體',12), anchor='w')
name_d11_1 = tk.Label(win4, text='鮮乳\n(33元)',font=('微軟正黑體',12), anchor='w')

#中杯
name_d1_2 = tk.Label(win4, text='無糖冰紅茶\n中(38元)',font=('微軟正黑體',12), anchor='w')
name_d2_2 = tk.Label(win4, text='無糖冰綠茶\n中(38元)',font=('微軟正黑體',12), anchor='w')
name_d3_2 = tk.Label(win4, text='可口可樂\n中(38元)',font=('微軟正黑體',12), anchor='w')
name_d4_2 = tk.Label(win4, text='檸檬紅茶\n中(38元)',font=('微軟正黑體',12), anchor='w')
name_d5_2 = tk.Label(win4, text='雪碧\n小(38元)',font=('微軟正黑體',12), anchor='w')
name_d6_2 = tk.Label(win4, text='零卡可樂\n中(38元)',font=('微軟正黑體',12), anchor='w')
name_d8_2 = tk.Label(win4, text='熱奶茶\n中(48元)',font=('微軟正黑體',12), anchor='w')

#大杯
name_d1_3 = tk.Label(win4, text='無糖冰紅茶\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d2_3 = tk.Label(win4, text='無糖冰綠茶\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d3_3 = tk.Label(win4, text='可口可樂\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d4_3 = tk.Label(win4, text='檸檬紅茶\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d5_3 = tk.Label(win4, text='雪碧\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d6_3 = tk.Label(win4, text='零卡可樂\n大(45元)',font=('微軟正黑體',12), anchor='w')
name_d10_3 = tk.Label(win4, text='冰奶茶\n大(48元)',font=('微軟正黑體',12), anchor='w')


#照片位置

pic_d1.grid(row=2,rowspan=2,column=0,padx=10, sticky=W)
pic_d2.grid(row=2,rowspan=2,column=4,padx=10, sticky=W)
pic_d3.grid(row=4,rowspan=2,column=0,padx=10, sticky=W)
pic_d4.grid(row=4,rowspan=2,column=4,padx=10, sticky=W)
pic_d5.grid(row=6,rowspan=2,column=0,padx=10, sticky=W)
pic_d6.grid(row=6,rowspan=2,column=4,padx=10, sticky=W)
pic_d7.grid(row=8,rowspan=2,column=0,padx=10, sticky=W)
pic_d8.grid(row=8,rowspan=2,column=4,padx=10, sticky=W)
pic_d9.grid(row=10,rowspan=2,column=0,padx=10, sticky=W)
pic_d10.grid(row=10,rowspan=2,column=4,padx=10, sticky=W)
pic_d11.grid(row=12,rowspan=2,column=0,padx=10, sticky=W)


pic_d1['bg'] = 'white'
pic_d2['bg'] = 'white'
pic_d3['bg'] = 'white'
pic_d4['bg'] = 'white'
pic_d5['bg'] = 'white'
pic_d6['bg'] = 'white'
pic_d7['bg'] = 'white'
pic_d8['bg'] = 'white'
pic_d9['bg'] = 'white'
pic_d10['bg'] = 'white'
pic_d11['bg'] = 'white'



#名稱位置
name_d.grid(row=1,column=0,padx=10, sticky=W)
name_d1_1.grid(row=2,column=1,padx=10, sticky=W)    #1
name_d1_2.grid(row=2,column=2,padx=10, sticky=W)
name_d1_3.grid(row=2,column=3,padx=10, sticky=W)
name_d2_1.grid(row=2,column=5,padx=10, sticky=W)    #2
name_d2_2.grid(row=2,column=6,padx=10, sticky=W)
name_d2_3.grid(row=2,column=7,padx=10, sticky=W)
name_d3_1.grid(row=4,column=1,padx=10, sticky=W)    #3
name_d3_2.grid(row=4,column=2,padx=10, sticky=W)
name_d3_3.grid(row=4,column=3,padx=10, sticky=W)
name_d4_1.grid(row=4,column=5,padx=10, sticky=W)    #4
name_d4_2.grid(row=4,column=6,padx=10, sticky=W)
name_d4_3.grid(row=4,column=7,padx=10, sticky=W)
name_d5_1.grid(row=6,column=1,padx=10, sticky=W)    #5
name_d5_2.grid(row=6,column=2,padx=10, sticky=W)
name_d5_3.grid(row=6,column=3,padx=10, sticky=W)
name_d6_1.grid(row=6,column=5,padx=10, sticky=W)    #6
name_d6_2.grid(row=6,column=6,padx=10, sticky=W)
name_d6_3.grid(row=6,column=7,padx=10, sticky=W)
name_d7_1.grid(row=8,column=1,padx=10, sticky=W)    #7
name_d8_1.grid(row=8,column=5,padx=10, sticky=W)    #8
name_d8_2.grid(row=8,column=6,padx=10, sticky=W)
name_d9_1.grid(row=10,column=1,padx=10, sticky=W)    #9
name_d10_1.grid(row=10,column=5,padx=10, sticky=W)   #10
#name_d10_2.grid(row=10,column=6,padx=10, sticky=W)
name_d10_3.grid(row=10,column=7,padx=10, sticky=W)
name_d11_1.grid(row=12,column=1,padx=10, sticky=W)   #11





name_d['bg'] = 'yellow'
name_d1_1['bg'] = 'white'
name_d1_2['bg'] = 'white'
name_d1_3['bg'] = 'white'
name_d2_1['bg'] = 'white'
name_d2_2['bg'] = 'white'
name_d2_3['bg'] = 'white'
name_d3_1['bg'] = 'white'
name_d3_2['bg'] = 'white'
name_d3_3['bg'] = 'white'
name_d4_1['bg'] = 'white'
name_d4_2['bg'] = 'white'
name_d4_3['bg'] = 'white'
name_d5_1['bg'] = 'white'
name_d5_2['bg'] = 'white'
name_d5_3['bg'] = 'white'
name_d6_1['bg'] = 'white'
name_d6_2['bg'] = 'white'
name_d6_3['bg'] = 'white'
name_d7_1['bg'] = 'white'
name_d8_1['bg'] = 'white'
name_d8_2['bg'] = 'white'
name_d9_1['bg'] = 'white'
name_d10_1['bg'] = 'white'
#name_d10_2['bg'] = 'white'
name_d10_3['bg'] = 'white'
name_d11_1['bg'] = 'white'






# Text 輸入數量
text_d1_1 = tk.Text(win4, width = 5,height = 1)
text_d1_2 = tk.Text(win4, width = 5,height = 1)
text_d1_3 = tk.Text(win4, width = 5,height = 1)
text_d2_1 = tk.Text(win4, width = 5,height = 1)
text_d2_2 = tk.Text(win4, width = 5,height = 1)
text_d2_3 = tk.Text(win4, width = 5,height = 1)
text_d3_1 = tk.Text(win4, width = 5,height = 1)
text_d3_2 = tk.Text(win4, width = 5,height = 1)
text_d3_3 = tk.Text(win4, width = 5,height = 1)
text_d4_1 = tk.Text(win4, width = 5,height = 1)
text_d4_2 = tk.Text(win4, width = 5,height = 1)
text_d4_3 = tk.Text(win4, width = 5,height = 1)
text_d5_1 = tk.Text(win4, width = 5,height = 1)
text_d5_2 = tk.Text(win4, width = 5,height = 1)
text_d5_3 = tk.Text(win4, width = 5,height = 1)
text_d6_1 = tk.Text(win4, width = 5,height = 1)
text_d6_2 = tk.Text(win4, width = 5,height = 1)
text_d6_3 = tk.Text(win4, width = 5,height = 1)
text_d7_1 = tk.Text(win4, width = 5,height = 1)
text_d8_1 = tk.Text(win4, width = 5,height = 1)
text_d8_2 = tk.Text(win4, width = 5,height = 1)
text_d9_1 = tk.Text(win4, width = 5,height = 1)
text_d10_1 = tk.Text(win4, width = 5,height = 1)
text_d10_3 = tk.Text(win4, width = 5,height = 1)
text_d11_1 = tk.Text(win4, width = 5,height = 1)


# Text 位置
text_d1_1.grid(row=3,column=1,padx=10 ,sticky=W)
text_d1_2.grid(row=3,column=2,padx=10 ,sticky=W)
text_d1_3.grid(row=3,column=3,padx=10 ,sticky=W)
text_d2_1.grid(row=3,column=5,padx=10 ,sticky=W)
text_d2_2.grid(row=3,column=6,padx=10 ,sticky=W)
text_d2_3.grid(row=3,column=7,padx=10 ,sticky=W)
text_d3_1.grid(row=5,column=1,padx=10 ,sticky=W)
text_d3_2.grid(row=5,column=2,padx=10 ,sticky=W)
text_d3_3.grid(row=5,column=3,padx=10 ,sticky=W)
text_d4_1.grid(row=5,column=5,padx=10 ,sticky=W)
text_d4_2.grid(row=5,column=6,padx=10 ,sticky=W)
text_d4_3.grid(row=5,column=7,padx=10 ,sticky=W)
text_d5_1.grid(row=7,column=1,padx=10 ,sticky=W)
text_d5_2.grid(row=7,column=2,padx=10 ,sticky=W)
text_d5_3.grid(row=7,column=3,padx=10 ,sticky=W)
text_d6_1.grid(row=7,column=5,padx=10 ,sticky=W)
text_d6_2.grid(row=7,column=6,padx=10 ,sticky=W)
text_d6_3.grid(row=7,column=7,padx=10 ,sticky=W)
text_d7_1.grid(row=9,column=1,padx=10 ,sticky=W)
text_d8_1.grid(row=9,column=5,padx=10 ,sticky=W)
text_d8_2.grid(row=9,column=6,padx=10 ,sticky=W)
text_d9_1.grid(row=11,column=1,padx=10 ,sticky=W)
text_d10_1.grid(row=11,column=5,padx=10 ,sticky=W)
text_d10_3.grid(row=11,column=7,padx=10 ,sticky=W)
text_d11_1.grid(row=13,column=1,padx=10 ,sticky=W)

text_d1_1.insert(tk.INSERT,"0")
text_d1_2.insert(tk.INSERT,"0")
text_d1_3.insert(tk.INSERT,"0")
text_d2_1.insert(tk.INSERT,"0")
text_d2_2.insert(tk.INSERT,"0")
text_d2_3.insert(tk.INSERT,"0")
text_d3_1.insert(tk.INSERT,"0")
text_d3_2.insert(tk.INSERT,"0")
text_d3_3.insert(tk.INSERT,"0")
text_d4_1.insert(tk.INSERT,"0")
text_d4_2.insert(tk.INSERT,"0")
text_d4_3.insert(tk.INSERT,"0")
text_d5_1.insert(tk.INSERT,"0")
text_d5_2.insert(tk.INSERT,"0")
text_d5_3.insert(tk.INSERT,"0")
text_d6_1.insert(tk.INSERT,"0")
text_d6_2.insert(tk.INSERT,"0")
text_d6_3.insert(tk.INSERT,"0")
text_d7_1.insert(tk.INSERT,"0")
text_d8_1.insert(tk.INSERT,"0")
text_d8_2.insert(tk.INSERT,"0")
text_d9_1.insert(tk.INSERT,"0")
text_d10_1.insert(tk.INSERT,"0")
text_d10_3.insert(tk.INSERT,"0")
text_d11_1.insert(tk.INSERT,"0")


text_d1_1['bg'] = 'WhiteSmoke'
text_d1_2['bg'] = 'WhiteSmoke'
text_d1_3['bg'] = 'WhiteSmoke'
text_d2_1['bg'] = 'WhiteSmoke'
text_d2_2['bg'] = 'WhiteSmoke'
text_d2_3['bg'] = 'WhiteSmoke'
text_d3_1['bg'] = 'WhiteSmoke'
text_d3_2['bg'] = 'WhiteSmoke'
text_d3_3['bg'] = 'WhiteSmoke'
text_d4_1['bg'] = 'WhiteSmoke'
text_d4_2['bg'] = 'WhiteSmoke'
text_d4_3['bg'] = 'WhiteSmoke'
text_d5_1['bg'] = 'WhiteSmoke'
text_d5_2['bg'] = 'WhiteSmoke'
text_d5_3['bg'] = 'WhiteSmoke'
text_d6_1['bg'] = 'WhiteSmoke'
text_d6_2['bg'] = 'WhiteSmoke'
text_d6_3['bg'] = 'WhiteSmoke'
text_d7_1['bg'] = 'WhiteSmoke'
text_d8_1['bg'] = 'WhiteSmoke'
text_d8_2['bg'] = 'WhiteSmoke'
text_d9_1['bg'] = 'WhiteSmoke'
text_d10_1['bg'] = 'WhiteSmoke'
text_d10_3['bg'] = 'WhiteSmoke'
text_d11_1['bg'] = 'WhiteSmoke'


#配餐說明

side = tk.Label(win4, text='*超值全餐配餐說明：\nA.經典配餐(55元)：中薯+38元冷/熱飲(可加價升級大薯、其它飲料)\nB.清爽配餐(55元)：四季沙拉+38元冷/熱飲(可加價升級其它飲料)\nC.勁脆配餐(68元)：麥脆雞腿+38元冷/熱飲(可加價升級其它飲料)\nD.炫冰配餐(85元)：冰炫風(OREO)+小薯+38元冷/熱飲(可加價升級其它飲料)\nE.豪吃配餐(85元)：麥克雞塊(6塊)+小薯+38元冷/熱飲(可加價升級其它飲料)\nF.地瓜配餐(75元)：黃金地瓜條+38元冷/熱飲(可加價升級其它飲料)\n(請將數量分別輸入在單點空格中，如：經典配餐在中薯和中杯可樂的空格輸入數字)',font=('微軟正黑體',12), anchor='w')


side.grid(row=12,column=4,rowspan=3,columnspan=4,sticky=W)
side['bg'] = 'WhiteSmoke'


# In[6]:


#計算金額
def calculate():
    button.grid_forget()
    a = 0
    b = 0
    #主食
    num_m1 = int(text_m1.get("0.0","end").replace(" ","").replace("\n",""))
    num_m2 = int(text_m2.get("0.0","end").replace(" ","").replace("\n",""))
    num_m3 = int(text_m3.get("0.0","end").replace(" ","").replace("\n",""))
    num_m4 = int(text_m4.get("0.0","end").replace(" ","").replace("\n",""))
    num_m5 = int(text_m5.get("0.0","end").replace(" ","").replace("\n",""))
    num_m6 = int(text_m6.get("0.0","end").replace(" ","").replace("\n",""))
    num_m7 = int(text_m7.get("0.0","end").replace(" ","").replace("\n",""))
    num_m8 = int(text_m8.get("0.0","end").replace(" ","").replace("\n",""))
    num_m9 = int(text_m9.get("0.0","end").replace(" ","").replace("\n",""))
    num_m10 = int(text_m10.get("0.0","end").replace(" ","").replace("\n",""))
    num_m11 = int(text_m11.get("0.0","end").replace(" ","").replace("\n",""))
    num_m12 = int(text_m12.get("0.0","end").replace(" ","").replace("\n",""))
    num_m13 = int(text_m13.get("0.0","end").replace(" ","").replace("\n",""))
    num_m14 = int(text_m14.get("0.0","end").replace(" ","").replace("\n",""))
    num_m15 = int(text_m15.get("0.0","end").replace(" ","").replace("\n",""))
    num_m16 = int(text_m16.get("0.0","end").replace(" ","").replace("\n",""))
    num_m17 = int(text_m17.get("0.0","end").replace(" ","").replace("\n",""))
    num_m18 = int(text_m18.get("0.0","end").replace(" ","").replace("\n",""))

    meal_num = num_m1 + num_m2 + num_m3 + num_m4 + num_m5 + num_m6 + num_m7 + num_m8 + num_m9 + num_m10 + num_m11               + num_m12 + num_m13 + num_m14 + num_m15 + num_m16 + num_m17 + num_m18

    meal_money = num_m1*75 + num_m2*65 + num_m3*80 + num_m4*45 + num_m5*64 + num_m6*104 + num_m7*75 + num_m8*98                 + num_m9*98 + num_m10*120 + num_m11*120 + num_m12*49 + num_m13*124 + num_m14*114 + num_m15*114                 + num_m16*114 + num_m17*104 + num_m18*104

    #1+1
    num_plus1 = int(text_plus1.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus2 = int(text_plus2.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus3 = int(text_plus3.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus4 = int(text_plus4.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus5 = int(text_plus5.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus6 = int(text_plus6.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus7 = int(text_plus7.get("0.0","end").replace(" ","").replace("\n",""))
    num_plus8 = int(text_plus8.get("0.0","end").replace(" ","").replace("\n",""))

    num_plusd1 = int(text_plusd1.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd2 = int(text_plusd2.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd3 = int(text_plusd3.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd4 = int(text_plusd4.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd5 = int(text_plusd5.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd6 = int(text_plusd6.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd7 = int(text_plusd7.get("0.0","end").replace(" ","").replace("\n",""))
    num_plusd8 = int(text_plusd8.get("0.0","end").replace(" ","").replace("\n",""))

    plusfood_num = num_plus1 + num_plus2 + num_plus3 + num_plus4 + num_plus5 + num_plus6 + num_plus7 + num_plus8 
    plusdrink_num = num_plusd1 + num_plusd2 + num_plusd3 + num_plusd4 + num_plusd5 + num_plusd6 + num_plusd7 + num_plusd8 
    

    if plusfood_num == plusdrink_num:
        plus_money = plusfood_num*50
        a = 1
    else:
        warning = tk.Label(win5, text='錯誤：1+1區的食物總數量應等於飲品總數量，本次輸入的數量有錯，無法完成搭配，請重新輸入。',font=('微軟正黑體',14))
        warning.grid(row=4,column=0,columnspan=20,padx=10,pady=5, sticky=W)
        warning['bg'] = 'yellow'
        b = 1


    

    #點心
    num_s1 = int(text_s1.get("0.0","end").replace(" ","").replace("\n",""))
    num_s2 = int(text_s2.get("0.0","end").replace(" ","").replace("\n",""))
    num_s3 = int(text_s3.get("0.0","end").replace(" ","").replace("\n",""))
    num_s4 = int(text_s4.get("0.0","end").replace(" ","").replace("\n",""))
    num_s5 = int(text_s5.get("0.0","end").replace(" ","").replace("\n",""))
    num_s6 = int(text_s6.get("0.0","end").replace(" ","").replace("\n",""))
    num_s7 = int(text_s7.get("0.0","end").replace(" ","").replace("\n",""))
    num_s8 = int(text_s8.get("0.0","end").replace(" ","").replace("\n",""))
    num_s9 = int(text_s9.get("0.0","end").replace(" ","").replace("\n",""))
    num_s10 = int(text_s10.get("0.0","end").replace(" ","").replace("\n",""))
    num_s11 = int(text_s11.get("0.0","end").replace(" ","").replace("\n",""))
    num_s12 = int(text_s12.get("0.0","end").replace(" ","").replace("\n",""))
    num_s13 = int(text_s13.get("0.0","end").replace(" ","").replace("\n",""))
    num_s14 = int(text_s14.get("0.0","end").replace(" ","").replace("\n",""))
    num_s15 = int(text_s15.get("0.0","end").replace(" ","").replace("\n",""))
    num_s16 = int(text_s16.get("0.0","end").replace(" ","").replace("\n",""))
    num_s17 = int(text_s17.get("0.0","end").replace(" ","").replace("\n",""))
    num_s18 = int(text_s18.get("0.0","end").replace(" ","").replace("\n",""))
    num_s19 = int(text_s19.get("0.0","end").replace(" ","").replace("\n",""))
    num_s20 = int(text_s20.get("0.0","end").replace(" ","").replace("\n",""))
    num_s21 = int(text_s21.get("0.0","end").replace(" ","").replace("\n",""))
    num_s22 = int(text_s22.get("0.0","end").replace(" ","").replace("\n",""))
    num_s23 = int(text_s23.get("0.0","end").replace(" ","").replace("\n",""))
    num_s24 = int(text_s24.get("0.0","end").replace(" ","").replace("\n",""))

    snack_num = num_s1 + num_s2 + num_s3 + num_s4 + num_s5 + num_s6 + num_s7 + num_s8 + num_s9 + num_s10 + num_s11                + num_s12 + num_s13 + num_s14 + num_s15 + num_s16 + num_s17 + num_s18 + num_s19 + num_s20 + num_s21                + num_s22 + num_s23 + num_s24 

    snack_money = num_s1*30 + num_s2*45 + num_s3*65 + num_s4*35 + num_s5*45 + num_s6*58 + num_s7*32 + num_s8*49                   + num_s9*130 + num_s10*49 + num_s11*130 + num_s12*35 + num_s13*55 + num_s14*45 + num_s15*39                   + num_s16*40 + num_s17*55 + num_s18*18 + num_s19*30 + num_s20*49 + num_s21*64 + num_s22*104                   + num_s23*60 + num_s24*60


    #飲料
    num_d1_1 = int(text_d1_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d1_2 = int(text_d1_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d1_3 = int(text_d1_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d2_1 = int(text_d2_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d2_2 = int(text_d2_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d2_3 = int(text_d2_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d3_1 = int(text_d3_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d3_2 = int(text_d3_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d3_3 = int(text_d3_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d4_1 = int(text_d4_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d4_2 = int(text_d4_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d4_3 = int(text_d4_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d5_1 = int(text_d5_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d5_2 = int(text_d5_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d5_3 = int(text_d5_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d6_1 = int(text_d6_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d6_2 = int(text_d6_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d6_3 = int(text_d6_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d7_1 = int(text_d7_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d8_1 = int(text_d8_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d8_2 = int(text_d8_2.get("0.0","end").replace(" ","").replace("\n",""))
    num_d9_1 = int(text_d9_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d10_1 = int(text_d10_1.get("0.0","end").replace(" ","").replace("\n",""))
    num_d10_3 = int(text_d10_3.get("0.0","end").replace(" ","").replace("\n",""))
    num_d11_1 = int(text_d11_1.get("0.0","end").replace(" ","").replace("\n",""))

    drink_num = num_d1_1 + num_d1_2 + num_d1_3 + num_d2_1 + num_d2_2 + num_d2_3 + num_d3_1 + num_d3_2                 + num_d3_3 + num_d4_1 + num_d4_2 + num_d4_3 + num_d5_1 + num_d5_2 + num_d5_3 + num_d6_1                 + num_d6_2 + num_d6_3 + num_d7_1 + num_d8_1 + num_d8_2 + num_d9_1 + num_d10_1 + num_d10_3 + num_d11_1

    drink_num_nosmall = num_d1_2 + num_d1_3 + num_d2_2 + num_d2_3 + num_d3_2 + num_d3_3 + num_d4_2 + num_d4_3                         + num_d5_2 + num_d5_3 + num_d6_2 + num_d6_3 + num_d7_1 + num_d8_1 + num_d8_2 + num_d9_1                         + num_d10_1 + num_d10_3

    drink_money = num_d1_1*33 + num_d1_2*38 + num_d1_3*45 + num_d2_1*33 + num_d2_2*38 + num_d2_3*45                   + num_d3_1*33 + num_d3_2*38 + num_d3_3*45 + num_d4_1*33 + num_d4_2*38 + num_d4_3*45                   + num_d5_1*33 + num_d5_2*38 + num_d5_3*45 + num_d6_1*33 + num_d6_2*38 + num_d6_3*45                   + num_d7_1*55 + num_d8_1*38 + num_d8_2*48 + num_d9_1*38 + num_d10_1*38 + num_d10_3*48 + num_d11_1*33



    #超值全餐配餐優惠 
    #A:省28$ 中薯=num_s5  ; B:省28$ 沙拉=num_s14  ; C:省30$ 麥脆雞腿=num_s23+num_s24  ; 
    #D:省43$ 冰炫風=num_s13+小薯=num_s4  ; E:省52$ 麥克雞塊六塊=num_s21+小薯=num_s4  ; F:省28$ 黃金地瓜條=num_s3

    set = num_s5 + num_s14 + (num_s23+num_s24) + num_s13 + num_s21 + num_s3  
    set_ABF = num_s5 + num_s14 + num_s3
    set_ABCF = set_ABF + (num_s23+num_s24)
    set_ABCDF = set - num_s21
    
    #套餐飲料點 33 元的不退錢
    drink_money_33 = 0
    
    #判斷
    if (set <= meal_num) and (set <= drink_num):
        #先從省最多的(麥克雞六塊)開始計算
        if num_s21 >= num_s4:
            #當小薯數量僅夠給麥克雞六塊搭配，可忽略冰炫風組合
            set_free = num_s4*52
            num_s21 = num_s21 - num_s4           #還剩幾份六塊雞塊
            #計算其它
            set_num = set -  num_s21 - num_s13   #成功搭配數量(扣去沒組合到的雞塊和冰炫風)
            set_free = num_s5*28 + num_s14*28 + (num_s23+num_s24)*30 + num_s4*52 + num_s3*28 
        #小薯數量搭配完雞塊後還可搭配冰炫風
        else:
            set_free = num_s21*52
            num_s4 = num_s4 - num_s21               #搭配完雞塊後剩下的小薯
            num_s21 = 0                               #六塊雞塊搭配完了，不能搭配後面的超值加點
            if num_s13 >= num_s4:                   #冰炫風數量 >= 小薯
                set_num = set - (num_s13 - num_s4)         #成功搭配數量(扣去沒組合到的冰炫風)
                set_free = set_free + num_s4*43 + num_s5*28 + num_s14*28 + (num_s23+num_s24)*30 + num_s3*28
            else:                                   #冰炫風數量 < 小薯
                set_num = set
                set_free = set_free + num_s13*43 + num_s5*28 + num_s14*28 + (num_s23+num_s24)*30 + num_s3*28
        
        #套餐飲料點 33 元的不退錢
        if drink_num_nosmall < set_num:
            drink_money_33 = (set_num - drink_num_nosmall)*5
        set_free = set_free - drink_money_33
        
        
    else:
        if meal_num >= drink_num:
            no_set = set - drink_num            #無法搭配到的配餐數
        else:
            no_set = set - meal_num             #無法搭配到的配餐數
        
        
        if no_set <= set_ABF:                 #從最便宜的開始放棄搭配
            if num_s21 >= num_s4:
                #先從省最多的(麥克雞六塊)開始計算
                #當小薯數量僅夠給麥克雞六塊搭配，可忽略冰炫風組合
                set_free = num_s4*52
                num_s21 = num_s21 - num_s4           #還剩幾份六塊雞塊
                #計算其它
                set_num = (set-no_set) -  num_s21 - num_s13   #成功搭配數量(扣去沒組合到的雞塊和冰炫風)
                set_free = (set_ABF - no_set)*28 + (num_s23+num_s24)*30 + num_s4*52 
            #小薯數量搭配完雞塊後還可搭配冰炫風
            else:
                set_free = num_s21*52
                num_s4 = num_s4 - num_s21                 #搭配完雞塊後剩下的小薯
                num_s21 = 0                               #六塊雞塊搭配完了，不能搭配後面的超值加點
                if num_s13 >= num_s4:                     #冰炫風數量 >= 小薯
                    set_num = (set-no_set) - (num_s13 - num_s4)         #成功搭配數量(扣去沒組合到的冰炫風)
                    set_free = set_free + num_s4*43 + (set_ABF - no_set)*28 + (num_s23+num_s24)*30
                else:                                     #冰炫風數量 < 小薯
                    set_num = (set-no_set)
                    set_free = set_free + num_s13*43 + (set_ABF - no_set)*28 + (num_s23+num_s24)*30
        
        
        elif no_set <= set_ABCF:                 #從省28和省30放棄搭配
            if num_s21 >= num_s4:
                #先從省最多的(麥克雞六塊)開始計算
                #當小薯數量僅夠給麥克雞六塊搭配，可忽略冰炫風組合
                set_free = num_s4*52
                num_s21 = num_s21 - num_s4           #還剩幾份六塊雞塊
                #計算其它
                set_num = (set-no_set) -  num_s21 - num_s13   #成功搭配數量(扣去沒組合到的雞塊和冰炫風)
                set_free = (set_ABCF - no_set)*30 + num_s4*52 
            #小薯數量搭配完雞塊後還可搭配冰炫風
            else:
                set_free = num_s21*52
                num_s4 = num_s4 - num_s21                 #搭配完雞塊後剩下的小薯
                num_s21 = 0                               #六塊雞塊搭配完了，不能搭配後面的超值加點
                if num_s13 >= num_s4:                     #冰炫風數量 >= 小薯
                    set_num = (set-no_set) - (num_s13 - num_s4)         #成功搭配數量(扣去沒組合到的冰炫風)
                    set_free = set_free + num_s4*43 + (set_ABCF - no_set)*30
                else:                                     #冰炫風數量 < 小薯
                    set_num = (set-no_set)
                    set_free = set_free + num_s13*43 + (set_ABCF - no_set)*30

        elif no_set <= set_ABCDF:                 #往省43的放棄搭配
            if num_s21 >= num_s4:
                #先從省最多的(麥克雞六塊)開始計算
                #當小薯數量僅夠給麥克雞六塊搭配，可忽略冰炫風組合
                set_free = num_s4*52
                num_s21 = num_s21 - num_s4           #還剩幾份六塊雞塊
                set_num = num_s4                     #因不用搭配冰炫風，成功搭配數量僅有自己
                set_free = num_s4*52 
            #小薯數量搭配完雞塊後還可搭配冰炫風
            else:
                set_free = num_s21*52
                num_s4 = num_s4 - num_s21                 #搭配完雞塊後剩下的小薯
                if (set_ABCDF - no_set) >= num_s4:               #可搭配的冰炫風數量 >= 小薯
                    set_num = num_s21 + (set_ABCDF - no_set)         #成功搭配數量
                    set_free = set_free + (set_ABCDF - no_set)*43
                else:                                            #可搭配的冰炫風數量 < 小薯
                    set_num = num_s21
                    set_free = set_free
                num_s21 = 0                               #六塊雞塊搭配完了

        # set_ABCDF < no_set <= set
        else:                
            if (set-no_set) >= num_s4 :
                set_num = num_s4
                set_free = num_s4*52
                num_s21 = num_s21 - num_s4
            else:
                set_num = (set-no_set) 
                set_free = (set-no_set)*52
                num_s21 = 0
                
        #套餐飲料點 33 元的不退錢
        if drink_num_nosmall < set_num:
            drink_money_33 = (set_num - drink_num_nosmall)*5
        set_free = set_free - drink_money_33
    

    #超值加點優惠：麥克雞塊4塊$45、麥克雞塊6塊$55
    if (set_num>=num_s21) or (set_num-num_s21>=num_s20):
        if (set_num >= num_s21):
            add_free = num_s21*9
            set_num = set_num-num_s21
            if (set_num >= num_s20):
                add_free = add_free + num_s20*4
    else:
        add_free = 0
        

    if a == 1:
        sum = meal_money + plus_money + snack_money + drink_money - set_free - add_free - num_s3*7
        sum_text1 = tk.Label(win5, text='最便宜的組合價格為：',font=('微軟正黑體',16))
        sum_text1.grid(row=4,column=0,padx=10,pady=5, sticky=W)
        sum_text1['bg'] = 'WhiteSmoke'
        sum_text2 = tk.Label(win5, text=sum,font=('微軟正黑體',16))
        sum_text2.grid(row=4,column=1,pady=5, sticky=W)
        sum_text2['bg'] = 'WhiteSmoke'
        sum_text3 = tk.Label(win5, text='元！',font=('微軟正黑體',16))
        sum_text3.grid(row=4,column=2,pady=5, sticky=W)
        sum_text3['bg'] = 'WhiteSmoke'
        warning = tk.Label(win5)

        
    #修改鍵   
    def amend():
        
        if a == 1:
            sum_text1.grid_forget()
            sum_text2.grid_forget()
            sum_text3.grid_forget()
            button_restart.grid_forget()
            button_amend.grid_forget()
        if b == 1:
            warning.grid_forget()
            button_restart.grid_forget() 
            button_amend.grid_forget()
        button = tk.Button(win5, width = 10, height = 2,text='確認點餐',font=('微軟正黑體',14),command=lambda:[button.grid_forget(),calculate()])
        button.grid(row=3,column=0,columnspan=4,padx=10, sticky=W)
        
    
    
    button_amend = tk.Button(win5, width = 10, height = 1,text='修改數量',font=('微軟正黑體',14),command=amend)
    button_amend.grid(row=5,column=0,padx=10, sticky=W)
    
    
    #重新開始鍵
    #將所有數字歸零
    def restart():
        
        if a == 1:
            sum_text1.grid_forget()
            sum_text2.grid_forget()
            sum_text3.grid_forget()
            button_restart.grid_forget()
            button_amend.grid_forget()
        if b == 1:
            warning.grid_forget()
            button_restart.grid_forget()
            button_amend.grid_forget()
        
        #刪除原本內容
        text_m1.delete('0.0', END)
        text_m1.delete('0.0', END)
        text_m2.delete('0.0', END)
        text_m3.delete('0.0', END)
        text_m4.delete('0.0', END)
        text_m5.delete('0.0', END)
        text_m6.delete('0.0', END)
        text_m7.delete('0.0', END)
        text_m8.delete('0.0', END)
        text_m9.delete('0.0', END)
        text_m10.delete('0.0', END)
        text_m11.delete('0.0', END)
        text_m12.delete('0.0', END)
        text_m13.delete('0.0', END)
        text_m14.delete('0.0', END)
        text_m15.delete('0.0', END)
        text_m16.delete('0.0', END)
        text_m17.delete('0.0', END)
        text_m18.delete('0.0', END)
        
        text_plus1.delete('0.0', END)
        text_plus2.delete('0.0', END)
        text_plus3.delete('0.0', END)
        text_plus4.delete('0.0', END)
        text_plus5.delete('0.0', END)
        text_plus6.delete('0.0', END)
        text_plus7.delete('0.0', END)
        text_plus8.delete('0.0', END)

        text_plusd1.delete('0.0', END)
        text_plusd2.delete('0.0', END)
        text_plusd3.delete('0.0', END)
        text_plusd4.delete('0.0', END)
        text_plusd5.delete('0.0', END)
        text_plusd6.delete('0.0', END)
        text_plusd7.delete('0.0', END)
        text_plusd8.delete('0.0', END)
        
        text_s1.delete('0.0', END)
        text_s2.delete('0.0', END)
        text_s3.delete('0.0', END)
        text_s4.delete('0.0', END)
        text_s5.delete('0.0', END)
        text_s6.delete('0.0', END)
        text_s7.delete('0.0', END)
        text_s8.delete('0.0', END)
        text_s9.delete('0.0', END)
        text_s10.delete('0.0', END)
        text_s11.delete('0.0', END)
        text_s12.delete('0.0', END)
        text_s13.delete('0.0', END)
        text_s14.delete('0.0', END)
        text_s15.delete('0.0', END)
        text_s16.delete('0.0', END)
        text_s17.delete('0.0', END)
        text_s18.delete('0.0', END)
        text_s19.delete('0.0', END)
        text_s20.delete('0.0', END)
        text_s21.delete('0.0', END)
        text_s22.delete('0.0', END)
        text_s23.delete('0.0', END)
        text_s24.delete('0.0', END)
        
        text_d1_1.delete('0.0', END)
        text_d1_2.delete('0.0', END)
        text_d1_3.delete('0.0', END)
        text_d2_1.delete('0.0', END)
        text_d2_2.delete('0.0', END)
        text_d2_3.delete('0.0', END)
        text_d3_1.delete('0.0', END)
        text_d3_2.delete('0.0', END)
        text_d3_3.delete('0.0', END)
        text_d4_1.delete('0.0', END)
        text_d4_2.delete('0.0', END)
        text_d4_3.delete('0.0', END)
        text_d5_1.delete('0.0', END)
        text_d5_2.delete('0.0', END)
        text_d5_3.delete('0.0', END)
        text_d6_1.delete('0.0', END)
        text_d6_2.delete('0.0', END)
        text_d6_3.delete('0.0', END)
        text_d7_1.delete('0.0', END)
        text_d8_1.delete('0.0', END)
        text_d8_2.delete('0.0', END)
        text_d9_1.delete('0.0', END)
        text_d10_1.delete('0.0', END)
        text_d10_3.delete('0.0', END)
        text_d11_1.delete('0.0', END)
        
        #預設為 0
        text_m1.insert(tk.INSERT, "0")
        text_m2.insert(tk.INSERT, "0")
        text_m3.insert(tk.INSERT, "0")
        text_m4.insert(tk.INSERT, "0")
        text_m5.insert(tk.INSERT, "0")
        text_m6.insert(tk.INSERT, "0")
        text_m7.insert(tk.INSERT, "0")
        text_m8.insert(tk.INSERT, "0")
        text_m9.insert(tk.INSERT, "0")
        text_m10.insert(tk.INSERT, "0")
        text_m11.insert(tk.INSERT, "0")
        text_m12.insert(tk.INSERT, "0")
        text_m13.insert(tk.INSERT, "0")
        text_m14.insert(tk.INSERT, "0")
        text_m15.insert(tk.INSERT, "0")
        text_m16.insert(tk.INSERT, "0")
        text_m17.insert(tk.INSERT, "0")
        text_m18.insert(tk.INSERT, "0")
        
        text_plus1.insert(tk.INSERT,"0")
        text_plus2.insert(tk.INSERT,"0")
        text_plus3.insert(tk.INSERT,"0")
        text_plus4.insert(tk.INSERT,"0")
        text_plus5.insert(tk.INSERT,"0")
        text_plus6.insert(tk.INSERT,"0")
        text_plus7.insert(tk.INSERT,"0")
        text_plus8.insert(tk.INSERT,"0")

        text_plusd1.insert(tk.INSERT,"0")
        text_plusd2.insert(tk.INSERT,"0")
        text_plusd3.insert(tk.INSERT,"0")
        text_plusd4.insert(tk.INSERT,"0")
        text_plusd5.insert(tk.INSERT,"0")
        text_plusd6.insert(tk.INSERT,"0")
        text_plusd7.insert(tk.INSERT,"0")
        text_plusd8.insert(tk.INSERT,"0")
        
        text_s1.insert(tk.INSERT,"0")
        text_s2.insert(tk.INSERT,"0")
        text_s3.insert(tk.INSERT,"0")
        text_s4.insert(tk.INSERT,"0")
        text_s5.insert(tk.INSERT,"0")
        text_s6.insert(tk.INSERT,"0")
        text_s7.insert(tk.INSERT,"0")
        text_s8.insert(tk.INSERT,"0")
        text_s9.insert(tk.INSERT,"0")
        text_s10.insert(tk.INSERT,"0")
        text_s11.insert(tk.INSERT,"0")
        text_s12.insert(tk.INSERT,"0")
        text_s13.insert(tk.INSERT,"0")
        text_s14.insert(tk.INSERT,"0")
        text_s15.insert(tk.INSERT,"0")
        text_s16.insert(tk.INSERT,"0")
        text_s17.insert(tk.INSERT,"0")
        text_s18.insert(tk.INSERT,"0")
        text_s19.insert(tk.INSERT,"0")
        text_s20.insert(tk.INSERT,"0")
        text_s21.insert(tk.INSERT,"0")
        text_s22.insert(tk.INSERT,"0")
        text_s23.insert(tk.INSERT,"0")
        text_s24.insert(tk.INSERT,"0")
        
        text_d1_1.insert(tk.INSERT,"0")
        text_d1_2.insert(tk.INSERT,"0")
        text_d1_3.insert(tk.INSERT,"0")
        text_d2_1.insert(tk.INSERT,"0")
        text_d2_2.insert(tk.INSERT,"0")
        text_d2_3.insert(tk.INSERT,"0")
        text_d3_1.insert(tk.INSERT,"0")
        text_d3_2.insert(tk.INSERT,"0")
        text_d3_3.insert(tk.INSERT,"0")
        text_d4_1.insert(tk.INSERT,"0")
        text_d4_2.insert(tk.INSERT,"0")
        text_d4_3.insert(tk.INSERT,"0")
        text_d5_1.insert(tk.INSERT,"0")
        text_d5_2.insert(tk.INSERT,"0")
        text_d5_3.insert(tk.INSERT,"0")
        text_d6_1.insert(tk.INSERT,"0")
        text_d6_2.insert(tk.INSERT,"0")
        text_d6_3.insert(tk.INSERT,"0")
        text_d7_1.insert(tk.INSERT,"0")
        text_d8_1.insert(tk.INSERT,"0")
        text_d8_2.insert(tk.INSERT,"0")
        text_d9_1.insert(tk.INSERT,"0")
        text_d10_1.insert(tk.INSERT,"0")
        text_d10_3.insert(tk.INSERT,"0")
        text_d11_1.insert(tk.INSERT,"0")
        button = tk.Button(win5, width = 10, height = 2,text='確認點餐',font=('微軟正黑體',14),command=lambda:[button.grid_forget(),calculate()])
        button.grid(row=3,column=0,columnspan=4,padx=10, sticky=W)

    
    button_restart = tk.Button(win5, width = 10, height = 1,text='重新輸入',font=('微軟正黑體',14),command=restart)
    button_restart.grid(row=5,column=1,columnspan=4,padx=10, sticky=W)
    
    
    


# In[7]:


# ----------------------結算----------------------

# Logo
logo1= ImageTk.PhotoImage(Image.open(os.path.relpath("picture/logo.jpg")).resize((120, 120), Image.ANTIALIAS))
pic_logo1= tk.Label(win5,image = logo)
pic_logo1.grid(row=0,column=0, sticky=W)
pic_logo1['bg'] = 'white'

# Label
title_c = tk.Label(win5, text='結算',font=('微軟正黑體',16))
title_c.grid(row=1,column=0,padx=5,pady=5, sticky=W)
title_c['bg'] = 'OrangeRed2'
text_c = tk.Label(win5, text='*因目前黃金地瓜條是嚐鮮價，單點或超值全餐有包含黃金地瓜條皆有7元折扣*\n*超值加點優惠：麥克雞塊4塊$45、麥克雞塊6塊$55*',font=('微軟正黑體',14))
text_c.grid(row=2,column=0,padx=5,columnspan=20,pady=5, sticky=W)
text_c['bg'] = 'white'

# Button
button = tk.Button(win5, width = 10, height = 2,text='確認點餐',font=('微軟正黑體',14),command=calculate)
button.grid(row=3,column=0,columnspan=4,padx=10, sticky=W)


root.mainloop()

