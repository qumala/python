#!/usr/bin/env python3.5
import numpy as np
import time
import math
from functools import partial
class Stardust:
    def __init__(self):
        self.dt   = 0.001
        self.dN   = 1
        self.Nt   = 0
        self.done = False
        self.Time = 0
        self.X    = (np.random.random([200,2]))
        self.V   =  (np.random.random([200,2]))
        self.typeOfCoordinates='dots'

    def onButton(self,symbol='+'):
        def muldN(i):
            if i > 0:
                self.dN *= 10
            elif i < 0 and self.dN >= 10:
                self.dN = int(self.dN / 10)
        def muldt(i):
            if i > 0:
                self.dt *= 10
            elif i < 0:
                self.dt /= 10
        dicoffunc = {'+':partial(muldN,1),'-':partial(muldN,-1),'*':partial(muldt,1),'/':partial(muldt,-1)}
        dicoffunc[symbol]()

    @property
    def dY(self):
        return (np.max(self.X)-np.min(self.X))

    @property
    def Yamax(self):
        return max(abs(np.max(self.X)), abs(np.min(self.X)))
    @property
    def Ymax(self):
        return np.max(self.X)
    @property
    def Ymin(self):
        return np.min(self.X)

    @property
    def coordX0(self):
        return -self.Ymin/self.dY
    @property
    def coordX1(self):
        return (1-self.Ymin)/self.dY
    @property
    def coordY0(self):
        return -self.Ymin/self.dY
    @property
    def coordY1(self):
        return (1-self.Ymin)/self.dY

    def getCoordinatesAndColors(self):
        R=[]
        dX=self.dY
        Xmin=self.Ymin
        for i in range(len(self.X)):
            R.append([(self.X[i][0]-Xmin)/dX,(self.X[i][1]-Xmin)/dX,0.,1.,0.])
        return R

    @property
    def text(self):
        return str(self.Time)+' '+str(self.Nt)

    def step(self,dN=0):
        if dN==0:dN=self.dN
        for i in range(int(dN)):
            if(self.done):
                break
            else:
                self.X+=self.V*self.dt
                for i in range(len(self.X)):
                    for j in range(i+1,len(self.X)):
                        dXij=self.X[i]-self.X[j]
                        dXij2=sum(dXij*dXij)
                        dVij=self.dt*(-dXij/(dXij2+1e-5))
                        self.V[i]+=dVij
                        self.V[j]-=dVij
                self.Nt+=1
                self.Time+=self.dt
        print("phys step ends")

def main():
    import plotting
    app = plotting.Application(Stardust())
    #A=Stardust()
    #print("here")
    #print(A.X[0]+A.X[1])
    print("here0")
    app.master.title('Sample application')
    app.after(10,app.draw)
    print("here1")
    app.mainloop()
    print("here2")


if __name__ == '__main__':
    main()
