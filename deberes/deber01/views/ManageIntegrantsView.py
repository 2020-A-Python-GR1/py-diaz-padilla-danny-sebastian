from tkinter import *
from tkinter import messagebox

from models.Integrant import Integrant
from models.utils import advanced_compare_of_search
from strings.Strings import Strings as s
from variables import total_integrants
from views.CreateIntegrantView import CreateIntegrantView
from views.UpdateIntegrantView import UpdateIntegrantView


class ManageIntegrantsView:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()

        self.frame.config(bg="#d5d98f")


        # ROW 0
        Label(self.frame, text=s.dictionary["text_manage_of_integrants"]).grid(row=0, column=0, columnspan=2)
        Button(self.frame, text=s.dictionary["string_create"], command=lambda: self.nav_to_create_integrant(Integrant.generateNewId())).grid(row=0, column=2)

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

        Button(self.frame, text=s.dictionary["text_update_list"], command=self.load_data).grid(row=5, column=0, columnspan=2)
        self.load_data()

        Button(self.frame, bg="orange", text=s.dictionary["string_cancel"], command=self.close_windows).grid(row=5, column=2)


    def close_windows(self):
        self.root.destroy()

    def load_data(self):
        if self.listbox.size() > 0:
            self.listbox.delete(0, END)
        for integrant in total_integrants.values():
            self.listbox.insert(END, integrant.user_name)

    def search_integrant(self, entry_search):
        found = False
        position = -1

        for i in range(self.listbox.size()):
            if advanced_compare_of_search(self.listbox.get(i), entry_search) is not None:
                found = True
                position = i
                break  # siempre la primera respuesta

        if found:
            actual_selection = self.listbox.curselection()
            if self.is_valid_selection(actual_selection):
                self.listbox.selection_clear(actual_selection[0])

            self.listbox.selection_set(position)
            messagebox.showinfo(title=s.dictionary['string_search'], message=s.dictionary['msg_search_found_and_selected'])
        else:
            messagebox.showinfo(title=s.dictionary['string_search'], message=s.dictionary['msg_search_not_found'])

    def nav_to_create_integrant(self, integrant_id):
        CreateIntegrantView(Toplevel(self.root), integrant_id)

    def nav_to_update_integrant(self, selection):
        if self.is_valid_selection(selection):
            UpdateIntegrantView(Toplevel(self.root), self.listbox.get(selection[0]))
        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])

    def delete_selection(self, selection):
        if self.is_valid_selection(selection):

            try:
                total_integrants.pop(self.listbox.get(selection[0]))
                Integrant.saveDataIntegrants(total_integrants)  # se guarda la eliminación
                self.listbox.delete(selection)
                messagebox.showinfo(title=s.dictionary['string_delete'], message=s.dictionary['msg_success_deleted'])
            except KeyError as error:
                self.load_data()
                messagebox.showinfo(title=s.dictionary['string_details'], message=s.dictionary['text_dont_forget_to_update_try_again'])



        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])

    def show_details(self, selection):
        if self.is_valid_selection(selection):

            try:
                integrant = total_integrants[self.listbox.get(selection[0])]
                messagebox.showinfo(title=s.dictionary['string_details'], message=integrant.read())

            except KeyError as error:
                self.load_data()
                messagebox.showinfo(title=s.dictionary['string_details'], message=s.dictionary['text_dont_forget_to_update_try_again'])


        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])


    @staticmethod
    def is_valid_selection(selection):
        return len(selection) > 0





