import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk
from servicios.calculo_servicio import calcular_desde_texto
from ui.componentes import crear_seccion, crear_boton_estilizado
from ui.editor import EditorModo
from core.precios import PRECIOS_MODELOS

def iniciar_app(es_personalizable=False):
    ventana = ctk.CTk()
    ventana.title("Calculadora de APIs")
    ventana.geometry("900x950")
    ctk.set_appearance_mode("light")

    # Variables de estado
    color_bg_app = "#ebebeb"
    fuentes = ["Segoe UI Emoji", "Arial", "Comic Sans MS", "Verdana"]
    var_fuente = tk.StringVar(value="Segoe UI Emoji")
    var_tamano = tk.StringVar(value="12")

    layout = ctk.CTkFrame(ventana, fg_color="transparent")
    layout.pack(fill="both", expand=True, padx=50, pady=20)
    
    editor = EditorModo(layout, ventana)

    def obtener_f(bold=False, offset=0):
        try: sz = int(var_tamano.get()) + offset
        except: sz = 12 + offset
        return (var_fuente.get(), sz, "bold" if bold else "normal")

    def refrescar_interfaz(*args):
        ventana.configure(fg_color=color_bg_app)
        f_bt, f_tit, f_res = obtener_f(True), obtener_f(True, 3), obtener_f(False, 1)
        
        l_mod_t.configure(font=f_tit)
        l_txt_t.configure(font=f_tit)
        l_res_t.configure(font=f_tit)
        sel_mod.configure(font=obtener_f())
        campo_texto.configure(font=obtener_f())
        b_calc.configure(font=f_bt)
        b_limp.configure(font=f_bt)
        b_salir.configure(font=f_bt)
        if es_personalizable: b_opciones.configure(font=f_bt)
        l_tok_res.configure(font=f_res)
        l_cos_res.configure(font=f_res)

    def abrir_opciones():
        top = ctk.CTkToplevel(ventana)
        top.title("Panel de Control")
        top.geometry("500x620")
        top.attributes("-topmost", True)
        top.resizable(False, False)

        tabview = ctk.CTkTabview(top, width=460, height=540)
        tabview.pack(padx=20, pady=10)

        tabview.add("Ajustes Visuales")
        tabview.add("Colores Fondos")
        tabview.add("Colores Ventanas")
        tabview.add("Personalización")

        # Pestaña 1: Tipografía
        ctk.CTkLabel(tabview.tab("Ajustes Visuales"), text="Tipografía", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkOptionMenu(tabview.tab("Ajustes Visuales"), values=fuentes, variable=var_fuente, command=refrescar_interfaz, width=200).pack(pady=5)
        ctk.CTkLabel(tabview.tab("Ajustes Visuales"), text="Tamaño", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkOptionMenu(tabview.tab("Ajustes Visuales"), values=["10", "12", "14", "16", "18"], variable=var_tamano, command=refrescar_interfaz, width=100).pack(pady=5)

        # Pestaña 2: Colores Fondos
        def pick_color(target):
            nonlocal color_bg_app
            c = colorchooser.askcolor()[1]
            if not c: return
            if target == "bg": color_bg_app = c
            elif target == "tok": f_tok.configure(fg_color=c)
            elif target == "cos": f_cos.configure(fg_color=c)
            refrescar_interfaz()

        ctk.CTkLabel(tabview.tab("Colores Fondos"), text="Fondos Globales", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkButton(tabview.tab("Colores Fondos"), text="App", command=lambda: pick_color("bg"), fg_color="#34495e").pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Fondos"), text="Tokens", command=lambda: pick_color("tok"), fg_color="#27ae60").pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Fondos"), text="Costes", command=lambda: pick_color("cos"), fg_color="#2980b9").pack(pady=5)

        # Pestaña 3: Colores Interiores
        def pick_color_int(target):
            c = colorchooser.askcolor()[1]
            if c:
                if target == "int_tok": l_tok_res.master.configure(fg_color=c)
                elif target == "int_cos": l_cos_res.master.configure(fg_color=c)

        ctk.CTkLabel(tabview.tab("Colores Ventanas"), text="Interiores", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkButton(tabview.tab("Colores Ventanas"), text="Caja Tokens", command=lambda: pick_color_int("int_tok"), fg_color="#7f8c8d").pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Ventanas"), text="Caja Costes", command=lambda: pick_color_int("int_cos"), fg_color="#7f8c8d").pack(pady=5)

        # Pestaña 4: Personalización
        ctk.CTkLabel(tabview.tab("Personalización"), text="Apariencia", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkSegmentedButton(tabview.tab("Personalización"), values=["Light", "Dark"], command=lambda m: ctk.set_appearance_mode(m)).pack(pady=5)
        
        def toggle_edit():
            top.destroy()
            editor.activar()
            msg = ctk.CTkToplevel(ventana)
            msg.geometry("250x150")
            msg.title("Editor Activo")
            msg.attributes("-topmost", True)
            ctk.CTkLabel(msg, text="L-Click: Mover\nR-Click: Tamaño", pady=15).pack()
            ctk.CTkButton(msg, text="GUARDAR", command=lambda: [editor.desactivar(), msg.destroy()], fg_color="#27ae60").pack(pady=10)
            for w in [l_mod_t, sel_mod, l_txt_t, campo_texto, f_btns, l_res_t, f_tok, f_cos]: editor.hacer_movible(w)

        ctk.CTkButton(tabview.tab("Personalización"), text="✏ MODO EDICIÓN", command=toggle_edit, fg_color="#e67e22", height=40).pack(pady=30)
        ctk.CTkButton(top, text="Cerrar", command=top.destroy).pack(pady=10)

    # Widgets Principales
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
        l_tok_res.configure(text=f"📥 Entrada: {r['tokens_entrada']}\n📤 Salida: {r['tokens_salida']}\n📈 Total: {r['tokens_totales']}")
        c = r['costes']
        l_cos_res.configure(text=f"💶 Euros: {c['coste_total_usd']*0.92:.6f} €\n💵 Dólar: {c['coste_total_usd']:.6f} $\n🪙 Cénts: {c['coste_total_cent']:.4f} cts")

    b_calc = crear_boton_estilizado(f_btns, "Calcular", calcular, "#2c3e50", obtener_f(True))
    b_calc.pack(side="left", padx=(0, 10))
    b_limp = crear_boton_estilizado(f_btns, "Limpiar", lambda: [campo_texto.delete("1.0", "end"), l_tok_res.configure(text=""), l_cos_res.configure(text="")], "#7f8c8d", obtener_f(True))
    b_limp.pack(side="left", padx=10)
    b_salir = crear_boton_estilizado(f_btns, "Salir", ventana.destroy, "#e74c3c", obtener_f(True))
    b_salir.pack(side="left", padx=10)

    if es_personalizable:
        b_opciones = crear_boton_estilizado(f_btns, "⚙ Opciones", abrir_opciones, "#2980b9", obtener_f(True))
        b_opciones.pack(side="left", padx=10)

    l_res_t = ctk.CTkLabel(layout, text="Resultados")
    l_res_t.pack(anchor="w", pady=(5, 5))

    f_tok, l_tok_res = crear_seccion(layout, "◇ Tokens", "#d5e8d4", obtener_f(True, 1), obtener_f(False, 1))
    f_tok.pack(fill="x", pady=5)
    f_cos, l_cos_res = crear_seccion(layout, "□ Costes", "#dae8fc", obtener_f(True, 1), obtener_f(False, 1))
    f_cos.pack(fill="x", pady=10)

    refrescar_interfaz()
    ventana.mainloop()