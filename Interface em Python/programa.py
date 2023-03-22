'''
Programa teste para criar interfaces para executar programas em python

Obs:
--- Executar comando no PowerShell como adm para ativar ambiente no Pycharm
Set-ExecutionPolicy Unrestricted -Force

--- Comando para gerar .exe
pyinstaller --noconsole  nomeDoPrograma.py
'''


from tkinter import *

def exemplo():
    textoMudar["text"] = "Alterou!"

janela = Tk()

janela.geometry("300x200")
janela.title("Título")
texto = Label(janela, text="Texto exemplo")
texto.grid(column=1, row=1, padx=10, pady=10)

botao = Button(janela, text="Executar", command=exemplo)
botao.grid(column=1, row=2, padx=10, pady=10)

textoMudar = Label(janela, text="")
textoMudar.grid(column=1, row=3, padx=10, pady=10)

janela.mainloop()

