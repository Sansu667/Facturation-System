from tkinter import *
import random
import datetime
from tkinter import messagebox, filedialog

operador = ""
precios_comida = [10, 15, 20, 25, 30, 10, 15, 5, 5, 20]
precios_bebida = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
precios_postres = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Funciones

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END) # Limpiar el visor
    visor_calculadora.insert(END, operador) # Insertar el operador en el visor
    
def obtener_resultado():
    global operador
    resultado = str(eval(operador)) # Evaluar la operación
    visor_calculadora.delete(0, END) # Limpiar el visor
    visor_calculadora.insert(END, resultado) # Insertar el resultado en el visor
    operador = "" # Reiniciar el operador
    
def revisar_check():
    costo_comida = 0 # Inicializar el costo de la comida
    costo_bebida = 0 # Inicializar el costo de la bebida
    costo_postres = 0 # Inicializar el costo de la postre
    subtotal = 0 # Inicializar el subtotal
    impuesto = 0 # Inicializar el impuesto
    total = 0 # Inicializar el total
    
    # Recorrer las comidas
    for i in cuadros_comida: # Recorrer la lista de comidas
        if variables_comida[costo_comida].get() == 1: # Condición
            cuadros_comida[costo_comida].config(state=NORMAL) # Habilitar el cuadro de entrada
            if cuadros_comida[costo_comida].get() == "0":
                cuadros_comida[costo_comida].delete(0, END) # Limpiar el cuadro de entrada
            cuadros_comida[costo_comida].focus() # Enfocar el cuadro de entrada
        else: # Condición
            cuadros_comida[costo_comida].config(state=DISABLED) # Deshabilitar el cuadro de entrada
            texto_comida[costo_comida].set(0) # Reiniciar el valor del cuadro de entrada
        costo_comida += 1 
    
    # Recorrer las bebidas
    for i in cuadros_bebida: # Recorrer la lista de bebidas
        if variables_bebida[costo_bebida].get() == 1: # Condición
            cuadros_bebida[costo_bebida].config(state=NORMAL) # Habilitar el cuadro de entrada
            if cuadros_bebida[costo_bebida].get() == "0":
                cuadros_bebida[costo_bebida].delete(0, END) # Limpiar el cuadro de entrada
            cuadros_bebida[costo_bebida].focus() # Enfocar el cuadro de entrada
        else: # Condición
            cuadros_bebida[costo_bebida].config(state=DISABLED) # Deshabilitar el cuadro de entrada
            texto_bebida[costo_bebida].set(0) # Reiniciar el valor del cuadro de entrada
        costo_bebida += 1 
    
    # Recorrer los postres
    for i in cuadros_postres: # Recorrer la lista de postres
        if variables_postres[costo_postres].get() == 1: # Condición
            cuadros_postres[costo_postres].config(state=NORMAL) # Habilitar el cuadro de entrada
            if cuadros_postres[costo_postres].get() == "0":
                cuadros_postres[costo_postres].delete(0, END) # Limpiar el cuadro de entrada
            cuadros_postres[costo_postres].focus() # Enfocar el cuadro de entrada
        else: # Condición
            cuadros_postres[costo_postres].config(state=DISABLED) # Deshabilitar el cuadro de entrada
            texto_postres[costo_postres].set(0) # Reiniciar el valor del cuadro de entrada
        costo_postres += 1 
            
def total():
    sub_total_comida = 0 # Inicializar el subtotal de la comida
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p]) # Calcular el subtotal de la comida
        p += 1
    print(sub_total_comida)
    
    sub_total_bebida = 0 # Inicializar el subtotal de la bebida
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p]) # Calcular el subtotal de la bebida
        p += 1
        
    sub_total_postres = 0 # Inicializar el subtotal de los postres
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p]) # Calcular el subtotal de los postres
        p += 1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres # Calcular el subtotal
    impuesto = sub_total * 0.19 # Calcular el impuesto
    total = sub_total + impuesto # Calcular el total
    
    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}") # Asignar el subtotal de la comida
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}") # Asignar el subtotal de la bebida
    var_costo_postres.set(f"$ {round(sub_total_postres, 2)}") # Asignar el subtotal de los postres
    var_subtotal.set(f"$ {round(sub_total, 2)}") # Asignar el subtotal
    var_impuesto.set(f"$ {round(impuesto, 2)}") # Asignar el impuesto
    var_total.set(f"$ {round(total, 2)}") # Asignar el total
    
