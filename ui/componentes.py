import customtkinter as ctk

def crear_seccion(master, titulo, color_fondo, fuente_tit, fuente_res):
    frame_fondo = ctk.CTkFrame(master, fg_color=color_fondo, corner_radius=15)
    
    label_titulo = ctk.CTkLabel(frame_fondo, text=titulo, font=fuente_tit, text_color="#2c3e50")
    label_titulo.pack(anchor="w", padx=20, pady=(10, 5))
    
    frame_interior = ctk.CTkFrame(frame_fondo, fg_color="white", corner_radius=10)
    frame_interior.pack(fill="both", expand=True, padx=10, pady=(0, 10))
    
    label_resultado = ctk.CTkLabel(frame_interior, text="", font=fuente_res, justify="left", anchor="w", text_color="black")
    label_resultado.pack(fill="x", padx=15, pady=15)

    return frame_fondo, label_resultado

def crear_boton_estilizado(master, texto, comando, color, fuente):
    return ctk.CTkButton(
        master, text=texto, command=comando, fg_color=color,
        hover_color="#34495e", font=fuente, corner_radius=12,
        height=42, width=150
    )