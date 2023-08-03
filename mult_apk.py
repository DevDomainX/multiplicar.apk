import tkinter as tk
from tkinter import PhotoImage
import random


def actualizar_etiqueta():
    global n1
    n1 = random.randint(1, 12)
    global n2
    n2 = random.randint(1, 12)
    etiqueta1.config(text=f"{n1} x {n2} = ")
    
    
def respuesta():
     total = entrada.get() 
     if total == str(n1*n2):
        mensaje.config(text=f"¡ Exelente !! ")
     else:
        mensaje.config(text="lo siento, mal")
     
def salir():
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Ejercicios de Multiolicaciones ")
ventana.title("multiplicaciones")
ventana.config(bg="black")

#imagen = tk.PhotoImage(file="bart.png")

#foto = tk.Label(ventana, foto = imagen)
#foto.place(x=23, y=70)


titulo = tk.Label(ventana, text="Ejercicios de Multiplicacion", fg="cyan", font=("arial 13"), bg="black")
titulo.place(x=120, y=200)

etiqueta1 = tk.Label(ventana, text="¡ iniciar !\nSiguiente", fg="cyan", font=("arial 30"), bg="black")
etiqueta1.place(x=250, y=500)

mensaje = tk.Label(ventana, text="Resultado", fg="cyan", font=("Curier 10"), bg="black")
mensaje.place(x=350, y=1000)

entrada = tk.Entry(ventana, text="ingreso", justify=tk.CENTER, font=("arial 10"), bg="black", bd=30, fg="cyan")
entrada.place(x=200, y=1200)

boton2 = tk.Button(ventana, text="Verificar", command=respuesta, fg="cyan", bg="black", bd=15)
boton2.place(x=400, y=1400)

boton =tk.Button(ventana, text="Siguiente", command=actualizar_etiqueta, fg="cyan", bg="black", bd=15)
boton.place(x=400, y=1600)

salir = tk.Button(ventana, text="Salir...", command=salir, fg="cyan", bg="black", bd=15)
salir.place(x=700, y=1800)

profe = tk.Label(ventana, text="Para profesor: Luis Cid", fg="cyan", bg="black", font=("arial 10"))
profe.place(x=10, y=1850)

liceo= tk.Label(ventana, text="Liceo polivalente de molina", fg="cyan", bg="black", font=("arial 10"))
liceo.place(x=10, y=1950)

creador= tk.Label(ventana, text="Creador: Hans Saldias", fg="cyan", bg="black", font=("arial 10"))
creador.place(x=10, y=2030)

#boton3 = tk.Button(ventana, text="limpiar")
#boton3.place(x=60, y=300)

#ventana.after(3, actualizar_etiqueta)

ventana.mainloop()