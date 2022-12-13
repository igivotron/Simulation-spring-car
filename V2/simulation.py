import matplotlib.pyplot as plt
import numpy as np

class Engin:
    def __init__(self,f,k):
        self.k = 865.6*4
        self.ratio = 2/5
        self.f_eng = f
        self.f_air = k

    def frot_engr(self, v):
        return -self.f_eng*v

    def frot_air(self,v):
        return -self.f_air*v

    def joules(self):
        return pow(10/self.k,1/2)

    def force_mot(self):
        


class Simu:
    def __init__(self,dt,sigma):
        self.dt = dt
        self.g = 9.81
        self.x = 0
        self.v = 0
        self.sigma =sigma
        self.loop = True

    def test_loop(self,v):
        if v < self.sigma:
            self.loop = False

    def lst_x(self):
        while loop:


class Graph:
    def __init__(self,t,l_x,l_v,n_x="Temps",n_y="Position"):
        self.title = t
        self.n_x = n_x
        self.n_y = n_y
        self.l_x = l_x
        self.l_v = l_v

    def title(self):
        plt.title(self.title())

    def legend(self):
        plt.xlabel(self.n_x)
        plt.ylabel(self.n_y)
        plt.legend()

    def plot_x(self):
        plt.plot(self.l_x,label="position en [m]")
        self.title()
        self.legend()
        plt.show()

    def plot_v(self):
        plt.plot(self.l_v,label="vitesse en [m/s]")
        self.title()
        self.legend()
        plt.show()

    def plot_both(self):
        plt.plot(self.l_x,label="position en [m]")
        plt.plot(self.l_v,label="vitesse en [m/s]")
        self.title()
        self.legend()
        plt.show()











