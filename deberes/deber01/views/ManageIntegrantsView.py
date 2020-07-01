from tkinter import *
from tkinter import messagebox

from models.Integrant import Integrant
from strings.Strings import Strings as s
from variables import total_integrants
from views.CreateIntegrantView import CreateIntegrantView
from views.UpdateIntegrantView import UpdateIntegrantView


class ManageIntegrantsView:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()
        # ROW 0
        Label(self.frame, text="Debug: Crear un integrante").grid(row=0, column=0, columnspan=2)
        Button(self.frame, text="Debug: Crear", command=lambda: self.nav_to_create_integrant(Integrant.generateNewId())).grid(row=0, column=2)

        # ROW 1
        self.entry_search = StringVar()
        Entry(self.frame, textvariable=self.entry_search).grid(row=1, column=0)
        Button(self.frame, text=s.dictionary['string_search'], command=lambda: self.search_integrant(self.entry_search.get())).grid(row=1, column=1)

        # ROW 2, 3, 4
        self.listbox = Listbox(self.frame)
        self.listbox.grid(row=2, column=0, rowspan=3, columnspan=2)

        # Lateral derecho de ROW 2, 3, 4
        Button(self.frame, text=s.dictionary['string_update'], command=lambda: self.nav_to_update_integrant(self.listbox.curselection())).grid(row=2, column=2)
        Button(self.frame, text=s.dictionary['string_delete'], command=lambda: self.delete_selection(self.listbox.curselection())).grid(row=3, column=2)
        Button(self.frame, text=s.dictionary['string_details'], command=lambda: self.show_details(self.listbox.curselection())).grid(row=4, column=2)

        Button(self.frame, text="Debug: Mostrar todo", command=self.load_data).grid(row=5, column=0, columnspan=2)
        self.load_data()

    def load_data(self):
        if self.listbox.size() > 0:
            self.listbox.delete(0, END)
        for integrant in total_integrants.values():
            self.listbox.insert(END, integrant.user_name)

    def search_integrant(self, entry_search):
        found = False
        position = -1

        for i in range(self.listbox.size()):
            if self.listbox.get(i).lower() == entry_search:
                found = True
                position = i

        if found:
            self.listbox.selection_set(position)
            messagebox.showinfo(title="Debug: Busqueda", message="Debug: Encontrado y seleccionado")
        else:
            messagebox.showinfo(title="Debug: Busqueda", message="Debug: No hay busqueda")

    def nav_to_create_integrant(self, integrant_id):
        CreateIntegrantView(Toplevel(self.root), integrant_id)

    def nav_to_update_integrant(self, selection):
        if self.is_valid_selection(selection):
            UpdateIntegrantView(Toplevel(self.root), self.listbox.get(selection[0]))
        else:
            messagebox.showinfo(title="Debug: Busqueda", message="Debug: Debe seleccionar un grupo antes")

    def delete_selection(self, selection):
        if self.is_valid_selection(selection):
            messagebox.showinfo(title="Debug: Eliminación", message="Debug: Eliminado")
            self.listbox.delete(selection)
        else:
            messagebox.showinfo(title="Debug: Eliminación", message="Debug: Debe seleccionar un grupo antes")

    def show_details(self, selection):
        print(selection)

    @staticmethod
    def is_valid_selection(selection):
        return len(selection) > 0





