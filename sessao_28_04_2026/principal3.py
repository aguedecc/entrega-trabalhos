import tkinter

raiz = tkinter.Tk()

# criar o botao
def escreve():
    print("escreve")

def testar():
    print("testar")

botao0 = tkinter.Button(text="0", command=escreve)
botao1 = tkinter.Button(text="1", command=testar)
botao2 = tkinter.Button(text="2")
botao3 = tkinter.Button(text="3")
botao4 = tkinter.Button(text="4")
botao5 = tkinter.Button(text="5")
botao6 = tkinter.Button(text="6")
botao7 = tkinter.Button(text="7")
botao8 = tkinter.Button(text="8")
botao9 = tkinter.Button(text="9")

# envia-lo par o interface
botao0.pack()
botao1.pack()
botao2.pack()
botao3.pack()
botao4.pack()
botao5.pack()
botao6.pack()
botao7.pack()
botao8.pack()
botao9.pack()

# arrancar com o interface
raiz.mainloop()