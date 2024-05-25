import tkinter as tk
from tkinter import messagebox
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

    cliente ={
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    collection.insert_one(cliente)
    messagebox.showinfo("Cliente agregado","Cliente agregado exitosamente")

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
root.title("Gestión clientes")

# Etiquetas 
tk.Label(root, text="ID").grid(row=0, column=0)
tk.Label(root, text="Nombre").grid(row=1, column=0)
tk.Label(root, text="Apellido").grid(row=2, column=0)
tk.Label(root, text="Teléfono").grid(row=3, column=0)
#consultar
tk.Label(root, text="ID a consultar").grid(row=5, column=0)
#editar
tk.Label(root, text="ID").grid(row=7, column=0)
tk.Label(root, text="Nuevo Nombre").grid(row=8, column=0)
tk.Label(root, text="Nuevo Apellido").grid(row=9, column=0)
tk.Label(root, text="Nuevo Teléfono").grid(row=10, column=0)
#eliminar
tk.Label(root, text="ID cliente a eliminar").grid(row=12, column=0)
# Campos de entrada 
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=2, column=1)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=3, column=1)
#campo cosultar
entry_id_consulta = tk.Entry(root)
entry_id_consulta.grid(row=5, column=1)
#campo editar
entry_id_editar = tk.Entry(root)
entry_id_editar.grid(row=7, column=1)
entry_nuevo_nombre = tk.Entry(root)
entry_nuevo_nombre.grid(row=8, column=1)
entry_nuevo_apellido = tk.Entry(root)
entry_nuevo_apellido.grid(row=9, column=1)
entry_nuevo_telefono = tk.Entry(root)
entry_nuevo_telefono.grid(row=10, column=1) 
#campo eliminar
entry_id_eliminar = tk.Entry(root)
entry_id_eliminar.grid(row=12, column=1) 
# Botones
tk.Button(root, text="Agregar Cliente", command=agregar_cliente).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Buscar Cliente", command=consultar_cliente).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Actualizar Cliente", command=actualizar_cliente).grid(row=11, column=0, columnspan=2, pady=10)
tk.Button(root, text="Eliminar Cliente", command=eliminar_cliente).grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()