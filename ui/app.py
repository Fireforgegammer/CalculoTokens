import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk
from servicios.calculo_servicio import calcular_desde_texto
from .componentes import crear_seccion, crear_boton_estilizado
from .editor import EditorModo
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
        l_mod_t.configure(font=f_tit); l_txt_t.configure(font=f_tit); l_res_t.configure(font=f_tit)
        sel_mod.configure(font=obtener_f()); campo_texto.configure(font=obtener_f())
        b_calc.configure(font=f_bt); b_limp.configure(font=f_bt); b_salir.configure(font=f_bt)
        if es_personalizable: b_opciones.configure(font=f_bt)
        l_tok_res.configure(font=f_res); l_cos_res.configure(font=f_res)
        l_tok_res.master.configure(fg_color=color_cajas_int)
        l_cos_res.master.configure(fg_color=color_cajas_int)

    def abrir_opciones():
        top = ctk.CTkToplevel(ventana)
        top.title("Panel de Control"); top.geometry("500x620"); top.attributes("-topmost", True)
        tabview = ctk.CTkTabview(top, width=460, height=540); tabview.pack(padx=20, pady=10)
        
        tabview.add("Ajustes Visuales"); tabview.add("Colores Fondos"); tabview.add("Colores Ventanas"); tabview.add("Personalización")

        # OPCIÓN 1: AJUSTES VISUALES
        ctk.CTkLabel(tabview.tab("Ajustes Visuales"), text="Tipografía", font=("Arial", 14, "bold")).pack(pady=10)
        ctk.CTkOptionMenu(tabview.tab("Ajustes Visuales"), values=fuentes, variable=var_fuente, command=refrescar_interfaz).pack()
        ctk.CTkOptionMenu(tabview.tab("Ajustes Visuales"), values=["10", "12", "14", "16"], variable=var_tamano, command=refrescar_interfaz).pack(pady=10)

        # OPCIÓN 2: COLORES FONDOS
        def pick_color(target):
            nonlocal color_bg_app
            c = colorchooser.askcolor()[1]
            if not c: return
            if target == "bg": color_bg_app = c
            elif target == "tok": f_tok.configure(fg_color=c)
            elif target == "cos": f_cos.configure(fg_color=c)
            refrescar_interfaz()

        ctk.CTkButton(tabview.tab("Colores Fondos"), text="Color Fondo App", command=lambda: pick_color("bg")).pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Fondos"), text="Fondo Tokens", command=lambda: pick_color("tok")).pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Fondos"), text="Fondo Costes", command=lambda: pick_color("cos")).pack(pady=5)

        # OPCIÓN 3: COLORES VENTANAS
        def pick_color_int(target):
            nonlocal color_cajas_int
            c = colorchooser.askcolor()[1]
            if not c: return
            if target == "int_tok": l_tok_res.master.configure(fg_color=c)
            elif target == "int_cos": l_cos_res.master.configure(fg_color=c)
            elif target == "global": color_cajas_int = c; refrescar_interfaz()

        ctk.CTkButton(tabview.tab("Colores Ventanas"), text="Interior Tokens", command=lambda: pick_color_int("int_tok")).pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Ventanas"), text="Interior Costes", command=lambda: pick_color_int("int_cos")).pack(pady=5)
        ctk.CTkButton(tabview.tab("Colores Ventanas"), text="Interior Global", command=lambda: pick_color_int("global")).pack(pady=5)

        # OPCIÓN 4: PERSONALIZACIÓN (CAJA DE HERRAMIENTAS)
        def toggle_edit():
            top.destroy()
            for child in layout.winfo_children(): child.pack_forget()
            editor.activar()
            
            tools = ctk.CTkToplevel(ventana)
            tools.title("Herramientas"); tools.geometry("280x600"); tools.attributes("-topmost", True)
            
            widgets_dict = {
                "Etiqueta Modelo": l_mod_t, "Selector IA": sel_mod,
                "Etiqueta Texto": l_txt_t, "Caja Texto": campo_texto,
                "Fila Botones": f_btns, "Etiqueta Result": l_res_t,
                "Sección Tokens": f_tok, "Sección Costes": f_cos
            }

            for nombre, widget in widgets_dict.items():
                ctk.CTkButton(tools, text=f"Añadir {nombre}", command=lambda w=widget: [w.place(x=50, y=50), editor.hacer_movible(w)]).pack(pady=3, padx=20, fill="x")

            ctk.CTkButton(tools, text="GUARDAR Y CERRAR", fg_color="#27ae60", command=lambda: [editor.desactivar(), tools.destroy()]).pack(pady=20, padx=20, fill="x")

        ctk.CTkSegmentedButton(tabview.tab("Personalización"), values=["Light", "Dark"], command=ctk.set_appearance_mode).pack(pady=20)
        ctk.CTkButton(tabview.tab("Personalización"), text="✏ MODO DISEÑO (TOOLBOX)", command=toggle_edit, fg_color="#e67e22", height=40).pack()

    # --- WIDGETS ---
    l_mod_t = ctk.CTkLabel(layout, text="Modelo de IA")
    sel_mod = ctk.CTkComboBox(layout, values=list(PRECIOS_MODELOS.keys()), fg_color="white", height=35)
    l_txt_t = ctk.CTkLabel(layout, text="Texto a analizar")
    campo_texto = ctk.CTkTextbox(layout, height=120, border_width=1, fg_color="white")
    
    f_btns = ctk.CTkFrame(layout, fg_color="transparent")
    def calcular():
        txt = campo_texto.get("1.0", "end-1c").strip()
        if not txt: return
        r = calcular_desde_texto(txt, sel_mod.get())
        l_tok_res.configure(text=f"📥 In: {r['tokens_entrada']} | 📤 Out: {r['tokens_salida']} | 📈 Tot: {r['tokens_totales']}")
        c = r['costes']
        l_cos_res.configure(text=f"💶 €: {c['coste_total_usd']*0.92:.6f} | 💵 $: {c['coste_total_usd']:.6f}")

    b_calc = crear_boton_estilizado(f_btns, "Calcular", calcular, "#2c3e50", obtener_f(True))
    b_limp = crear_boton_estilizado(f_btns, "Limpiar", lambda: [campo_texto.delete("1.0", "end"), l_tok_res.configure(text=""), l_cos_res.configure(text="")], "#7f8c8d", obtener_f(True))
    b_salir = crear_boton_estilizado(f_btns, "Salir", ventana.destroy, "#e74c3c", obtener_f(True))
    b_calc.pack(side="left", padx=(0, 10)); b_limp.pack(side="left", padx=10); b_salir.pack(side="left", padx=10)
    
    if es_personalizable:
        b_opciones = crear_boton_estilizado(f_btns, "⚙ Opciones", abrir_opciones, "#2980b9", obtener_f(True))
        b_opciones.pack(side="left", padx=10)

    l_res_t = ctk.CTkLabel(layout, text="Resultados")
    f_tok, l_tok_res = crear_seccion(layout, "Tokens", "#d5e8d4", obtener_f(True, 1), obtener_f(False, 1))
    f_cos, l_cos_res = crear_seccion(layout, "Costes", "#dae8fc", obtener_f(True, 1), obtener_f(False, 1))

    # Montaje Inicial
    l_mod_t.pack(anchor="w", pady=2); sel_mod.pack(fill="x", pady=(0, 15))
    l_txt_t.pack(anchor="w", pady=2); campo_texto.pack(fill="x", pady=(0, 20))
    f_btns.pack(fill="x", pady=10); l_res_t.pack(anchor="w", pady=5)
    f_tok.pack(fill="x", pady=5); f_cos.pack(fill="x", pady=10)

    refrescar_interfaz()
    ventana.mainloop()