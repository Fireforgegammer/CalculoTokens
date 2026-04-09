import tkinter as tk
import customtkinter as ctk
from servicios.calculo_servicio import calcular_desde_texto
from ui.componentes import crear_seccion, crear_boton_estilizado
from core.precios import PRECIOS_MODELOS

def iniciar_app():
    ventana = ctk.CTk()
    ventana.title("Calculadora de Costes de APIs de IA")
    ventana.geometry("650x800")
    ventana.configure(fg_color="#f5f7f9")
    ctk.set_appearance_mode("light")

    layout = ctk.CTkFrame(ventana, fg_color="transparent")
    layout.pack(fill="both", expand=True, padx=40, pady=20)

    ctk.CTkLabel(layout, text="Modelo de IA", font=("Segoe UI", 14, "bold"), text_color="#4b4b4b").pack(anchor="w")

    lista_modelos = list(PRECIOS_MODELOS.keys())
    variable_modelo = tk.StringVar(value=lista_modelos[0])
    
    selector_modelo = ctk.CTkComboBox(layout, variable=variable_modelo, values=lista_modelos, state="readonly", font=("Segoe UI", 12), fg_color="white")
    selector_modelo.pack(fill="x", pady=(5, 15))

    ctk.CTkLabel(layout, text="Texto a analizar", font=("Segoe UI", 14, "bold"), text_color="#4b4b4b").pack(anchor="w")

    campo_texto = ctk.CTkTextbox(layout, height=150, font=("Segoe UI", 12), border_width=1, border_color="black", fg_color="white", text_color="black")
    campo_texto.pack(fill="x", pady=(5, 25))

    frame_btns = ctk.CTkFrame(layout, fg_color="transparent")
    frame_btns.pack(fill="x")

    def on_calcular():
        texto = campo_texto.get("1.0", "end-1c").strip()
        if not texto: return

        res = calcular_desde_texto(texto, variable_modelo.get())
        c = res['costes']
        
        label_tokens_r.configure(
            text=f"💾 Entrada: {res['tokens_entrada']} tokens\n"
                 f"📋 Salida (estimada): {res['tokens_salida']} tokens\n"
                 f"📊 Total: {res['tokens_totales']} tokens"
        )

        label_costes_r.configure(
            text=f"💵 Euros:   {c['coste_total_usd'] * 0.92:.6f} €\n"
                 f"💵 Dólar:   {c['coste_total_usd']:.6f} $\n"
                 f"¢ Céntimos: {c['coste_total_cent']:.4f} cts"
        )

    crear_boton_estilizado(frame_btns, "Calcular Costes", on_calcular, "#2c3e50").pack(side="left", padx=(0, 15))
    
    def limpiar():
        campo_texto.delete("1.0", "end")
        label_tokens_r.configure(text="")
        label_costes_r.configure(text="")

    crear_boton_estilizado(frame_btns, "Limpiar", limpiar, "#7f8c8d").pack(side="left", padx=15)
    crear_boton_estilizado(frame_btns, "Salir", ventana.destroy, "#e74c3c").pack(side="left", padx=15)

    ctk.CTkLabel(layout, text="Resultados", font=("Segoe UI", 14, "bold"), text_color="#4b4b4b").pack(anchor="w", pady=(30, 10))

    frame_tokens = crear_seccion(layout, "◊ Tokens", "#eafaf1")
    frame_tokens.pack(fill="x", pady=5)
    label_tokens_r = ctk.CTkLabel(frame_tokens, text="", bg_color="transparent", justify="left", anchor="w", font=("Segoe UI", 11), text_color="black")
    label_tokens_r.pack(fill="x", padx=15, pady=10)

    frame_costes = crear_seccion(layout, "⊡ Costes", "#ebf5fb")
    frame_costes.pack(fill="x", pady=10)
    label_costes_r = ctk.CTkLabel(frame_costes, text="", bg_color="transparent", justify="left", anchor="w", font=("Segoe UI", 11), text_color="black")
    label_costes_r.pack(fill="x", padx=15, pady=10)

    ventana.mainloop()