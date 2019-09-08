from tkinter import *
import forces
import objects
import time
import constantes
import obstacles


def jump(*args):
    global temp_forces
    bird.jump(6)

temp_forces = []


#create window and canvas
root = Tk()
root.title('Flappy Flippin Bird')
canvas = Canvas(root,width = constantes.width,height = constantes.height)
canvas.grid()

#create bird object
bird = objects.Ball(r= 0.4,x0 = 1,y0 = 5 ,mass = 2 ,vx=0,vy=0,color='blue')
bird.insert(canvas)

#create Obstacles

obs = [obstacles.Obstacle(x0= 0.5*constantes.width ),
obstacles.Obstacle(x0= 0.75*constantes.width ),
obstacles.Obstacle(x0= 1*constantes.width ),
obstacles.Obstacle(x0= 1.25*constantes.width )
]

for ob in obs:
    ob.insert(canvas)

root.bind("<Up>",jump)
while True:
    if not bird.check_collision_y():
        temp_forces.append(forces.Poids(bird))
        bird.apply_forces(temp_forces)
        temp_forces = []
        bird.move(canvas)
    for ob in obs:
        ob.move(canvas,2)
    root.update()
    bird.update(canvas)
    time.sleep(0.5 * constantes.tscale)


root.mainloop()
