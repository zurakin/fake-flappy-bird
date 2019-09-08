import constantes
from math import pi
from PIL import ImageTk
from tkinter import NW

class Object():

    def __init__(self,x0,y0,mass,vx=0,vy=0,color='blue'):
        self.mass = mass
        self.x = x0
        self.y = y0
        self.vx = vx
        self.vy = vy
        self.ax=0
        self.ay=0
        self.color=color


    def apply_forces(self,forces):
        self.fx = []
        self.fy = []
        for f in forces:
                self.fx.append(f.x)
                self.fy.append(f.y)
                self.ax = sum(self.fx)/self.mass
                self.ay = sum(self.fy)/self.mass

    def jump(self , speed):
        self.vy = -speed

    def delete(self,canvas):
        canvas.delete(self.image)

    def convert_pos(self):
        return (self.x * constantes.scale , self.y * constantes.scale)

    def convert_sp(self):
        return (self.vx * constantes.scale * constantes.tscale ,
         self.vy * constantes.scale * constantes.tscale)

    def move(self,canvas):
        canvas.move(self.image, self.convert_sp()[0], self.convert_sp()[1])


class Bird(Object):

    def __init__(self,x0,y0,mass,vx=0,vy=0):
        Object.__init__(self,x0=x0,y0=y0,mass=mass,vx=vx,vy=vy)
        self.picture = ImageTk.PhotoImage(file = r"media\rbluebird.png")

    def insert(self,canvas):
        self.image = canvas.create_image(
        self.convert_pos()[0],
        self.convert_pos()[1],
        image = self.picture,
        anchor = NW)
    def update(self,canvas):
        self.vx = self.ax * constantes.tscale + self.vx
        self.vy = self.ay * constantes.tscale + self.vy
        self.y = constantes.rconvert(canvas.coords(self.image)[1])
        self.x = constantes.rconvert(canvas.coords(self.image)[0])

    def check_collision_y(self):
        return self.y*constantes.scale + 47 >= constantes.height and self.vy >= 0

    def check_crash(self,obstacles):
        tolerance = 10
        imx = 71
        imy = 47
        return any([
        ob.x-imx<self.x*constantes.scale <ob.x+imy - tolerance and (
        self.y*constantes.scale+imy > constantes.height-ob.height or self.y*constantes.scale<constantes.height-ob.height - ob.hole_size)
        for ob in obstacles])


    def check_stable(self):
        return -0.5 <= self.vy <= 0.5 and self.y >= constantes.hval-self.rayon*1.1
