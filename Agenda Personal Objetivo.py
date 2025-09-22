import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Instala con: pip install tkcalendar

# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=5)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)
        self.hora_entry = ttk.Entry(self.frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)
        self.desc_entry = ttk.Entry(self.frame_entrada, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, pady=5)

        # Frame para botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(pady=10)

        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    # Función para agregar evento
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")

    # Función para eliminar evento
    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmar = messagebox.askyesno("Confirmar eliminación", "¿Deseas eliminar el evento seleccionado?")
            if confirmar:
                self.tree.delete(seleccionado)
        else:
            messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()