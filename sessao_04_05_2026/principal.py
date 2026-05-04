import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def criar_portefolio():
    # Configuração da Janela Principal
    janela = tk.Tk()
    janela.title("O Meu Portefólio")
    janela.geometry("400x550")
    janela.configure(bg="#f0f0f0")

    # --- FOTO DE PERFIL ---
    try:
        # Tenta carregar a imagem (substitui 'foto.png' pelo nome do teu ficheiro)
        img = Image.open("IMG_3477.jpg")
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(img)
        
        lbl_foto = tk.Label(janela, image=foto, bg="#f0f0f0")
        lbl_foto.image = foto # Manter referência
        lbl_foto.pack(pady=20)
    except:
        tk.Label(janela, text="[Imagem não encontrada]", bg="#f0f0f0").pack(pady=20)

    # --- INFORMAÇÕES PESSOAIS ---
    nome = tk.Label(janela, text="Paulo Ricardo Miranda Gomes", font=("Arial", 18, "bold"), bg="#f0f0f0")
    nome.pack()

    profissao = tk.Label(janela, text="Motorista de Pesados", font=("Arial", 12), fg="gray", bg="#f0f0f0")
    profissao.pack(pady=5)

    # Separador
    ttk.Separator(janela, orient='horizontal').pack(fill='x', padx=50, pady=15)

    # Detalhes
    detalhes = [
        ("Email:", "aguedecc@hotmail.com"),
        ("LinkedIn:", ":ricardomirand//linkedin.com"),
        ("GitHub:", "://github.com"),
        ("Bio:", "Entusiasta de tecnologia e automação.")
    ]

    for rotulo, texto in detalhes:
        frame = tk.Frame(janela, bg="#f0f0f0")
        frame.pack(fill='x', padx=50, pady=2)
        
        tk.Label(frame, text=rotulo, font=("Arial", 10, "bold"), bg="#f0f0f0").pack(side="left")
        tk.Label(frame, text=f" {texto}", font=("Arial", 10), bg="#f0f0f0").pack(side="left")

    # Botão de Sair
    btn_sair = tk.Button(janela, text="Fechar", command=janela.quit, bg="#d9534f", fg="white")
    btn_sair.pack(pady=30)

    janela.mainloop()

if __name__ == "__main__":
    criar_portefolio()