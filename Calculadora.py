#Primera version de la calculadora

import tkinter as tk

def al_presionar_boton(valor):
    """Agrega el texto del botón presionado al display."""
    expresion_actual = display.get()
    display.delete(0, tk.END)
    display.insert(0, expresion_actual + str(valor))

def limpiar_pantalla():
    """Borra todo el contenido del display."""
    display.delete(0, tk.END)

def borrar_ultimo():
    """Borra el último carácter ingresado."""
    expresion_actual = display.get()
    display.delete(0, tk.END)
    display.insert(0, expresion_actual[:-1])

def calcular_resultado():
    """Evalúa la expresión matemática ingresada."""
    try:
        expresion = display.get()
        # Reemplazamos los símbolos visuales por los operadores de Python
        expresion_eval = expresion.replace("×", "*").replace("÷", "/")
        resultado = eval(expresion_eval)
        
        display.delete(0, tk.END)
        # Si el resultado es un entero exacto (ej. 5.0), lo mostramos como entero (5)
        if isinstance(resultado, float) and resultado.is_integer():
            display.insert(0, str(int(resultado)))
        else:
            display.insert(0, str(resultado))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Div por 0")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x380")
ventana.resizable(False, False)

# --- DISPLAY / PANTALLA ---
display = tk.Entry(
    ventana, 
    font=("Arial", 20, "bold"), 
    justify="right", 
    bd=10, 
    relief=tk.FLAT
)
display.pack(fill="x", padx=15, pady=15)

# --- CONTENEDOR DE BOTONES (GRID) ---
frame_botones = tk.Frame(ventana)
frame_botones.pack(expand=True, fill="both", padx=10, pady=(0, 10))

# Configurar peso de filas y columnas para que se distribuyan uniformemente
for i in range(5):
    frame_botones.rowconfigure(i, weight=1)
for j in range(4):
    frame_botones.columnconfigure(j, weight=1)

# Distribución de la botonera: (Texto, Fila, Columna)
botones = [
    ('C', 0, 0), ('←', 0, 1), ('÷', 0, 2), ('×', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3),
    ('0', 4, 0), ('.', 4, 2)
]

# Creación dinámica de botones
for texto, fila, columna in botones:
    if texto == 'C':
        cmd = limpiar_pantalla
    elif texto == '←':
        cmd = borrar_ultimo
    elif texto == '=':
        cmd = calcular_resultado
    else:
        # lambda t=texto asegura que pase el valor correcto de cada botón
        cmd = lambda t=texto: al_presionar_boton(t)

    # El '0' abarca 2 columnas (columnspan=2)
    colspan = 2 if texto == '0' else 1
    # El '=' abarca 2 filas (rowspan=2)
    rowspan = 2 if texto == '=' else 1

    btn = tk.Button(
        frame_botones, 
        text=texto, 
        font=("Arial", 14, "bold"),
        command=cmd
    )
    btn.grid(row=fila, column=columna, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=2, pady=2)

ventana.mainloop()