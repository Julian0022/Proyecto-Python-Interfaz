from matplotlib import pyplot as plt
import numpy as np
from math import e

def RCfuncion(Vo,Vs,R,C):
    T = R*C
    x = np.linspace(0,5*T,100)
    y= (Vo*(e)**-(x/T))+(Vs*(1-(e)**-(x/T)))

    x2 = np.linspace(-10,0,10)
    y2 = [Vo]*10

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Circuito RC')
    ax.set_ylabel('Voltaje [V]')
    ax.set_xlabel('Tiempo [s]')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    if Vo>Vs:
        ax.set_ylim([0, Vo])
    else: ax.set_ylim([0, Vs])

    # plot the function
    plt.plot(x,y, label = "y")
    plt.plot(x2, y2, label = "line 2")
    # show the plot
    plt.savefig('Funcion/RC_foto.png')
    return f"V(t) = {Vo}e^(-t/{T}) + {Vs}(1-e^(-t/{T}))"
