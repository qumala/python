#!/usr/bin/env python3.5
import tkinter as tk
import numpy as np
import time
import math
from functools import partial

class Application(tk.Frame):
    def __init__(self,physWorld,master=None):
        tk.Frame.__init__(self, master)
        self.physWorld=physWorld
        self.grid()
        self.createWidgets()
        self.done = False
        self.pause = True

    def pauseOnButton(self):
        self.pause = not self.pause
        print("pause " + str(self.pause))
        self.canvas.after(1, self.actionloop)

    def quiteOnButton(self):
        self.done = True
        time.sleep(0.001)
        self.quit()

    def createWidgets(self):
        self.ButtonQuit = tk.Button(self, text='Pause',
                                    command=self.pauseOnButton)
        self.ButtonPause = tk.Button(self, text='Quit',
                                     command=self.quiteOnButton)
        self.ButtonPlus = tk.Button(self, text='+',command=partial(self.physWorld.onButton,'+'))
        self.ButtonMnus = tk.Button(self, text='-',command=partial(self.physWorld.onButton,'-'))
        self.ButtonMult = tk.Button(self, text='*',command=partial(self.physWorld.onButton,'*'))
        self.ButtonDiv = tk.Button(self, text='/',command=partial(self.physWorld.onButton,'/'))
        self.timetext = tk.Label(self, text='0')
        self.ButtonQuit.grid(column=0, row=1)
        self.ButtonPause.grid(column=6, row=1)
        self.ButtonPlus.grid(column=1, row=1)
        self.ButtonMnus.grid(column=5, row=1)
        self.ButtonMult.grid(column=2, row=1)
        self.ButtonDiv.grid(column=4, row=1)
        self.timetext.grid(column=3, row=1)
        self.canvas = tk.Canvas(self, height=600, width=1100, bg='#000000')
        def canvasclick(event):
            d={1:'left',3:'right'}
            if event.num in d.keys():
                print(d[event.num],event.x,event.y)
        def wheelscroll(event):
            if event.num in [2,4,5]:
                print("wheel",event.num, event.x,event.y)
            else:
                print("not wheel")
        self.canvas.bind("<Button-1>",canvasclick)
        self.canvas.bind("<Button-2>",wheelscroll)
        self.canvas.bind("<Button-3>",canvasclick)
        self.canvas.bind("<Button-4>",wheelscroll)
        self.canvas.bind("<Button-5>",wheelscroll)
        self.img = tk.PhotoImage(width=self.canvas['width'], height=self.canvas['height'])
        self.canvas.create_image((int(int(self.canvas['width'])/2),int(int(self.canvas['height'])/2)), image=self.img, state="normal")

        self.canvas.grid(column=0, row=0, columnspan=7)
        print("finish creation")

    def draw(self):
        c=self.physWorld.getCoordinatesAndColors()
        #print("draw",len(c),c[0])
        def cordY(y):
            return int((0.9-y*0.8)*self.img.height())
        def cordX(x):
            return int((0.1+0.8*x)*self.img.width())
        #self.canvas.create_text(200,100,text="hello_word",fill='#00ff00')
        #for n in range(len(self.X)):
            #if n>0 and n< self.img.width() and cordY(self.X[n])>0 and cordY(self.X[n])<self.img.height():
                #self.img.put("#000000", (n, cordY(self.pX[n])))
                #self.img.put("#ff0000", (n, cordY(self.X[n])))
                #self.canvas.create_rectangle(n, cordY(self.X[n]), n+2, cordY(self.X[n])+2, fill='#FF0000')
        def converColor(color):
            return '#'+hex(int(color[0]*(2**4-1)))[2:]+hex(int(color[1]*(2**4-1)))[2:]+hex(int(color[2]*(2**4-1)))[2:]

        self.canvas.delete('all')
        if self.physWorld.typeOfCoordinates=='lines':
            for n in range(len(c) - 1):
                self.canvas.create_line(cordX(c[n][0]), cordY(c[n][1]), cordX(c[n+1][0]), cordY(c[n+1][1]), fill=converColor(c[n][2:]))
        elif self.physWorld.typeOfCoordinates=='dots':
            self.img = tk.PhotoImage(width=self.canvas['width'], height=self.canvas['height'])
            self.canvas.create_image((int(int(self.canvas['width']) / 2), int(int(self.canvas['height']) / 2)),image=self.img, state="normal")
            for n in range(len(c)):
                self.img.put(converColor(c[n][2:]), (cordX(c[n][0]), cordY(c[n][1])))


        #for n in range(self):
        self.canvas.create_line(cordX(self.physWorld.coordX0), cordY(0), cordX(self.physWorld.coordX0), cordY(1), fill='#00F0FF')
        self.canvas.create_line(cordX(self.physWorld.coordX1), cordY(0), cordX(self.physWorld.coordX1), cordY(1), fill='#00F0FF')
        #for n in range(maxX):
        self.canvas.create_line(cordX(0), cordY(self.physWorld.coordY0), cordX(1), cordY(self.physWorld.coordY0), fill='#00F0FF')
        self.canvas.create_line(cordX(0), cordY(self.physWorld.coordY1), cordX(1), cordY(self.physWorld.coordY1),fill='#00F0FF')

    def actionloop(self):
        if not self.done and not self.pause and not self.physWorld.done:
            self.step()
            self.canvas.after(1, self.actionloop)

    def step(self):
        self.physWorld.step()
        self.draw()
        #print("drawing ends")
        self.timetext['text'] = self.physWorld.text

def main():
    import termoconductivity
    app = Application(termoconductivity.Termoconductivity())
    app.master.title('Sample application')
    print("here")
    #app.after(500,app.physicloop)
    app.after(10,app.draw)
    #app.draw()
    print("here1")
    app.mainloop()
    print("here2")


if __name__ == '__main__':
    main()
