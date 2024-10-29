import random
import GrandLottoNum
import win32gui
import threading
import tkinter as tk
import requests 
from bs4 import BeautifulSoup
import json


#print("=" *20)
#print("Grand Lotto")
#print("=" *20)
#print("these are numbers:")
#frontNum = GrandLottoNum.randomNum5()
#backNum = GrandLottoNum.randomNum2()
#GrandLottoNum.lottoPrint(frontNum)
#print(" | ",end = "")
#GrandLottoNum.lottoPrint(backNum)
#print("")
#frontNum.sort()
#backNum.sort()
#GrandLottoNum.lottoPrint(frontNum)
#@print(" | ",end = "")
#GrandLottoNum.lottoPrint(backNum)
#print("")
#input("press enter to quit")

#init
isWin2Open = 0
url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1'
error = 0
#latest num
response = requests.get(url)
if response.status_code == 200:
    # print("200!")
    data = json.loads(response.text)
    nums = data["value"]["lastPoolDraw"]["lotteryDrawResult"]
    time1 = data["value"]["lastPoolDraw"]["lotteryDrawTime"]
else:
    print("error")
    error = 1

# print(nums)
# print(time1)

#num string
def init():
    global String1
    global String2
    String1 = []  #nunm
    String2 = []  #sorted num

def updateNum():
    global frontNum
    global backNum
    global String1
    global String2
    for x in frontNum:
        String1.append(x)
    String1.append("|")
    for x in backNum:
        String1.append(x)

    frontNum.sort()
    backNum.sort()

    for x in frontNum:
        String2.append(x)
    String2.append("|")
    for x in backNum:
        String2.append(x)


#window
window = tk.Tk()
window.title("Grand Lotto Number Spawner")
window.geometry("400x400")
window.config(bg="lightblue")

#lebel
varLabelLottoNum1 = tk.StringVar() #the front
varLabelLottoNum2 = tk.StringVar() #the back
varLabelNum = tk.StringVar()
varLabelNum.set("0")
label1 = tk.Label(window,text="="*44,bg="lightblue",font="Arial 12")
label2 = tk.Label(window,text="="*44,bg="lightblue",font="Arial 12")
label3 = tk.Label(window,textvariable=varLabelLottoNum1,bg="lightblue",font="Arial 24")
label4 = tk.Label(window,textvariable=varLabelLottoNum2,bg="lightblue",font="Arial 24")
label5 = tk.Label(window,textvariable=varLabelNum,bg="lightblue",fg="red",font="Arial 34")
label6 = tk.Label(window,text="generation time(s):",bg="lightblue",font="Arial 20")

########toplevel window
varLatestNum = tk.StringVar()


n = 0
#button
def on_buttonClick1():
    global frontNum
    global backNum
    frontNum = GrandLottoNum.randomNum5()
    backNum = GrandLottoNum.randomNum2()
    init()
    updateNum()
    global n
    n = n + 1
    varLabelNum.set(n)
    varLabelLottoNum1.set(String1)
    varLabelLottoNum2.set(String2)




def on_buttonClick2():
    window.destroy()

def on_buttonClick3():
    global isWin2Open
    global window2
    global time1
    global nums
    if isWin2Open == 0:
        isWin2Open = 1
        window2 = tk.Toplevel()
        window2.title("qwq")
        window2.geometry("640x240")
        window2.config(bg="lightblue")
        label21 = tk.Label(window2,text=f'LottoNumbers:'+nums,bg="lightblue",font="Arial 24")
        label22 = tk.Label(window2,text=f'Date:'+time1,bg="lightblue",font="Arial 24")
        label21.place(relx=0.5,rely=0.3,anchor="center")
        label22.place(relx=0.5,rely=0.6,anchor="center")
        print(nums)
        print(time1)
    elif isWin2Open == 1:
        isWin2Open = 0
        window2.destroy()
    

# def on_buttonClick4():
#     isWin2Open = 0
#     window2.destory()


buttonStart = tk.Button(window,text="Spawn Lotto Number",command=on_buttonClick1,height=4,width=44,background="pink",font=4)
buttonEnd = tk.Button(window,text="Quit",command=on_buttonClick2,height=4,width=44,background="pink",font=4)
buttonT = tk.Button(window,text="wow",command=on_buttonClick3,height=2,width=44)

#set
label1.place(relx=0.5,rely=0.05,anchor="center")
label3.place(relx=0.5,rely=0.15,anchor="center")
label4.place(relx=0.5,rely=0.25,anchor="center")
label6.place(relx=0.5,rely=0.4,anchor="center")
label5.place(relx=0.5,rely=0.5,anchor="center")
label2.place(relx=0.5,rely=0.6,anchor="center")
buttonStart.place(relx=0.5,rely=0.7,height=44,width=344,anchor="center")
buttonEnd.place(relx=0.5,rely=0.85,height=44,width=344,anchor="center")
buttonT.place(relx=0.5,rely=0.95,height=20,width=44,anchor="center")

label2.place()




window.mainloop()


