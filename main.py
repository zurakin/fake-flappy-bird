from tkinter import *
import forces
import objects
import time
import constantes
import obstacles
from PIL import ImageTk, Image


def jump(*args):
    global bird
    global temp_forces
    try:
        bird.jump(6)
    except:
        pass

def reset():
    global obs
    global bird
    try:
        canvas.delete(bird.image)
        for ob in obs:
            canvas.delete(ob.image[0])
            canvas.delete(ob.image[1])
    except:
        pass
    bird = objects.Bird(x0 = 1,y0 = 5 ,mass = 2 ,vx=0,vy=0)
    bird.insert(canvas)

    obs = [obstacles.Obstacle(x0= 0.5*constantes.width ),
    obstacles.Obstacle(x0= 0.75*constantes.width ),
    obstacles.Obstacle(x0= 1*constantes.width ),
    obstacles.Obstacle(x0= 1.25*constantes.width )
    ]
    for ob in obs:
        ob.insert(canvas)

temp_forces = []
root = Tk()


#create window and canvas
root.title('Flappy Flippin Bird')


root.bind("<Up>",jump)



canvas = Canvas(root,width = constantes.width,height = constantes.height)
canvas.grid()

loadback = Image.open(r"media/background.jpg")
background = ImageTk.PhotoImage(image = loadback)
canvas.create_image(0,0,image = background ,anchor = NW)

def execute():
    temp_forces = []
    reset()
    while True:
        if not bird.check_collision_y():
            temp_forces.append(forces.Poids(bird))
            bird.apply_forces(temp_forces)
            temp_forces = []
            bird.move(canvas)
        for ob in obs:
            ob.move(canvas,2)
        if bird.check_crash(obs):
            time.sleep(1)
            reset()

        root.update()
        bird.update(canvas)
        time.sleep(0.5 * constantes.tscale)


execute()
root.mainloop()
