from matplotlib import pyplot as plt
import numpy as np
from math import e

def RLfuncion(Io,Is,R,L):
    T = L/R
    x = np.linspace(0,5*T,100)
    y= (Io*(e)**-(x/T))+(Is*(1-(e)**-(x/T)))

    x2 = np.linspace(-10,0,10)
    y2 = [Io]*10

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Circuito RL')
    ax.set_ylabel('Corriente [A]')
    ax.set_xlabel('Tiempo [s]')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    if Io>Is:
        ax.set_ylim([0, Io])
    else: ax.set_ylim([0, Is])

    # plot the function
    plt.plot(x,y, label = "y")
    plt.plot(x2, y2, label = "line 2")
    # show the plot
    plt.savefig('Funcion/RL_foto.png')
    return f"I(t) = {Io}e^(-t/{T}) + {Is}(1-e^(-t/{T}))"