def recibo():
    texto_recibo.delete("1.0", END) # Limpiar el area de texto
    num_recibo = f"N# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    texto_recibo.insert(END, f"Tu recibo: \t{num_recibo}\t\t{fecha}\n")
    texto_recibo.insert(END, f"*" *64 + "\n")
    texto_recibo.insert(END, f"Items\t\tCantidad\t\tPrecio\n")
    texto_recibo.insert(END, f"*" *64 + "\n")
    
    x = 0 
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comida[x]}\t\t{comida.get()}\t" f"\t$ {round(int(comida.get()) * precios_comida[x], 2)}\n")
        x += 1
        
    x = 0     
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t" f"\t$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n")
        x += 1
        
    x = 0     
    for postre in texto_postres:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t" f"\t$ {round(int(postre.get()) * precios_postres[x], 2)}\n")
        x += 1
        
    texto_recibo.insert(END, f"*" *64 + "\n")
    texto_recibo.insert(END, f"Subtotal:\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuesto:\t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" *64 + "\n")
    texto_recibo.insert(END, "Gracias por tu compra\n")

def guardar():
    info_recibo = texto_recibo.get("1.0", END) # Obtener el texto del area de texto
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt") # Abrir un archivo
    archivo.write(info_recibo) # Escribir el texto en el archivo
    archivo.close() # Cerrar el archivo
    messagebox.showinfo("Guardado", "El recibo ha sido guardado") # Mostrar un mensaje
    
def resetear():
    for i in range(10):
        texto_comida[i].set(0)
        texto_bebida[i].set(0)
        texto_postres[i].set(0)
        
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED) # Reiniciar el valor del cuadro de entrada
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED) # Reiniciar el valor del cuadro de entrada
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED) # Reiniciar el valor del cuadro de entrada
    
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)
        
    var_costo_comida.set("") # Asignar el subtotal de la comida
    var_costo_bebida.set("") # Asignar el subtotal de la bebida
    var_costo_postres.set("") # Asignar el subtotal de los postres
    var_subtotal.set("") # Asignar el subtotal
    var_impuesto.set("") # Asignar el impuesto
    var_total.set("") # Asignar el total
    texto_recibo.delete("1.0", END) # Limpiar el area de texto
    visor_calculadora.delete(0, END) # Limpiar el visor
    global operador
    operador = "" # Reiniciar el operador

#Iniciar tkinter
aplicacion = Tk() # Crear la ventana principal

# Tamaño de la ventana
aplicacion.geometry("1200x630+0+0") # anchura x altura

# Evitar maximixar
aplicacion.resizable(False,False) # (x,y) 1 = True, 0 = False

# Titulo de la ventana
aplicacion.title("Food Light - Sistema de facturación") # Titulo de la ventana

# Color de fondo
aplicacion.config(bg = "gray") # Color de fondo de la ventana

# ----- Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)   # Crear un panel superior
panel_superior.pack(side=TOP) # Empaquetar el panel superior

# Etiqueta título
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4", font=("Arial", 24, "bold"), bg="black", width=27) # Crear una etiqueta
etiqueta_titulo.grid(row=0, column=0) # Posicionar la etiqueta

# ----- Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)   # Crear un panel izquierdo
panel_izquierdo.pack(side=LEFT) # Empaquetar el panel izquierdo

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=100)   # Crear un panel costos
panel_costos.pack(side=BOTTOM) # Empaquetar el panel costos

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, bd=1, relief=FLAT, text="Comidas", font=("Arial", 24, "bold"), fg="azure4")   # Crear un panel comidas
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, bd=1, relief=FLAT, text="Bebidas", font=("Arial", 24, "bold"), fg="azure4")   # Crear un panel bebidas
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, bd=1, relief=FLAT, text="Postres", font=("Arial", 24, "bold"), fg="azure4")   # Crear un panel postres
panel_postres.pack(side=RIGHT)

# ----- Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)   # Crear un panel derecho
panel_derecho.pack(side=RIGHT) # Empaquetar el panel derecho

# Panel calculadora 
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT)   # Crear un panel calculadora
panel_calculadora.pack(side=TOP) # Empaquetar el panel calculadora

# Panel recibo 
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT)   # Crear un panel recibo
panel_recibo.pack(side=TOP) # Empaquetar el panel recibo

# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT)   # Crear un panel botones
panel_botones.pack(side=BOTTOM) # Empaquetar el panel botones

