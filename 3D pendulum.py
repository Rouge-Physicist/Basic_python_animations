
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Lagrangian : 1/2*m*l**2*(thetadot*sin(phi)**2+phidot**2)+m*g*l*cos(phi) where theta is the angle with z axis and phi the polar angle

#pv_cur strucutre: (r,phi,theta,rdot,phidot,thetadot)
# function to update pendulum
def new_pos(pv_cur,frames):
    t = np.arange(frames)
    points_rtp = np.array(pv_cur)
    points_xyz = np.array(
        [pv_cur[0] * np.cos(pv_cur[1]) * np.sin(pv_cur[2]), pv_cur[0] * np.sin(pv_cur[1]) * np.sin(pv_cur[2]),
         pv_cur[0] * np.cos(pv_cur[2])])

    for k in t:
        g = 9.8 #m/s**2
        l = 0.25 # m
        accel = np.array([0,0,pv_cur[4]**2*np.cos(pv_cur[2])*np.sin(pv_cur[2])-g*np.sin(pv_cur[2])/l])
        t_step = 0.02 # seconds
        pv_cur[-3:] += accel*t_step
        pv_cur[:3] += pv_cur[-3:]*t_step
        points_rtp = np.append(points_rtp,pv_cur[:3])
        pv_xyz = np.array([pv_cur[0]*np.cos(pv_cur[1])*np.sin(pv_cur[2]),pv_cur[0]*np.sin(pv_cur[1])*np.sin(pv_cur[2]),pv_cur[0]*np.cos(pv_cur[2])])
        points_xyz = np.append(points_xyz,pv_xyz)
    return points_xyz, points_rtp
global frames
frames = 2000

def animate(i):
    global pv_cur,x,y,z,E,pv_initial,thetavel_old,phivel_old, points_xyz, points_rtp
    m = 1
    l = 0.25
    g = 9.8
    disp = 0.5
    if i == 0 :
        # setting intial position of pendulum and initial velocity
        pv_cur = np.array([l,np.pi,np.pi/2,0,sphivel.val,sthetavel.val])
        points_xyz,points_rtp = new_pos(pv_cur,frames)
        x = points_xyz[0]+disp
        y = points_xyz[1]+disp
        z = -points_xyz[2]+disp
    if i > 0:
        x = np.append(x,points_xyz[3*i+0]+disp)
        y = np.append(y,points_xyz[3*i+1]+disp)
        z = np.append(z,-points_xyz[3*i+2]+disp)  #-pv_xyz[2]+disp)
        #setting reset animation condition upon altering initial values
        if sthetavel.val != thetavel_old or phivel_old != sphivel.val:
            # resets animation from scratch
            anim.frame_seq = anim.new_frame_seq()
    #setting position of pendulum
    x2 = np.array([disp,points_xyz[3*i+0]+disp])
    y2 = np.array([disp,points_xyz[3*i+1]+disp])
    z2 = np.array([disp,-points_xyz[3*i+2]+disp])
    #updating line information to be displayed
    line[0].set_xdata(x)
    line[0].set_ydata(y)
    line[0].set_3d_properties(z)
    line2[0].set_xdata(x2)
    line2[0].set_ydata(y2)
    line2[0].set_3d_properties(z2)
    #line3[0].set_data(np.array([points_xyz[3*i+0]+disp,points_xyz[3*i+0]+disp]),np.array([points_xyz[3*i+1]+disp,points_xyz[3*i+1]+disp]))
    #line3[0].set_3d_properties(np.array([0,-points_xyz[3*i+2]+disp]))
    #saving old values to check value change
    thetavel_old = sthetavel.val
    phivel_old = sphivel.val
    return line,line2,#line3,
# with plt.xkcd():
#setting up figure
# plt.style.use('default')

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
line=ax.plot([],[],[],label='xy-projection')
line2=ax.plot([],[],[],marker='o',label='pendulum')
#line3 = ax.plot([],[],[],alpha=0.3,color='r')
ax.legend(loc='best')
#setting up sliders
axcolor = 'lightgoldenrodyellow'
axphivel = fig.add_axes([0.2, 0.05, 0.2, 0.03], facecolor=axcolor)
sphivel = Slider(axphivel, 'phi initial vel', 0, 10, valinit=0, valstep=0.5)
axthetavel = fig.add_axes([0.7, 0.05, 0.2, 0.03], facecolor=axcolor)
sthetavel = Slider(axthetavel, 'theta initial vel', 0, 10, valinit=0, valstep=0.5)
#animating pendulum
anim = animation.FuncAnimation(fig, animate, frames=frames,interval=1, blit=False)
plt.show()
