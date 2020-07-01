from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Parameters import Parameters
from models.Integrant import Integrant
from strings.Strings import Strings as s

from variables import total_integrants


class UpdateIntegrantView:

    def __init__(self, root, integrant_user_name=None):
        print(integrant_user_name)
        self.root = root
        self.frame = Frame(self.root)

        self.integrant = total_integrants[integrant_user_name]

        # ROW 0
        Label(self.frame, text="debug: Actualización de integrante").grid(row=0, column=0, columnspan=3)

        # ROW 1
        Label(self.frame, text="debug: ID").grid(row=1, column=0)
        Label(self.frame, text=str(self.integrant.integrant_id)).grid(row=1, column=1, columnspan=2)

        # ROW 2
        Label(self.frame, text="debug: user_name").grid(row=2, column=0)
        self.entry_user_name = StringVar(value=self.integrant.user_name)
        Entry(self.frame, textvariable=self.entry_user_name).grid(row=2, column=1, columnspan=2)

        # ROW 3
        Label(self.frame, text="debug: Fecha").grid(row=3, column=0)
        Label(self.frame, text=self.integrant.date_creation).grid(row=3, column=1, columnspan=2)

        # ROW 4
        Label(self.frame, text="debug: Estado").grid(row=4, column=0)
        self.combo_box_state = Combobox(self.frame, state="readonly")
        self.combo_box_state.grid(row=4, column=1, columnspan=2)
        self.combo_box_state["values"] = ["Debug: Conectado", "Debug: Inactivo"]
        self.combo_box_state.current(0 if self.integrant.state == Integrant.states[Parameters.key_state_connected] else 1)

        # ROW 5
        Label(self.frame, text="debug: Se le permite hablar").grid(row=5, column=0)
        self.combo_box_allowed_to_talk = Combobox(self.frame, state="readonly")
        self.combo_box_allowed_to_talk.grid(row=5, column=1, columnspan=2)
        self.combo_box_allowed_to_talk["values"] = [s.dictionary["string_yes"], s.dictionary["string_no"]]
        self.combo_box_allowed_to_talk.current(0 if self.integrant.allowed_to_talk else 1)

        Button(self.frame, text="DEBUG: Crear", command=lambda:
               self.update_integrant(self.integrant.integrant_id, self.entry_user_name.get(),
                                     Integrant.states[Parameters.key_state_connected if self.combo_box_allowed_to_talk.get() == "Debug: Conectado" else Parameters.key_state_disconnected],
                                     self.integrant.date_creation, self.combo_box_allowed_to_talk.get() == s.dictionary["string_yes"]))\
            .grid(row=6, column=1)

        Button(self.frame, text="DEBUG: Cancelar", command=self.close_windows, bd=10).grid(row=6, column=2)

        self.frame.pack()

    def update_integrant(self, integrant_id, user_name, state, today, allowed_to_talk):

        if self.valid_fields(user_name):
            if user_name not in total_integrants:
                integrant = Integrant(integrant_id, user_name, state, today, allowed_to_talk)
                total_integrants.pop(self.integrant.user_name)
                total_integrants[user_name] = integrant
                print("Actualización de integrante", self.integrant.user_name, total_integrants)
            else:
                messagebox.showinfo(title="Debug: Creación", message="Debug: Ese nombre ya existe")
        else:
            messagebox.showinfo(title="Debug: Creación", message="Debug: Campos no válidos revise nuevamente")


    @staticmethod
    def valid_fields(user_name):
        return user_name != "" and user_name is not None

    def close_windows(self):
        self.root.destroy()







