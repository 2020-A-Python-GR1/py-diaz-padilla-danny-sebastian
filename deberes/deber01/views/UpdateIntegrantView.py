from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Parameters import Parameters
from models.Integrant import Integrant
from strings.Strings import Strings as s

from variables import total_integrants


class UpdateIntegrantView:

    def __init__(self, root, integrant_user_name=None):
        print("Actualizando al integrante ", integrant_user_name)
        self.root = root
        self.frame = Frame(self.root)
        self.frame.config(bg="#d5d98f")
        self.integrant_user_name = integrant_user_name

        self.integrant = total_integrants[integrant_user_name]

        # ROW 0
        Label(self.frame, text=s.dictionary['text_update_of_integrants']).grid(row=0, column=0, columnspan=3)

        # ROW 1
        Label(self.frame, text=s.dictionary['string_id']).grid(row=1, column=0)
        Label(self.frame, text=str(self.integrant.integrant_id)).grid(row=1, column=1, columnspan=2)

        # ROW 2
        Label(self.frame, text=s.dictionary['text_user_name']).grid(row=2, column=0)
        self.entry_user_name = StringVar(value=self.integrant.user_name)
        Entry(self.frame, textvariable=self.entry_user_name).grid(row=2, column=1, columnspan=2)

        # ROW 3
        Label(self.frame, text=s.dictionary['string_date']).grid(row=3, column=0)
        Label(self.frame, text=self.integrant.date_creation).grid(row=3, column=1, columnspan=2)

        # ROW 4
        Label(self.frame, text=s.dictionary['string_state']).grid(row=4, column=0)
        self.combo_box_state = Combobox(self.frame, state="readonly")
        self.combo_box_state.grid(row=4, column=1, columnspan=2)
        self.combo_box_state["values"] = [s.dictionary['string_connected'], s.dictionary['string_disconnected']]
        self.combo_box_state.current(0 if self.integrant.state == Integrant.states[Parameters.key_state_connected] else 1)

        # ROW 5
        Label(self.frame, text=s.dictionary['text_is_allowed_to_talk']).grid(row=5, column=0)
        self.combo_box_allowed_to_talk = Combobox(self.frame, state="readonly")
        self.combo_box_allowed_to_talk.grid(row=5, column=1, columnspan=2)
        self.combo_box_allowed_to_talk["values"] = [s.dictionary["string_yes"], s.dictionary["string_no"]]
        self.combo_box_allowed_to_talk.current(0 if self.integrant.allowed_to_talk else 1)

        Button(self.frame, bg="green", text=s.dictionary['string_update'], command=lambda:
               self.update_integrant(self.integrant.integrant_id, self.entry_user_name.get(),
                                     Integrant.states[Parameters.key_state_connected] if self.combo_box_allowed_to_talk.get() == s.dictionary['string_connected'] else Integrant.states[Parameters.key_state_disconnected],
                                     self.integrant.date_creation, self.combo_box_allowed_to_talk.get() == s.dictionary["string_yes"]))\
            .grid(row=6, column=1)

        Button(self.frame, bg="orange", text=s.dictionary['string_cancel'], command=self.close_windows, bd=10).grid(row=6, column=2)

        self.frame.pack()

    def update_integrant(self, integrant_id, user_name, state, today, allowed_to_talk):

        if self.valid_fields(user_name):
            integrant = Integrant(integrant_id, user_name, state, today, allowed_to_talk)
            total_integrants.pop(self.integrant.user_name)
            total_integrants[user_name] = integrant
            print("Actualización de integrante", self.integrant.user_name, total_integrants)

            Integrant.saveDataIntegrants(total_integrants)
            self.close_windows()
            messagebox.showinfo(title=s.dictionary["string_update"], message=s.dictionary["msg_success_update"])

        else:
            messagebox.showinfo(title=s.dictionary["string_update"], message=s.dictionary["msg_not_valid_fields"])


    @staticmethod
    def valid_fields(user_name):
        return user_name != "" and user_name is not None

    def close_windows(self):
        self.root.destroy()







