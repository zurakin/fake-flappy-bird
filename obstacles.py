import constantes
import random

class Obstacle:
    def __init__(self,x0):
        self.height = random.randint(0.1*constantes.height, 0.9*constantes.height)
        self.x = x0
        self.hole_size = random.randint(int(constantes.scale * 2),
        int(constantes.scale * 2.5))

    def insert(self,canvas):
        self.image = []
        self.image.append(canvas.create_rectangle(
        self.x,
        constantes.height-self.height,
        self.x + 20,
        constantes.height,
        fill = 'black'
        ))
        self.image.append(
        canvas.create_rectangle(
        self.x,
        0,
        self.x + 20,
        constantes.height-self.height - self.hole_size,
        fill = 'black'
        )
        )

    def move(self,canvas,speed):
        if self.x <0 :
            Obstacle.__init__(self,constantes.width+20)
            canvas.delete(self.image[0])
            canvas.delete(self.image[1])
            self.insert(canvas)
        self.x -=speed * constantes.scale * constantes.tscale
        canvas.move(self.image[0],
        -speed * constantes.scale * constantes.tscale,
        0
        )
        canvas.move(self.image[1],
        -speed * constantes.scale * constantes.tscale,
        0
        )
