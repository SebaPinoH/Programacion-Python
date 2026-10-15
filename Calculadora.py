#Primera version de la calculadora

import tkinter as tk

def obtener_numeros():
    """Función auxiliar para validar e ingresar los dos valores."""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        return a, b
    except ValueError:
        lbl_resultado.config(text="Por favor, ingresa Solo Numeros")
        return None, None

def sumar():
    a, b = obtener_numeros()
    if a is not None and b is not None:
        lbl_resultado.config(text=f"Resultado: {a + b}")

def restar():
    a, b = obtener_numeros()
    if a is not None and b is not None:
        lbl_resultado.config(text=f"Resultado: {a - b}")

def multiplicar():
    a, b = obtener_numeros()
    if a is not None and b is not None:
        lbl_resultado.config(text=f"Resultado: {a * b}")

def dividir():
    a, b = obtener_numeros()
    if a is not None and b is not None:
        if b == 0:
            lbl_resultado.config(text="No se puede dividir por cero")
        else:
            lbl_resultado.config(text=f"Resultado: {a / b}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Operaciones")
ventana.geometry("340x260")
ventana.resizable(False, False)

# Primer número
lbl_a = tk.Label(ventana, text="Primero Numero:")
lbl_a.pack(pady=(15, 2))
entry_a = tk.Entry(ventana, justify="center")
entry_a.pack(pady=2)

# Segundo número
lbl_b = tk.Label(ventana, text="Segundo Numero:")
lbl_b.pack(pady=(10, 2))
entry_b = tk.Entry(ventana, justify="center")
entry_b.pack(pady=2)

# Contenedor para los botones alineados horizontalmente
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

btn_sumar = tk.Button(frame_botones, text="+", width=4, command=sumar)
btn_sumar.pack(side="left", padx=3)

btn_restar = tk.Button(frame_botones, text="-", width=4, command=restar)
btn_restar.pack(side="left", padx=3)

btn_multiplicar = tk.Button(frame_botones, text="×", width=4, command=multiplicar)
btn_multiplicar.pack(side="left", padx=3)

btn_dividir = tk.Button(frame_botones, text="÷", width=4, command=dividir)
btn_dividir.pack(side="left", padx=3)

# Etiqueta de resultado
lbl_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 11, "bold"))
lbl_resultado.pack(pady=5)

ventana.mainloop()