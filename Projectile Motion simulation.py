import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button
# makes plot look like xkcd format
# with plt.xkcd():
fig,axi = plt.subplots()
plt.subplots_adjust(bottom=0.3)
ax = plt.axes(xlim=(0, 280), ylim=(0, 150))
ax2 = ax.twinx()
ax2.set_ylim(-50,50)
ax.set_title('projectile motion')
ax2.set_ylabel('velocity (m/s)')
line, = ax.plot([], [], lw=2, color='b', alpha=1, label='projectile path')
line2, = ax2.plot([], [], lw=2, color='m', alpha=1, label='mod(velocity)')
line3, = ax2.plot([], [], lw=2, color='r', alpha=0.3, label='velocity-x')
line4, = ax2.plot([], [], lw=2, color='g', alpha=0.3, label='velocity-y')
ax.legend(loc='best')
ax2.legend(loc=4)
time_text = ax.text(0.05,0.95,'',horizontalalignment='left',verticalalignment='top',transform=ax.transAxes)

axcolor = 'lightgoldenrodyellow'
axangle = fig.add_axes([0.2, 0.05, 0.2, 0.03], facecolor=axcolor)
sangle = Slider(axangle, 'angle', 1, 90, valinit=45, valstep=0.5)
axvel = fig.add_axes([0.65, 0.05, 0.2, 0.03], facecolor=axcolor)
svel = Slider(axvel, 'V initial', 20, 50, valinit=20, valstep=1)
axgrav = fig.add_axes([0.65, 0.1, 0.2, 0.03], facecolor=axcolor)
sgrav = Slider(axgrav, 'Gravity', 9.8/4, 3*9.8, valinit=9.8, valstep=0.1)


def calculate_path(v_prev,s_prev,g,angle,v_in):
    t_tot = 2*(50)
    t_step = t_tot/2500
    v_new = np.array([v_prev[0],v_prev[1]-g*t_step])
    s_new = v_new*t_step
    s = s_prev + s_new
    return s,v_new

def init():
    line.set_data(np.array([[]]), np.array([[]]))
    line2.set_data(np.array([[]]), np.array([[]]))
    line3.set_data(np.array([[]]), np.array([[]]))
    line4.set_data(np.array([[]]), np.array([[]]))
    time_text.set_text('')
    return line,line2,line3,line4,time_text

def animate(i):
    global v_cur, g_old, angle_old, x, y,v_in,s_cur, v_old, v, vx, vy
    angle = sangle.val
    v_in = svel.val
    if i == 0:
        v_cur = np.array([v_in*np.cos(np.deg2rad(angle)),v_in*np.sin(np.deg2rad(angle))])
        s_cur = np.array([0,0])
    g = sgrav.val
    s_cur,v_cur = calculate_path(v_cur,s_cur,g,angle,v_in)
    if i == 0:
        x = s_cur[0]
        y = s_cur[1]
        v = np.array(np.linalg.norm(v_cur))
        vx = v_cur[0]
        vy = v_cur[1]
    else:
        x = np.append(x,s_cur[0])
        y = np.append(y,s_cur[1])
        v = np.append(v, np.linalg.norm(v_cur))
        vx = np.append(vx, v_cur[0])
        vy = np.append(vy, v_cur[1])
    if i > 0:
        if v_in != v_old or angle != angle_old or s_cur[1] < 0:
            # resets animation from scratch
            anim.frame_seq = anim.new_frame_seq()
    line.set_data(x,y)
    line2.set_data(x,v)
    line3.set_data(x,vx)
    line4.set_data(x,vy)

    time_text.set_text('time = %.1d' % i)
    angle_old = sangle.val
    v_old = svel.val
    g_old = sgrav.val

    return line,line2,line3,line4,time_text,

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=2500,interval=100,blit=True)

plt.show()


