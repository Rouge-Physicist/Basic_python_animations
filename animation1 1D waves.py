import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button

# with plt.xkcd():
#plt.style.use('dark_background')
fig,axi= plt.subplots()
# plt.rc('text',usetex = True)
# plt.rc('font', family = 'serif')
# plt.title(r"superimposing waves" r"$A\cos (kz-\omega t)$")
plt.subplots_adjust(bottom=0.3)
ax = plt.axes(xlim=(0,10),ylim=(-5,5))
ax.set_title('Superimposing fwd and bwd waves')
line, = ax.plot([],[],lw=2,color='r',alpha=0.3,label='fwd wave')
line2, = ax.plot([],[],lw=2,color='b',alpha=0.3,label = 'bwrd wave')
line3, = ax.plot([],[],lw=2,color='g',label = 'sum of waves')
ax.legend(loc = 'best')
ax.set_xlabel('distance (m) \n bring xkcd into the future')
ax.set_ylabel('Amplitude')
time_text = ax.text(0.05,0.95,'',horizontalalignment='left',verticalalignment='top',transform=ax.transAxes)

axcolor = 'lightgoldenrodyellow'
axlam1 = fig.add_axes([0.12, 0.05, 0.3, 0.03], facecolor=axcolor)
slam1 = Slider(axlam1, 'lambda 1', 0.1, 10, valinit=3, valstep=0.1)
axlam2 = fig.add_axes([0.6, 0.05, 0.3, 0.03], facecolor=axcolor)
slam2 = Slider(axlam2, 'lambda 2', 0.1, 10, valinit=3, valstep=0.1)

def init():
    line.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    time_text.set_text('')

    return line,line2,line3,

def generate_wave(Lambda, amplitude,i):
    phase = 0
    zspace = np.linspace(0, 10, 500)
    c = 3e8
    freq = c/Lambda
    t_step = 0.01 / freq
    w = 2 * np.pi * freq
    k = 2 * np.pi / Lambda
    y_wave = amplitude * np.cos(k * zspace - w * i * t_step + phase)
    return y_wave,zspace


# general form of wave is A*cos(k*z - w*t+phi)

def animate(i):
    new_lam = slam1.val
    new_lam2 = slam2.val
    y_wave,zspace = generate_wave(new_lam,2,i)
    y_wave2,zspace = generate_wave(new_lam2,2,-i)
    y_wave3 = y_wave+y_wave2
    line.set_data(zspace,y_wave)
    line2.set_data(zspace,y_wave2)
    line3.set_data(zspace,y_wave3)
    time_text.set_text('time = %.1d' % i)

    return line,line2,line3,time_text,

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=200,interval=10,blit=True)
ax.legend()

plt.show()

