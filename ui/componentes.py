import customtkinter as ctk

def crear_seccion(master, titulo, bg_color):
    frame = ctk.CTkFrame(
        master, 
        fg_color=bg_color, 
        corner_radius=15,
        border_width=1,
        border_color="#ced4da"
    )
    
    label_titulo = ctk.CTkLabel(
        frame,
        text=titulo,
        font=("Segoe UI", 13, "bold"),
        text_color="#2c3e50"
    )
    label_titulo.pack(anchor="w", padx=15, pady=(10, 5))

    return frame

def crear_boton_estilizado(master, texto, comando, color):
    return ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        fg_color=color,
        hover_color="#34495e",
        font=("Segoe UI", 12, "bold"),
        corner_radius=10,
        height=40,
        width=140
    )