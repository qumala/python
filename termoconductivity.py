#!/usr/bin/env python3.5
import numpy as np
import time
import math
from functools import partial
class Termoconductivity:
    def __init__(self):
        self.dt   = 0.01
        self.dN   = 100
        self.Nt   = 0
        self.done = False
        self.Time = 0
        self.X    = (np.random.random(1000)) * np.linspace(10, -10, 1000)
        self.pX   = np.zeros(1000)
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
        return max(self.X)-min(self.X)

    @property
    def Yamax(self):
        return max(abs(max(self.X)), abs(min(self.X)))
    @property
    def Ymax(self):
        return max(self.X)
    @property
    def Ymin(self):
        return min(self.X)

    @property
    def coordX0(self):
        return 0
    @property
    def coordX1(self):
        return 1/len(self.X)
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
            R.append([i/len(self.X),(self.X[i]-Xmin)/dX,0.,1.,0.])
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
                self.X[-1]=self.pX[-2]+1#0**6*(10-math.exp(self.X[-1]))/X(self.X[-1],len(self.X)+1)
                self.Nt+=1
                self.Time+=self.dt
        #print("phys step ends")
