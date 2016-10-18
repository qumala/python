#!/usr/bin/env python3.5
import tkinter as tk
import numpy as np
import time
import math
from functools import partial

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.done = False
        self.pause = True
        self.dt = 0.01
        self.dN = 100
        self.Nt=0
        self.X=(np.random.random(1000))*np.linspace(10,-10,1000)
        self.pX=np.zeros(1000)
        #self.X=self.pX=np.ndarray(1000)
        #for i in range(len(self.X)):
        #    self.X[i]=math.sin(math.exp(i/50))#np.random.random()
        #    self.pX[i]=0

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
        def muldN(i):
            if i>0:
                self.dN*=10
            elif i<0 and self.dN>=10:
                self.dN=int(self.dN/10)
        def muldt(i):
            if i>0:
                self.dt*=10
            elif i<0 :
                self.dt/=10
        self.ButtonPlus = tk.Button(self, text='+',
                                     command=partial(muldN,1))
        self.ButtonMnus = tk.Button(self, text='-',
                                     command=partial(muldN,-1))
        self.ButtonMult = tk.Button(self, text='*',
                                     command=partial(muldt,1))
        self.ButtonDiv = tk.Button(self, text='/',
                                     command=partial(muldt,-1))
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
        #self.bind_all("<MouseWheel>", wheelscroll)
        self.img = tk.PhotoImage(width=self.canvas['width'], height=self.canvas['height'])
        self.canvas.create_image((300, 300), image=self.img, state="normal")
        self.canvas.grid(column=0, row=0, columnspan=7)
        print("finish creation")

    def draw(self):
        #print("draw")
        self.canvas.delete('all')
        #self.canvas.create_rectangle(0, 0, self.img.width(), self.img.height(), fill='#ffffff')
        # for x in range(4 * WIDTH):
        #    y = int(HEIGHT / 2 + HEIGHT / 4 * sin(x / 80.0))
        #    img.put("#ffffff", (x // 4, y))
        maxX=int(max(max(self.X),abs(min(self.X))))
        def cordY(y):
            return int((-y/maxX+1)*0.5*self.img.height())
        def cordX(x):
            return int(x+50)
        #self.canvas.create_rectangle(0, 0, 100, 200, fill='#00ff00')
        #self.canvas.create_text(200,100,text="hello_word")
        #for n in range(len(self.X)):
            #if n>0 and n< self.img.width() and cordY(self.X[n])>0 and cordY(self.X[n])<self.img.height():
                #self.img.put("#000000", (n, cordY(self.pX[n])))
                #self.img.put("#ff0000", (n, cordY(self.X[n])))
                #self.canvas.create_rectangle(n, cordY(self.X[n]), n+2, cordY(self.X[n])+2, fill='#FF0000')
        self.canvas.create_line(cordX(0), cordY(0), cordX(len(self.X)), cordY(0), fill='#0000FF')
        for n in range(maxX):
            self.canvas.create_line(cordX(0), cordY(n), cordX(len(self.X)), cordY(n), fill='#00F0FF')
        for n in range(len(self.X)-1):
            self.canvas.create_line(cordX(n), cordY(self.X[n]), cordX(n+1), cordY(self.X[n+1]), fill='#FF0000')
        #self.canvas.create_rectangle(300+self.R[0], 300+self.R[1], self.R[0]+303, self.R[1]+303, fill='#FF0000')

    def actionloop(self):
        #while not self.done and not self.pause:
            #time.sleep(0.001)
        if not self.done and not self.pause:
            for i in range(self.dN-1):
                self.physstep()
            self.step()
            self.canvas.after(1, self.actionloop)

    def physstep(self):
        dL=0.001;
        def C(T,x):
            return (1+T/100+10*np.exp(-T*2/200))*x**2
        def X(T,x):
            return (1-T/100)*x**2
        self.X,self.pX=(self.X+
                        self.dt*X(self.X,np.linspace(1,len(self.X)+1,len(self.X)))
                        /C(self.X,np.linspace(1,len(self.X)+1,len(self.X)))
                        *(-2*self.X+np.roll(self.X,1)+np.roll(self.X,-1))),self.X
        self.X[0]=self.X[1]
        A=10**2
        self.X[-1]=self.pX[-2]+10**6*(3-math.exp(self.X[-1]))/X(self.X[-1],len(self.X)+1)
        self.Nt+=1

    def step(self):
        self.physstep()
        self.draw()
        self.timetext['text'] = str(self.Nt)


def main():
    app = Application()
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
