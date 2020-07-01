from tkinter import *

root = Tk()
root.title("DEBUG: Deber 03")
root.resizable(False, False)  # para no redimensionar
# raiz.iconbitmap("imagen.ico")
root.geometry("650x350")  # tamaño
root.config(bg="blue")
# root.config(bd=35, relief="groove")  # documentacion
root.config(cursor="hand2")

top_frame = Frame(root)
top_frame.pack()
# top_frame.pack(fill="y", expand="True")  # side = right opcional, anclado, anchor
top_frame.config(bg="red", width="300", height="200")
# borde
top_frame.config(bd=35, relief="groove")  # documentacion
top_frame.config(cursor="pirate")

bottom_frame = Frame(root)
bottom_frame.pack(side="bottom")
bottom_frame.config(bg="black", width="300", height="200")


# en comand se le manda la función
def tomar_datos(event):
    print(event)
    print("Entry 1", entry1_text)


def btn_click(item):
    print(item)


boton_1 = Button(top_frame, text="Boton 1")  # command=lambda: print("Touch")
boton_1.bind("<Button-1>", tomar_datos)
boton_1.pack()

entry1_text = StringVar()
Label(bottom_frame, text="label1").grid(row=0)

input_frame = Frame(root, width=312, height=50)
input_frame.pack()

input_field1 = Entry(input_frame, font=('arial', 10, 'bold'), textvariable=entry1_text, width=50, bg="#000", bd=1)
input_field1.grid(row=0, column=0)
# input_field1.pack(ipady=10)

Label(bottom_frame, text="label2").grid(row=1)
Entry(bottom_frame).grid(row=1, column=1)

Checkbutton(bottom_frame, text="check").grid(columnspan=2)

btn_frame = Frame(bottom_frame, width=312, height=272.5, bg="grey")
# btn_frame.pack()

btn_test = Button(btn_frame, text="test", fg="black", width=100, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("test") )
# btn_test.pack()

root.mainloop()




"""
input_frame = Frame(frame)
input_frame.pack()
input_frame.config(bg="green", bd=5)
input_frame.config(cursor="pirate")

entry1_text = StringVar()
Label(input_frame, text="label1").grid(row=0, column=0)

input_field1 = Entry(input_frame, font=('arial', 10, 'bold'), textvariable=entry1_text, bg="#fff", bd=1)
input_field1.grid(row=0, column=1)

"""