# ----- Lista de productos
lista_comida = ["Pollo", "Cordero", "Carne de Res", "Pescado", "Camarones", "Pasta", "Pizza", "Ensalada", "Sopa", "Sushi"]
lista_bebidas = ["Agua", "Gaseosa", "Jugo", "Cerveza", "Vino", "Cóctel", "Whisky", "Ron", "Tequila", "Pisco"]
lista_postres = ["Helado", "Torta", "Gelatina", "Flan", "Mazamorra", "Arroz con leche", "Mousse", "Tiramisú", "Cheesecake", "Brownie"]

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0 
for comida in lista_comida: # Recorrer la lista de comidas
    
    # Crear checkbutton
    variables_comida.append("")
    variables_comida[contador] = IntVar() # Crear una variable para cada comida
    comida = Checkbutton(panel_comidas, text=comida.title(), font=("Arial", 16, "bold"), fg="azure4", onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_check) # Crear una comida
    comida.grid(row=contador, column=0, sticky=W) # Posicionar la comida
    
    # Crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar() # Crear una variable para cada comida
    texto_comida[contador].set(0) # Inicializar la variable en 0
    cuadros_comida[contador] = Entry(panel_comidas, font=("Arial", 16, "bold"), fg="azure4", width=6, bd=1, state=DISABLED, textvariable=texto_comida[contador]) # Crear un cuadro de entrada
    cuadros_comida[contador].grid(row=contador, column=1, sticky=W) # Posicionar el cuadro de entrada
    
    contador += 1 # Incrementar el contador
    
# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0 
for bebida in lista_bebidas: # Recorrer la lista de bebidas
    
    # Crear checkbutton
    variables_bebida.append("")
    variables_bebida[contador] = IntVar() # Crear una variable para cada bebida
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Arial", 16, "bold"), fg="azure4", onvalue=1, offvalue=0, variable=variables_bebida[contador], command=revisar_check) # Crear una bebida
    bebida.grid(row=contador, column=0, sticky=W) # Posicionar la bebida
    
    # Crear los cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar() # Crear una variable para cada comida
    texto_bebida[contador].set(0) # Inicializar la variable en 0
    cuadros_bebida[contador] = Entry(panel_bebidas, font=("Arial", 16, "bold"), fg="azure4", width=6, bd=1, state=DISABLED, textvariable=texto_bebida[contador]) # Crear un cuadro de entrada
    cuadros_bebida[contador].grid(row=contador, column=1, sticky=W) # Posicionar el cuadro de entrada
    
    contador += 1 # Incrementar el contador

# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0 
for postre in lista_postres: # Recorrer la lista de postres
    
    # Crear checkbutton
    variables_postres.append("")
    variables_postres[contador] = IntVar() # Crear una variable para cada postres
    postre = Checkbutton(panel_postres, text=postre.title(), font=("Arial", 16, "bold"), fg="azure4", onvalue=1, offvalue=0, variable=variables_postres[contador], command=revisar_check) # Crear una postre
    postre.grid(row=contador, column=0, sticky=W) # Posicionar la postre
    
    # Crear los cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar() # Crear una variable para cada comida
    texto_postres[contador].set(0) # Inicializar la variable en 0
    cuadros_postres[contador] = Entry(panel_postres, font=("Arial", 16, "bold"), fg="azure4", width=6, bd=1, state=DISABLED, textvariable=texto_postres[contador]) # Crear un cuadro de entrada
    cuadros_postres[contador].grid(row=contador, column=1, sticky=W) # Posicionar el cuadro de entrada
    
    contador += 1 # Incrementar el contador

# Variables
var_costo_comida = StringVar() # Variable para el costo de la comida
var_costo_bebida = StringVar() # Variable para el costo de la bebida
var_costo_postres = StringVar() # Variable para el costo de la postre
var_subtotal = StringVar() # Variable para el subtotal
var_impuesto = StringVar() # Variable para el impuesto
var_total = StringVar() # Variable para el total

