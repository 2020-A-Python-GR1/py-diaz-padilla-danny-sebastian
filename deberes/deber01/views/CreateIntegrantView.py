from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Parameters import Parameters
from models.Integrant import Integrant
from strings.Strings import Strings as s

from variables import total_integrants


class CreateIntegrantView:

    def __init__(self, root, integrant_id=None):
        print(integrant_id)
        self.root = root
        self.frame = Frame(self.root)

        # ROW 0
        Label(self.frame, text="debug: Creación de un nuevo integrante").grid(row=0, column=0, columnspan=3)

        # ROW 1
        Label(self.frame, text="debug: ID").grid(row=1, column=0)
        Label(self.frame, text=str(integrant_id)).grid(row=1, column=1, columnspan=2)

        # ROW 2
        Label(self.frame, text="debug: user_name").grid(row=2, column=0)
        self.entry_user_name = StringVar()
        Entry(self.frame, textvariable=self.entry_user_name).grid(row=2, column=1, columnspan=2)

        # ROW 3
        Label(self.frame, text="debug: Fecha").grid(row=3, column=0)
        today = str(datetime.today()).split()[0]
        Label(self.frame, text=today).grid(row=3, column=1, columnspan=2)

        # ROW 4
        Label(self.frame, text="debug: Estado").grid(row=4, column=0)
        self.combo_box_state = Combobox(self.frame, state="readonly")
        self.combo_box_state.grid(row=4, column=1, columnspan=2)
        self.combo_box_state["values"] = ["Debug: Conectado", "Debug: Inactivo"]
        self.combo_box_state.current(1)

        # ROW 5
        Label(self.frame, text="debug: Se le permite hablar").grid(row=5, column=0)
        self.combo_box_allowed_to_talk = Combobox(self.frame, state="readonly")
        self.combo_box_allowed_to_talk.grid(row=5, column=1, columnspan=2)
        self.combo_box_allowed_to_talk["values"] = [s.dictionary["string_yes"], s.dictionary["string_no"]]
        self.combo_box_allowed_to_talk.current(0)

        Button(self.frame, text="DEBUG: Actualizar", command=lambda:
               self.create_new_integrant(integrant_id, self.entry_user_name.get(),
                                         Integrant.states[Parameters.key_state_connected if self.combo_box_allowed_to_talk.get() == "Debug: Conectado" else Parameters.key_state_disconnected],
                                         today, self.combo_box_allowed_to_talk.get() == s.dictionary["string_yes"]))\
            .grid(row=6, column=1)

        Button(self.frame, text="DEBUG: Cancelar", command=self.close_windows, bd=10).grid(row=6, column=2)

        self.frame.pack()

    def create_new_integrant(self, integrant_id, user_name, state, today, allowed_to_talk):

        if self.valid_fields(user_name):
            if user_name not in total_integrants:
                integrant = Integrant(integrant_id, user_name, state, today, allowed_to_talk)

                total_integrants[user_name] = integrant
                print("Creación de integrante", integrant, total_integrants)
            else:
                messagebox.showinfo(title="Debug: Creación", message="Debug: Ese nombre ya existe")
        else:
            messagebox.showinfo(title="Debug: Creación", message="Debug: Campos no válidos revise nuevamente")


    @staticmethod
    def valid_fields(user_name):
        return user_name != "" and user_name is not None


    def close_windows(self):
        self.root.destroy()






