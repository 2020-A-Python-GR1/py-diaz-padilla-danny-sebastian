from tkinter import *
from tkinter import messagebox

from Parameters import Parameters
from models.utils import advanced_compare_of_search
from strings.Strings import Strings as s

from .CreateGrupalChatView import CreateGrupalChatView
from models.ChatGroup import ChatGroup
from .ManageIntegrantsView import ManageIntegrantsView
from .UpdateChatGroupView import UpdateChatGroupView

from variables import group_chats


class MainView:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()


        self.frame.config(bg="#8fb8ac")

        # ROW 0
        Label(self.frame, text=s.dictionary['text_main_window']).grid(row=0, column=0, columnspan=2)
        Button(self.frame, bg="#d5d98f", text=s.dictionary['text_manage_integrants'], command=lambda: self.nav_to_manage_integrants()).grid(row=0, column=2)


        # ROW 1
        self.entry_search = StringVar()
        Entry(self.frame, textvariable=self.entry_search).grid(row=1, column=0)
        Button(self.frame, text=s.dictionary['string_look_for'], command=lambda: self.search_group(self.entry_search.get())).grid(row=1, column=1)
        Button(self.frame, text=s.dictionary['string_create'], command=lambda: self.nav_to_create_grupal_chat(ChatGroup.generateNewId())).grid(row=1, column=2)

        # ROW 2, 3, 4
        self.listbox = Listbox(self.frame)
        self.listbox.grid(row=2, column=0, rowspan=3, columnspan=2)

        # Lateral derecho de ROW 2, 3, 4
        Button(self.frame, text=s.dictionary['string_update'], command=lambda: self.nav_to_update_group(self.listbox.curselection())).grid(row=2, column=2)
        Button(self.frame, text=s.dictionary['string_delete'], command=lambda: self.delete_selection(self.listbox.curselection())).grid(row=3, column=2)
        Button(self.frame, text=s.dictionary['string_details'], command=lambda: self.show_details(self.listbox.curselection())).grid(row=4, column=2)
        Button(self.frame, text=s.dictionary["text_update_list"], command=self.load_data, bg="#7fd2db").grid(row=5, column=0, columnspan=2)

        self.load_data()

        Label(self.frame, text=s.dictionary['string_language'], bg="#8fb8ac").grid(row=7, column=0)
        Button(self.frame, text=Parameters.language_spanish, command=self.set_spanish, bg="#81ba80").grid(row=7, column=1)
        Button(self.frame, text=Parameters.language_english, command=self.set_english, bg="#a476c4").grid(row=7, column=2)

    def set_spanish(self):
        s.changeLanguage(Parameters.language_spanish)
        self.reload()

    def set_english(self):
        s.changeLanguage(Parameters.language_english)
        self.reload()

    def reload(self):
        self.frame.destroy()
        self.__init__(self.root)

    def load_data(self):
        if self.listbox.size() > 0:
            self.listbox.delete(0, END)

        for group in group_chats.values():
            self.listbox.insert(END, group.name_group)

    def search_group(self, entry_search):
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

    def nav_to_create_grupal_chat(self, chat_id):
        CreateGrupalChatView(Toplevel(self.root), chat_id)

    def nav_to_manage_integrants(self):
        ManageIntegrantsView(Toplevel(self.root))

    def nav_to_update_group(self, selection):
        if self.is_valid_selection(selection):
            try:
                group = group_chats[self.listbox.get(selection[0])]
                UpdateChatGroupView(Toplevel(self.root), group.name_group)
            except KeyError as error:
                self.load_data()
                messagebox.showinfo(title=s.dictionary['string_details'], message=s.dictionary['text_dont_forget_to_update_try_again'])


        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])

    def delete_selection(self, selection):
        if self.is_valid_selection(selection):

            try:
                group_chats.pop(self.listbox.get(selection[0]))
                ChatGroup.saveDataChatGroups(group_chats)  # se guarda la eliminación
                self.listbox.delete(selection)
                messagebox.showinfo(title=s.dictionary['string_delete'], message=s.dictionary['msg_success_deleted'])
            except KeyError as error:
                self.load_data()
                messagebox.showinfo(title=s.dictionary['string_details'], message=s.dictionary['text_dont_forget_to_update_try_again'])

        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])

    @staticmethod
    def is_valid_selection(selection):
        return len(selection) > 0

    def show_details(self, selection):
        if self.is_valid_selection(selection):
            try:
                group = group_chats[self.listbox.get(selection[0])]
                messagebox.showinfo(title=s.dictionary['string_details'], message=group.read())
            except KeyError as error:
                self.load_data()
                messagebox.showinfo(title=s.dictionary['string_details'], message=s.dictionary['text_dont_forget_to_update_try_again'])

        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first'])