# Etiquetas de costo y campos de entrada
etiqueta_costo = Label(panel_costos, text="Costo Comida", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_costo.grid(row=0, column=0, sticky=W) # Posicionar la etiqueta

texto_costo = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_costo_comida) # Crear un cuadro de entrada
texto_costo.grid(row=0, column=1, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos, text="Costo Bebida", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_costo_bebida.grid(row=1, column=0, sticky=W) # Posicionar la etiqueta

texto_costo_bebida = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_costo_bebida) # Crear un cuadro de entrada
texto_costo_bebida.grid(row=1, column=1, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Etiquetas de costo y campos de entrada
etiqueta_costo_postres = Label(panel_costos, text="Costo Postres", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_costo_postres.grid(row=2, column=0, sticky=W) # Posicionar la etiqueta

texto_costo_postres = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_costo_postres) # Crear un cuadro de entrada
texto_costo_postres.grid(row=2, column=1, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Etiquetas de costo y campos de entrada
etiqueta_subtotal = Label(panel_costos, text="Subtotal", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_subtotal.grid(row=0, column=2, sticky=W) # Posicionar la etiqueta

texto_subtotal = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_subtotal) # Crear un cuadro de entrada
texto_subtotal.grid(row=0, column=3, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Etiquetas de costo y campos de entrada
etiqueta_impuesto = Label(panel_costos, text="Impuestos", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_impuesto.grid(row=1, column=2, sticky=W) # Posicionar la etiqueta

texto_impuesto = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_impuesto) # Crear un cuadro de entrada
texto_impuesto.grid(row=1, column=3, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Etiquetas de costo y campos de entrada
etiqueta_total = Label(panel_costos, text="Total", font=("Arial", 12, "bold"), fg="white", bg="azure4") # Crear una etiqueta
etiqueta_total.grid(row=2, column=2, sticky=W) # Posicionar la etiqueta

texto_total = Entry(panel_costos, font=("Arial", 12, "bold"), fg="azure4", width=10, bd=1, state="readonly", textvariable=var_total) # Crear un cuadro de entrada
texto_total.grid(row=2, column=3, sticky=W, padx= 41) # Posicionar el cuadro de entrada

# Botones
botones = ["Total", "Recibo", "Guardar", "Resetear"] # Lista de botones
botones_creados = [] # Lista de botones creados
columnas = 0 # Inicializar la variable columnas
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Arial", 14, "bold"), fg="azure4", bg="black", width=8, bd=1) # Crear un boton
    botones_creados.append(boton) # Guardar el boton en la lista de botones creados
    boton.grid(row=0, column=columnas) # Posicionar el boton
    columnas += 1 # Incrementar la variable columnas

botones_creados[0].config(command=total) # Configurar el comando del boton
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area de recibo
texto_recibo = Text(panel_recibo, font=("Arial", 12, "bold"), fg="azure4", width=43, height=10, bd=1) # Crear un area de texto
texto_recibo.grid(row=0, column=0) # Posicionar el area de texto

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=("Arial", 16, "bold"), fg="azure4", width=30, bd=1) # Crear un visor
visor_calculadora.grid(row=0, column=0, columnspan=4) # Posicionar el visor
botones_calculadora = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"] # Lista de botones
botones_guardados = [] # Lista de botones guardados
filas = 1 # Inicializar la variable filas
columnas = 0 # Inicializar la variable columnas
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=("Arial", 14, "bold"), fg="azure4", bg="black", width=8, bd=1) # Crear un boton
    boton.grid(row=filas, column=columnas) # Posicionar el boton
    columnas += 1 # Incrementar la variable columnas
    if columnas > 3: # Condición
        columnas = 0 # Reiniciar la variable columnas
        filas += 1 # Incrementar la variable filas  
        
    botones_guardados.append(boton) # Guardar el boton en la lista de botones guardados

botones_guardados[0].config(command=lambda:click_boton("7")) # Configurar el comando del boton
botones_guardados[1].config(command=lambda:click_boton("8"))
botones_guardados[2].config(command=lambda:click_boton("9"))
botones_guardados[3].config(command=lambda:click_boton("/"))
botones_guardados[4].config(command=lambda:click_boton("4"))
botones_guardados[5].config(command=lambda:click_boton("5"))
botones_guardados[6].config(command=lambda:click_boton("6"))
botones_guardados[7].config(command=lambda:click_boton("*"))
botones_guardados[8].config(command=lambda:click_boton("1"))
botones_guardados[9].config(command=lambda:click_boton("2"))
botones_guardados[10].config(command=lambda:click_boton("3"))
botones_guardados[11].config(command=lambda:click_boton("-"))
botones_guardados[12].config(command=lambda:click_boton("0"))
botones_guardados[13].config(command=lambda:click_boton("."))
botones_guardados[14].config(command=obtener_resultado)
botones_guardados[15].config(command=lambda:click_boton("+"))


# Evitar que la pantalla se cierre
aplicacion.mainloop() # Bucle infinito para que se ejecute la ventana   