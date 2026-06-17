import customtkinter as ctk
from tkinter import messagebox

# =========================
# Funções
# =========================
def salvar():
    print("testando")

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11

# =========================
# Janela
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cadastro de Usuários")
app.geometry("500x420")
app.resizable(False, False)

# Título
titulo = ctk.CTkLabel(
    app,
    text="Cadastro de Usuário",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

# Nome
label_nome = ctk.CTkLabel(app, text="Nome")
label_nome.pack(anchor="w", padx=40)

entry_nome = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Digite seu nome"
)
entry_nome.pack(pady=8)

# Senha
label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(anchor="w", padx=40)

entry_senha = ctk.CTkEntry(
    app,
    width=400,
    show="*",
    placeholder_text="Digite sua senha"
)
entry_senha.pack(pady=8)

# CPF
label_cpf = ctk.CTkLabel(app, text="CPF")
label_cpf.pack(anchor="w", padx=40)

entry_cpf = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="000.000.000-00"
)
entry_cpf.pack(pady=8)

# Botão
btn_salvar = ctk.CTkButton(
    app,
    text="Cadastrar",
    width=250,
    height=40,
    command=salvar
)
btn_salvar.pack(pady=30)

app.mainloop()
