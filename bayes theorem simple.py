import numpy as np
import scipy as sp
import random as rdm
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button
import collections as co

## BAYES THEOREM ##

''' 
P(H\D) = P(D/H)*P(H)/P(D)
where P(H) is the prior: general probability of our hypothesis
      P(D/H) is the likelihood: the probability of the data given our hypothesis is true
      P(H/D) is the posterior
      P(D) is the probability of the data regardless of hypothesis
      P(D) = int_a^b p(D/H)*P(H) dH
    Say we are working with a coing which has a unknown bias towards either heads or tails
    Firstly we should say that our initial prior should be teh "flat" prior or a uniform distribution
    but then we will slowly introduce more data and update our pdf function for the bias.
'''

## FIGURE SETUP ##
fig,axi = plt.subplots()
ax = plt.axes(xlim=(0,1),ylim=(0,1))
line, = ax.plot([],[],lw=2,color='r',alpha=1,label='bias pdf')
time_text = ax.text(0.05,0.95,'',horizontalalignment='left',verticalalignment='top',transform=ax.transAxes)

def init():
    line.set_data([],[])
    time_text.set_text('')
    return line,
N = 100
trial_num = 1000
bias = 0.2
global rdm_nums
rdm_nums = np.random.uniform(0,1,trial_num)+bias
rdm_nums[0] = 0.6
'''
    Assume the P(heads) = x and P(tails) = 1-x 
    and initial prior is 1
    
'''
global x
x = np.linspace(0,1,N)
global prior
prior = [1/len(x) for i in x]
Area = np.trapz(prior,x,x[1]-x[0])
print(sum(prior))
print(Area)

def posterior_cal(Data,prior,Hypothesis):
    Heads = False
    if Data >= 0.5:
        Heads = True
    '''
        numerator: P(D/H)*P(H)
        denominator: P(D)
    '''
    if Heads == False:
        numerator = prior * (1 - Hypothesis)
        #denominator =  np.trapz(prior*(1-Hypothesis),Hypothesis,Hypothesis[1]-Hypothesis[0],0)
    else:
        numerator = prior * (Hypothesis)
        #denominator = np.trapz(prior * (Hypothesis), Hypothesis,Hypothesis[1]-Hypothesis[0],0)
    denominator = sum(numerator)
    posterior = numerator/denominator
    return posterior


def animate(i):
    global prior, x,rdm_nums
    prior = posterior_cal(rdm_nums[i],prior,x)
    line.set_data(x,prior)
    heads_num = dict(co.Counter(rdm_nums[:i]>0.5))[True]
    tails_num = len(rdm_nums[:i])-heads_num
    time_text.set_text('heads num = %.1d' % heads_num +' tails num = %.1d' % tails_num)
    return line, time_text,

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=trial_num,interval=1,blit=True)
ax.legend()

plt.show()


