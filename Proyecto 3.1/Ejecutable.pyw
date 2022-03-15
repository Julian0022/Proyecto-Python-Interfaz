### Ejecutable proyecto Programacion 2 - Interfaz grafica ###

from tkinter import *
from Funcion.RL import *
from Funcion.RC import *

TipoC = True
#Funciones

def ready():
	if TipoC:
		Vs = float(EVs.get())
		Vo = float(EVo.get())
		R = float(ER.get())
		C = float(EC.get())
		CasoC = RCfuncion(Vo,Vs,R,C)
		ImagenGRC['file'] = 'Funcion/RC_foto.png'
		EcuacionFormula['text'] = f'{CasoC}  [V]'
		EcuacionImagen['image'] = ImagenGRC
	else:
		Is = float(EVs.get())
		Io = float(EVo.get())
		R = float(ER.get())
		L = float(EC.get())
		CasoL = RLfuncion(Io,Is,R,L)
		ImagenGRL['file'] = 'Funcion/RL_foto.png'
		EcuacionFormula['text'] = f'{CasoL}  [A]'
		EcuacionImagen['image'] = ImagenGRL


def RC():
	global TipoC
	TipoC = True
	Titulo2['text'] = "Circuito RC"
	EcuacionFormula['text'] = "V(t) = Vo*e^(-t/J) + Vs(1-e^(-t/J)) [V]"
	EcuacionImagenmodelo['image'] = IRC
	l1['text'] = "Voltaje de la fuente: "
	l3['text'] = "Voltaje inicial del capacitor: "
	l4['text'] = "Capacitancia: "
	EcuacionImagen['image'] = Imagen

def RL():
	global TipoC
	TipoC = False
	Titulo2['text'] = "Circuito RL"
	EcuacionFormula['text'] = "I(t) = Io*e^(-t/J) + Is(1-e^(-t/J)) [A]"
	EcuacionImagenmodelo['image'] = IRL
	l1['text'] = "Intensidad de la fuente: "
	l3['text'] = "Intensidad inicial del inductor: "
	l4['text'] = "Inductancia: "
	EcuacionImagen['image'] = Imagen



#Datos de la raiz

raiz = Tk()
raiz.title('RC and RL')
raiz.resizable(0,0)
raiz.iconbitmap('icono.ico')

#Datos del main Frame

mainFrame = Frame()
mainFrame.pack()
mainFrame.config(bg='white')

#Objetos

Titulo = Label(mainFrame, text='Análisis RC y RL')
Titulo.grid(row=0, column=0, sticky='sn', padx=50, pady=10)
Titulo.config(bg='white',font=('Arial', 30))

texintro = Label(mainFrame, text="""Los circuitos de primer orden son circuitos que contienen solamente un componente que 
almacena energía (puede ser un condensador o inductor), y que además pueden describirse
usando solamente una ecuación diferencial de primer orden. Los dos posibles tipos de 
circuitos primer orden:

1.Circuito RC (Resistor y Condensador)
2.Circuito RL (Resistor e Inductor)

Elija el tipo de circuito que desea analizar y luego ingrese los valores de resistencia, 
capacitancia/inductancia, voltaje/corriente inicial y voltaje/corriente de la fuente (en caso
de querer analizar el circuito en descarga ingrese el valor de la fuente como 0).""", justify=LEFT)
texintro.grid(row=1, column=0, sticky='sn', padx=45, pady=10)
texintro.config(bg='white',font=('Arial', 13))

ImagenGRC = PhotoImage(file='Funcion/RC_foto.png')
ImagenGRL = PhotoImage(file='Funcion/RL_foto.png')
Imagen = PhotoImage(file='Funcion/output.png')
EcuacionImagen = Label(mainFrame, image=Imagen, bg='white')
EcuacionImagen.grid(row=4, column=0, sticky='sn', padx=20, pady=10)

#Parte derecha

Titulo2 = Label(mainFrame, text='Circuito RC')
Titulo2.grid(row=0, column=1, sticky='sn', padx=50, pady=10)
Titulo2.config(bg='white',font=('Arial', 30))

ImagenRC = PhotoImage(file='rc.png')
IRC = ImagenRC.subsample(2)
ImagenRL = PhotoImage(file='rl.png')
IRL = ImagenRL.subsample(2)
EcuacionImagenmodelo = Label(mainFrame, image=IRC)
EcuacionImagenmodelo.grid(row=1, column=1, sticky='sn', padx=20, pady=10)

#Parte inferior

#Segundo Frame

Frame2 = Frame(mainFrame)
Frame2.grid(row=3, column=0, sticky='sn', padx=50, pady=10)
Frame2.config(bg='white')

EcuacionLabel = Label(Frame2, text='Ecuación: ')
EcuacionLabel.grid(row=0, column=0, sticky='sn', padx=20, pady=10)
EcuacionLabel.config(bg='white',font=('Arial', 20))

EcuacionFormula = Label(Frame2, text='V(t) = Vo*e^(-t/J) + Vs(1-e^(-t/J)) [V]')
EcuacionFormula.grid(row=0, column=1, sticky='sn', padx=10, pady=10)
EcuacionFormula.config(bg='white',font=('Arial', 20))

#Tercer Frame

Frame3 = Frame(mainFrame)
Frame3.grid(row=3, column=1, sticky='s', padx=40, pady=10)
Frame3.config(bg='white')

BotonRC = Button(Frame3, text='Analizar Circuito RC', command=RC, font=('Arial', 13))
BotonRC.grid(row=0, column=0, sticky='sn', padx=40, pady=10)

BotonRL = Button(Frame3, text='Analizar Circuito RL', command=RL, font=('Arial', 13))
BotonRL.grid(row=0, column=1, sticky='sn', padx=40, pady=10)

#Cuarto Frame

Frame4 = Frame(mainFrame)
Frame4.grid(row=4, column=1, sticky='sn', padx=20, pady=10)
Frame4.config(bg='white')

Botonready = Button(Frame4, text='Listo!', command=ready, font=('Arial', 13))
Botonready.grid(row=1, column=0, sticky='s', padx=250, pady=10)

#Quinto Frame ###############################################################################################

Frame5 = Frame(Frame4)
Frame5.grid(row=0, column=0, sticky='w', padx=50, pady=10)
Frame5.config(bg='white')

l1 = Label(Frame5,text='Voltaje de la fuente: ', justify=LEFT)
l1.grid(row=0, column=0, sticky='w', padx=5, pady=10)
l1.config(bg='white',font=('Arial', 16))

EVs = Entry(Frame5)
EVs.grid(row=0, column=1, sticky='sn', padx=5, pady=10)

l2 = Label(Frame5,text='Resistencia: ', justify=LEFT)
l2.grid(row=1, column=0, sticky='w', padx=5, pady=10)
l2.config(bg='white',font=('Arial', 16))

ER = Entry(Frame5)
ER.grid(row=1, column=1, sticky='sn', padx=5, pady=10)

l3 = Label(Frame5,text='Voltaje inicial del capacitor: ', justify=LEFT)
l3.grid(row=2, column=0, sticky='w', padx=5, pady=10)
l3.config(bg='white',font=('Arial', 16))

EVo = Entry(Frame5)
EVo.grid(row=2, column=1, sticky='sn', padx=5, pady=10)

l4 = Label(Frame5,text='Capacitancia: ', justify=LEFT)
l4.grid(row=3, column=0, sticky='w', padx=5, pady=10)
l4.config(bg='white',font=('Arial', 16))

EC = Entry(Frame5)
EC.grid(row=3, column=1, sticky='sn', padx=5, pady=10)






raiz.mainloop()

