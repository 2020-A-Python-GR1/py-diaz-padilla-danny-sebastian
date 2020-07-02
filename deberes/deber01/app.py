from Parameters import Parameters  # para generar congruencia


from tkinter import *

from views.MainView import MainView



# Configuración de la interfaz gráfica
root = Tk()
root.title("Deber 03")
root.resizable(False, False)  # para no redimensionar
root.iconbitmap("fav.ico")
# root.geometry("600x400")  # tamaño

app = MainView(root)
root.mainloop()

