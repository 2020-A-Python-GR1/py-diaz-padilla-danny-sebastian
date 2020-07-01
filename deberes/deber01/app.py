from Parameters import Parameters  # para generar congruencia

from strings.Strings import Strings as s
from tkinter import *

from views.MainView import MainView

# Asegurarse primero que el diccionario a utilizar tenga todos las claves necesarias
s.changeLanguage(Parameters.language_spanish)

# Configuración de la interfaz gráfica
root = Tk()
root.title("DEBUG: Deber 03")
root.resizable(False, False)  # para no redimensionar
root.iconbitmap("fav.ico")
root.geometry("600x400")  # tamaño

app = MainView(root)
root.mainloop()

