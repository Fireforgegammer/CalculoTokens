import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk
from servicios.calculo_servicio import calcular_desde_texto
from ui.componentes import crear_seccion, crear_boton_estilizado
from core.precios import PRECIOS_MODELOS

def iniciar_app(es_personalizable=False):
    ventana = ctk.CTk()
    ventana.title("Calculadora de APIs")
    ventana.geometry("900x950")
    ctk.set_appearance_mode("light")

    color_bg_app = "#ebebeb"
    color_cajas_int = "#ffffff"
    fuentes = ["Segoe UI Emoji", "Arial", "Comic Sans MS", "Verdana"]

    var_fuente = tk.StringVar(value="Segoe UI Emoji")
    var_tamano = tk.StringVar(value="12")

    def obtener_f(bold=False, offset=0):
        try:
            sz = int(var_tamano.get()) + offset
        except:
            sz = 12 + offset
        return (var_fuente.get(), sz, "bold" if bold else "normal")

    def refrescar_interfaz(*args):
        ventana.configure(fg_color=color_bg_app)
        f_bt = obtener_f(True)
        f_tit = obtener_f(True, 3)
        f_res = obtener_f(False, 1)

        l_mod_t.configure(font=f_tit)
        l_txt_t.configure(font=f_tit)
        l_res_t.configure(font=f_tit)
        sel_mod.configure(font=obtener_f())
        campo_texto.configure(font=obtener_f())
        b_calc.configure(font=f_bt)
        b_limp.configure(font=f_bt)
        b_salir.configure(font=f_bt)

        l_tok_res.configure(font=f_res)
        l_cos_res.configure(font=f_res)
        l_tok_res.master.configure(fg_color=color_cajas_int)
        l_cos_res.master.configure(fg_color=color_cajas_int)

    if es_personalizable:
        f_ajustes = ctk.CTkFrame(ventana, fg_color="white", corner_radius=10)
        f_ajustes.pack(fill="x", padx=50, pady=(10, 0), ipady=5)
        
        def pick_color(target):
            nonlocal color_bg_app, color_cajas_int
            c = colorchooser.askcolor()[1]
            if c:
                if target == "bg": color_bg_app = c
                else: color_cajas_int = c
                refrescar_interfaz()

        ctk.CTkLabel(f_ajustes, text="F:").pack(side="left", padx=5)
        ctk.CTkOptionMenu(f_ajustes, values=fuentes, variable=var_fuente, command=refrescar_interfaz, width=110).pack(side="left")
        ctk.CTkLabel(f_ajustes, text="T:").pack(side="left", padx=5)
        ctk.CTkOptionMenu(f_ajustes, values=["10", "12", "14", "16"], variable=var_tamano, command=refrescar_interfaz, width=60).pack(side="left")
        ctk.CTkButton(f_ajustes, text="Pintar Fondo", command=lambda: pick_color("bg"), width=80).pack(side="left", padx=5)
        ctk.CTkButton(f_ajustes, text="Pintar Interior", command=lambda: pick_color("int"), width=80).pack(side="left", padx=5)

    layout = ctk.CTkFrame(ventana, fg_color="transparent")
    layout.pack(fill="both", expand=True, padx=50, pady=20)

    l_mod_t = ctk.CTkLabel(layout, text="Modelo de IA")
    l_mod_t.pack(anchor="w", pady=(5, 2))
    sel_mod = ctk.CTkComboBox(layout, values=list(PRECIOS_MODELOS.keys()), fg_color="white", corner_radius=10, height=35)
    sel_mod.pack(fill="x", pady=(0, 15))

    l_txt_t = ctk.CTkLabel(layout, text="Texto a analizar")
    l_txt_t.pack(anchor="w", pady=(5, 2))
    campo_texto = ctk.CTkTextbox(layout, height=120, border_width=1, border_color="#ced4da", fg_color="white", corner_radius=10)
    campo_texto.pack(fill="x", pady=(0, 25))

    f_btns = ctk.CTkFrame(layout, fg_color="transparent")
    f_btns.pack(fill="x", pady=(0, 25))

    def calcular():
        txt = campo_texto.get("1.0", "end-1c").strip()
        if not txt: return
        r = calcular_desde_texto(txt, sel_mod.get())
        
        l_tok_res.configure(text=(
            f"\U0001F4E5 Entrada: {r['tokens_entrada']} tokens\n"
            f"\U0001F4E4 Salida: {r['tokens_salida']} tokens\n"
            f"\U0001F4C8 Total: {r['tokens_totales']} tokens"
        ))
        
        c = r['costes']
        l_cos_res.configure(text=(
            f"\U0001F4B6 Euros: {c['coste_total_usd']*0.92:.6f} \u20AC\n"
            f"\U0001F4B5 Dólar: {c['coste_total_usd']:.6f} $\n"
            f"\U0001FA99 Céntimos: {c['coste_total_cent']:.4f} cts"
        ))

    b_calc = crear_boton_estilizado(f_btns, "Calcular", calcular, "#2c3e50", obtener_f(True))
    b_calc.pack(side="left", padx=(0, 10))
    b_limp = crear_boton_estilizado(f_btns, "Limpiar", lambda: [campo_texto.delete("1.0", "end"), l_tok_res.configure(text=""), l_cos_res.configure(text="")], "#7f8c8d", obtener_f(True))
    b_limp.pack(side="left", padx=10)
    b_salir = crear_boton_estilizado(f_btns, "Salir", ventana.destroy, "#e74c3c", obtener_f(True))
    b_salir.pack(side="left", padx=10)

    l_res_t = ctk.CTkLabel(layout, text="Resultados")
    l_res_t.pack(anchor="w", pady=(5, 5))

    f_tok, l_tok_res = crear_seccion(layout, "\u25CA Tokens", "#d5e8d4", obtener_f(True, 1), obtener_f(False, 1), color_cajas_int)
    f_tok.pack(fill="x", pady=5)

    f_cos, l_cos_res = crear_seccion(layout, "\u22A1 Costes", "#dae8fc", obtener_f(True, 1), obtener_f(False, 1), color_cajas_int)
    f_cos.pack(fill="x", pady=10)

    refrescar_interfaz()
    ventana.mainloop()