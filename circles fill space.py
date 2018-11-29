import turtle as t
import numpy as np
import random
import time
#start = time.time()

def draw_poly(center,r):
    np.append(position,position[0])
    for i in range(len(position)):
        if i==0:
            t.up()
        else:
            t.down()
        t.goto(np.real(position[i])+center[0],np.imag(position[i])+center[1])
    return r,theta

def pol_to_cart(pos):
    x = pos[1]*np.cos(pos[2])
    y = pos[1]*np.sin(pos[2])
    return x,y,



def draw_circ(prop):
    x = prop[1]*np.cos(prop[2])
    y = prop[1]*np.sin(prop[2])
    t.up()
    t.setpos(x,y)
    t.right(90)
    t.forward(prop[0])
    t.right(270)
    t.down()
    t.circle(prop[0])
    t.up()

pts = [[0,0,0]]

def make_point():
    angle = random.random()*2*np.pi
    for i in range(len(theta)):
        if angle>=theta[i]:
            ind = i
    x1 = poly_r*np.cos(theta[ind])
    x2 = poly_r*np.cos(theta[ind+1])
    y1 = poly_r * np.sin(theta[ind])
    y2 = poly_r * np.sin(theta[ind + 1])
    m1 = (y1-y2)/(x1-x2)
    m2 = np.sin(angle)/np.cos(angle)
    x = (-m1*x1+y1)/(m2-m1)
    y = m2*x
    R = np.linalg.norm(x+1j*y)
    r = random.random()*R
    rad = 3
    pos = [rad,r,angle,0]
    return pos
def check_inter_and_updt(pos):
    for i in range(len(pos)):
        if pos[i][3]==1:
            pass
        else:
            x0, y0 = pol_to_cart(pos[i])
            for k in range(len(theta)):
                if pos[i][2] > theta[k]:
                    ind = int(k)
                elif pos[i][2]==0 or pos[i][2]==2*np.pi:
                    ind = 0
            x1 = poly_r * np.cos(theta[ind])
            x2 = poly_r * np.cos(theta[ind + 1])
            y1 = poly_r * np.sin(theta[ind])
            y2 = poly_r * np.sin(theta[ind + 1])
            dist = np.abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)/np.sqrt((y2-y1)**2+(x2-x1)**2)
            if dist <= pos[i][0]:
                pos[i][3] = 1
            # xtemp,ytemp = pol_to_cart(pos[i])
            # range = xtemp+pos[i][0]
            for j in range(len(pos)):
                if i==j or pos[i][3]==1:
                    pass
                else:
                    x1,y1 = pol_to_cart(pos[j])
                    dis = np.sqrt(((x0-x1)**2) + ((y0-y1)**2))
                    if dis <=(pos[i][0]+pos[j][0]):
                        pos[i][3] =1
            if pos[i][3] == 0:
                pos[i][0] += 1

    return pos




R =200
n = 10
global max_r
max_r = 0
#t.color('white','red')
#t.screensize(2000,2000,'black')
global theta
theta = np.linspace(0,2*np.pi,n+1)
global poly_r
poly_r = 200 / np.cos((2 * np.pi / n) / 2)
global pos
position = poly_r*np.exp(1j*theta)
t.tracer(0,0)
t.setpos(0,0)

pos = [[0,0,0,0]]
for i in range(R):
    for x in pos:
        #t.begin_fill()
        # if x[0] > max_r:
        #     max_r = x[0]
        draw_circ(x)
        #t.end_fill()
    pos = check_inter_and_updt(pos)
    for l in range(5):
        new_pt = make_point()
        iter = 0
        for j in range(len(pos)):
            if iter == 1:
                pass
            else:
                x1,y1 = pol_to_cart(new_pt)
                x2,y2 = pol_to_cart(pos[j])
                distance = np.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
                if distance < pos[j][0]:
                    iter=1
        if iter == 0:
            pos.append(new_pt)
    draw_poly([0, 0], 200 / np.cos((2 * np.pi / n) / 2))
    t.up()
    t.update()
    if i <R-1:
        t.reset()

t.update()
#end = time.time()
t.done()

#print(end-start)