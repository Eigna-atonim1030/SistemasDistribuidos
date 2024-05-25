import tkinter as tk
from tkinter import messagebox, ttk
from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client.clientes
collection = db.informacion_cliente

def agregar_cliente():
    id = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()

    cliente = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    collection.insert_one(cliente)
    messagebox.showinfo("Cliente agregado", "Cliente agregado exitosamente")

def consultar_cliente():
    id_consulta = entry_id_consulta.get()
    cliente = collection.find_one({"id": id_consulta})
    if cliente:
        messagebox.showinfo("Cliente Encontrado", f"ID: {cliente['id']}\nNombre: {cliente['nombre']}\nApellido: {cliente['apellido']}\nTeléfono: {cliente['telefono']}")
    else:
        messagebox.showerror("Error", "Cliente no encontrado")

def actualizar_cliente():
    id_actualizar = entry_id_editar.get()
    nuevo_nombre = entry_nuevo_nombre.get()
    nuevo_apellido = entry_nuevo_apellido.get()
    nuevo_telefono = entry_nuevo_telefono.get()
    cliente_actualizado = {
        "nombre": nuevo_nombre,
        "apellido": nuevo_apellido,
        "telefono": nuevo_telefono
    }
    resultado = collection.update_one({"id": id_actualizar}, {"$set": cliente_actualizado})
    if resultado.modified_count:
        messagebox.showinfo("Cliente Actualizado", "Cliente actualizado exitosamente")
    else:
        messagebox.showerror("Error", "Cliente no encontrado")

def eliminar_cliente():
    id_eliminar = entry_id_eliminar.get()
    resultado = collection.delete_one({"id": id_eliminar})
    if resultado.deleted_count:
        messagebox.showinfo("Cliente Eliminado", "Cliente eliminado exitosamente")
    else:
        messagebox.showerror("Error", "Cliente no encontrado")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")
root.geometry("400x500")
root.configure(bg="#E0E0E0")

# Estilo para las etiquetas
label_style = ttk.Style()
label_style.configure("TLabel", font=("Arial", 12), background="#E0E0E0")

# Estilo para las entradas de texto
entry_style = ttk.Style()
entry_style.configure("TEntry", font=("Arial", 12))

# Estilo para los botones
button_style = ttk.Style()
button_style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white")

# Etiquetas
ttk.Label(root, text="ID", style="TLabel").grid(row=0, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Nombre", style="TLabel").grid(row=1, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Apellido", style="TLabel").grid(row=2, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Teléfono", style="TLabel").grid(row=3, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="ID a consultar", style="TLabel").grid(row=5, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="ID", style="TLabel").grid(row=7, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Nuevo Nombre", style="TLabel").grid(row=8, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Nuevo Apellido", style="TLabel").grid(row=9, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="Nuevo Teléfono", style="TLabel").grid(row=10, column=0, padx=10, pady=10, sticky="w")
ttk.Label(root, text="ID cliente a eliminar", style="TLabel").grid(row=12, column=0, padx=10, pady=10, sticky="w")

# Campos de entrada
entry_id = ttk.Entry(root, style="TEntry")
entry_id.grid(row=0, column=1, padx=10, pady=10)
entry_nombre = ttk.Entry(root, style="TEntry")
entry_nombre.grid(row=1, column=1, padx=10, pady=10)
entry_apellido = ttk.Entry(root, style="TEntry")
entry_apellido.grid(row=2, column=1, padx=10, pady=10)
entry_telefono = ttk.Entry(root, style="TEntry")
entry_telefono.grid(row=3, column=1, padx=10, pady=10)
entry_id_consulta = ttk.Entry(root, style="TEntry")
entry_id_consulta.grid(row=5, column=1, padx=10, pady=10)
entry_id_editar = ttk.Entry(root, style="TEntry")
entry_id_editar.grid(row=7, column=1, padx=10, pady=10)
entry_nuevo_nombre = ttk.Entry(root, style="TEntry")
entry_nuevo_nombre.grid(row=8, column=1, padx=10, pady=10)
entry_nuevo_apellido = ttk.Entry(root, style="TEntry")
entry_nuevo_apellido.grid(row=9, column=1, padx=10, pady=10)
entry_nuevo_telefono = ttk.Entry(root, style="TEntry")
entry_nuevo_telefono.grid(row=10, column=1, padx=10, pady=10)
entry_id_eliminar = ttk.Entry(root, style="TEntry")
entry_id_eliminar.grid(row=12, column=1, padx=10, pady=10)

# Botones
ttk.Button(root, text="Agregar Cliente", command=agregar_cliente, style="TButton").grid(row=4, column=0, columnspan=2, pady=10)
ttk.Button(root, text="Buscar Cliente", command=consultar_cliente, style="TButton").grid(row=6, column=0, columnspan=2, pady=10)
ttk.Button(root, text="Actualizar Cliente", command=actualizar_cliente, style="TButton").grid(row=11, column=0, columnspan=2, pady=10)
ttk.Button(root, text="Eliminar Cliente", command=eliminar_cliente, style="TButton").grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()
