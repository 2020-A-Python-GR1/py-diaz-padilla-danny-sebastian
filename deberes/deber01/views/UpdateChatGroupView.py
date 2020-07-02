from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from models.ChatGroup import ChatGroup
from models.Integrant import Integrant
from strings.Strings import Strings as s

from variables import group_chats, total_integrants
from views.CreateIntegrantView import CreateIntegrantView


class UpdateChatGroupView:

    def __init__(self, root, group_name=None):
        print(group_name)
        self.root = root
        self.frame = Frame(self.root)
        self.frame.config(bg="#8fb8ac")

        self.group = group_chats[group_name]

        # ROW 0
        Label(self.frame, text=s.dictionary['text_update_of_chat']).grid(row=0, column=0, columnspan=6)

        # ROW 1
        Label(self.frame, text=s.dictionary['text_actual_integrants']).grid(row=1, column=3)
        Label(self.frame, text=s.dictionary['text_rest_of_integrants']).grid(row=1, column=5)

        # ROW 2
        Label(self.frame, text=s.dictionary['string_id']).grid(row=2, column=0)
        Label(self.frame, text=str(self.group.chat_id)).grid(row=2, column=1, columnspan=2)
        self.listbox_actual_integrants = Listbox(self.frame)
        self.listbox_actual_integrants.grid(row=2, column=3, rowspan=5)
        self.listbox_total_integrants = Listbox(self.frame)
        self.listbox_total_integrants.grid(row=2, column=5, rowspan=5)

        for integrant in self.group.integrants:
            self.listbox_actual_integrants.insert(END, integrant.user_name)

        for integrant in total_integrants.values():
            if integrant not in self.group.integrants:
                self.listbox_total_integrants.insert(END, integrant.user_name)

        # ROW 3
        Label(self.frame, text=s.dictionary['text_group_name']).grid(row=3, column=0)
        self.entry_group_name = StringVar(value=self.group.name_group)
        Entry(self.frame, textvariable=self.entry_group_name).grid(row=3, column=1, columnspan=2)
        Button(self.frame, text="<-", command=lambda: self.transfer_new_integrant(self.listbox_total_integrants.curselection())).grid(row=3, column=4)

        # ROW 4
        Label(self.frame, text=s.dictionary['text_maximun_capacity']).grid(row=4, column=0)
        self.entry_maximun_capacity = StringVar(value=str(self.group.capacity_maximun))
        Entry(self.frame, textvariable=self.entry_maximun_capacity).grid(row=4, column=1, columnspan=2)
        Button(self.frame, text="->", command=lambda: self.transfer_actual_integrant(self.listbox_actual_integrants.curselection())).grid(row=4, column=4)

        # ROW 5
        Label(self.frame, text=s.dictionary['text_date_creation']).grid(row=5, column=0)
        Label(self.frame, text=self.group.date_creation).grid(row=5, column=1, columnspan=2)

        # ROW 6
        Label(self.frame, text=s.dictionary['string_active']).grid(row=6, column=0)
        self.combo_box_state = Combobox(self.frame, state="readonly")
        self.combo_box_state.grid(row=6, column=1, columnspan=2)
        self.combo_box_state["values"] = [s.dictionary['string_active'], s.dictionary['string_inactive']]  # solo True o False
        self.combo_box_state.current(0 if self.group.active else 1)

        # ROW 7
        Button(self.frame, bg="green", text=s.dictionary['string_update'], command=lambda:
               self.update_group_chat(self.group.chat_id, self.entry_group_name.get(), self.entry_maximun_capacity.get(),
                                      self.group.date_creation, self.combo_box_state.get() == "Activo"))\
            .grid(row=7, column=1)

        Button(self.frame, bg="orange", text=s.dictionary['string_cancel'], command=self.close_windows).grid(row=7, column=2)
        # Button(self.frame, text=s.dictionary['text_create_integrant'], command=lambda: self.nav_create_integrant(Integrant.generateNewId()), bd=10).grid(row=7, column=5)

        self.frame.pack()

    def close_windows(self):
        self.root.destroy()

    def nav_create_integrant(self, integrant_id):
        CreateIntegrantView(Toplevel(self.root), integrant_id)

    def transfer_actual_integrant(self, selection):

        if self.is_valid_selection(selection):

            self.listbox_total_integrants.insert(END, self.listbox_actual_integrants.get(selection[0]))
            self.listbox_actual_integrants.delete(selection[0])
        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first_from_actual'])

    def transfer_new_integrant(self, selection):

        if self.is_valid_selection(selection):
            self.listbox_actual_integrants.insert(END, self.listbox_total_integrants.get(selection[0]))
            self.listbox_total_integrants.delete(selection[0])
        else:
            messagebox.showinfo(title=s.dictionary['string_selection'], message=s.dictionary['msg_should_select_something_first_from_rest'])

    def update_group_chat(self, chat_id, entry_group_name, maximun_capacity, today, active):

        if self.valid_fields(entry_group_name, maximun_capacity):
            chat_group = ChatGroup(chat_id, entry_group_name, int(maximun_capacity), today, active)

            print("Tamaño inicial de los integrantes a establecer", len(chat_group.integrants))

            for i in range(self.listbox_actual_integrants.size()):
                print("Integrante", total_integrants[self.listbox_actual_integrants.get(i)], "Agregado")
                chat_group.integrants.append(total_integrants[self.listbox_actual_integrants.get(i)])

            group_chats.pop(self.group.name_group)
            group_chats[entry_group_name] = chat_group
            print("Actualización de grupo, nombre anterior y grupo total", self.group.name_group, group_chats)
            ChatGroup.saveDataChatGroups(group_chats)
            self.close_windows()
            messagebox.showinfo(title=s.dictionary["string_update"], message=s.dictionary["msg_success_update"])

        else:
            messagebox.showinfo(title=s.dictionary["string_update"], message=s.dictionary["msg_not_valid_fields"])

    @staticmethod
    def valid_fields(entry_group_name, maximun_capacity):
        try:
            int(maximun_capacity)
            return entry_group_name != "" and entry_group_name is not None
        except ValueError:
            return False

    @staticmethod
    def is_valid_selection(selection):
        return len(selection) > 0






