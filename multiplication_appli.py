# -*- coding: utf-8 -*-
"""
Created on 2020/6/1
@author: iansala
掛け算の暗算アプリ

【機能】
・ランダムに2桁×2桁の掛け算の問題を表示する。
・答えを入力する。
・「正解」を押下すると，正解を表示する。
・「次の問題」を押下すると，問題を更新し，「入力値」と「正解」を空白にする。
"""

import tkinter as tk
import numpy as np
from numpy.random import randint

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.width=500
        self.height=300

        master.geometry(str(self.width)+"x"+str(self.height)) #ウィンドウの作成

        master.title("掛け算") #タイトル
        self.master.config(bg="pink") #ウィンドウの背景色

        self.createWidgets() #ウィジェットの作成

    def createWidgets(self): #ウィジェットの作成
        #和の計算をするためのテキストボックスやラベル、ボタンの作成
        a = randint(1,100)
        b = randint(1,100)
        right_answer = a*b

        self.question1_1 = tk.Label(text=a,fg="black",bg="pink",font=("Helvetica",30))
        self.question1_1.place(x=40,y=50)
        self.question1_2 = tk.Label(text=b,fg="black",bg="pink",font=("Helvetica",30))
        self.question1_2.place(x=190,y=50)
        self.entry1 = tk.Entry(font=("",30))
        self.entry1.place(x=300,y=50, width= 150, height=50)

        self.label2 = tk.Label(text="×",fg="black",bg="pink",font=("Helvetica",30,"bold"))
        self.label2.place(x=130,y=53)
        self.label3 = tk.Label(text="=",fg="black",bg="pink",font=("Helvetica",30,"bold"))
        self.label3.place(x=258,y=53)

        self.button1 = tk.Button(text="答え合わせ",command=self.button1Click(right_answer))
        self.button1.place(x=120, y=140,height=40, width=80)

        self.button2 = tk.Button(text="次の問題",command=self.button2Click)
        self.button2.place(x=120, y=210,height=40, width=80)

    def button1Click(self,right_answer): #ボタンが押された時に呼ばれるメソッド
        def x():
            if right_answer == int(self.entry1.get()):
                self.answer1 = tk.Label(text="正解！！",fg="red",bg="pink",font=("Helvetica",30))
                self.answer1.place(x=250, y=135)
            else:    
                self.answer1 = tk.Label(text=right_answer,fg="black",bg="pink",font=("Helvetica",30))
                self.answer1.place(x=250, y=135)
        return x

    def button2Click(self): #ボタンが押された時に呼ばれるメソッド
        self.entry1.delete(0,tk.END)
        self.answer1.place_forget()
        self.createWidgets()

def main():
    win = tk.Tk()
    win.resizable(width=True, height=True) #ウィンドウを固定サイズに
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()
