import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dist(p1,p2):
    distance = np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distance
r = 1
r_lim = 0.05
global dtheta
dtheta = 0.0001
class circle:
    def __init__(self,r,center):
        self.radius = r
        self.center = center
    def draw_circ(self):
        theta= np.arange(0,2*np.pi,0.01)
        circ = self.radius*np.exp(1j*theta)
        np.append(circ,circ[0])
        X = np.real(circ)+self.center[0]
        Y = np.imag(circ)+self.center[1]
        return X, Y,
class new_circ(circle):

    def __init__(self,r,pre_r,pre_x,pre_y,angle):
        self.radius = r
        self.center = np.array([(r+pre_r)*np.cos(angle)+pre_x, (r+pre_r)*np.sin(angle)+pre_y])



fig = plt.figure()
ax = plt.axes(xlim = (-3,3), ylim=(-3,3))
linep, = ax.plot([],[],color = 'purple',lw=1)
line = []
radius = [1]
centers = []
diff = []
angle = [0]
vel = [0]
global count
count = 0
while r > r_lim:
    line1, = ax.plot([],[],lw=2)
    line.append(line1)
    r/=2
    radius.append(r)
    centers.append([])
    diff.append(0)
    angle.append(0)
    vel.append((7)**(count+1)*dtheta)
    count += 1

def init():
    linep.set_data([],[])
    for x in line:
        x.set_data([],[])
    return linep, line,

pntx = []
pnty = []


def animate(i):
    r = 1
    x = 0
    y = 0
    c1 = circle(r, [x, y])
    x1, y1 = c1.draw_circ()
    line[0].set_data(x1, y1)
    centers[0] = c1.center
    for k in range(1,count):
        r /= 2
        vel[k] = (7)**(k)*dtheta
        angle[k] += vel[k]
        c1 = new_circ(r,r*2,c1.center[0],c1.center[1],angle[k])
        centers[k] = c1.center
        x1, y1 = c1.draw_circ()
        # if k >1:
        #     for l in range(0,k-1):
        #         distance =  dist(centers[l], centers[k])
        #         if distance < radius[l]+radius[k]:
        #             vel[k] = -vel[k]
        #             angle[k] += vel[k]
        #             c1 = new_circ(radius[k],radius[k-1],centers[k-1][0],centers[k-1][1],angle[k])
        #             centers[k] = c1.center
        #             x1, y1 = c1.draw_circ()
        line[k].set_data(x1, y1)
        #print(line[k])
        # x = c1.center[0]
        # y = c1.center[1]

        if k == count-1:
            pntx.append(c1.center[0])
            pnty.append(c1.center[1])
            linep.set_data(pntx,pnty)
    return linep, line,

frames = int((2*np.pi/dtheta)/120)
anim = animation.FuncAnimation(
    fig, animate, init_func= init, frames=int(2*np.pi/dtheta), interval = 1, blit= False)
#anim.save('fractal circle 4.mp4', fps=frames, extra_args=['-vcodec', 'libx264'])
plt.show()

