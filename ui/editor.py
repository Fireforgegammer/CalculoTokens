import customtkinter as ctk

class EditorModo:
    def __init__(self, layout, ventana):
        self.layout = layout
        self.ventana = ventana
        self.activo = False
        self.drag_data = {"widget": None, "x": 0, "y": 0}

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False
        self._set_estado_interactivo(self.layout, "normal")

    def hacer_movible(self, widget):
        self._aplicar_escudo_total(widget, widget)

    def _set_estado_interactivo(self, w, state):
        if isinstance(w, (ctk.CTkButton, ctk.CTkComboBox, ctk.CTkOptionMenu, ctk.CTkEntry, ctk.CTkTextbox)):
            try:
                w.configure(state=state)
            except:
                pass
        for hijo in w.winfo_children():
            self._set_estado_interactivo(hijo, state)

    def _aplicar_escudo_total(self, target, padre):
        if isinstance(target, (ctk.CTkButton, ctk.CTkComboBox, ctk.CTkOptionMenu, ctk.CTkEntry, ctk.CTkTextbox)):
            try:
                target.configure(state="disabled")
            except:
                pass
        
        target.bind("<Button-1>", lambda e: self._inicio_dr(e, padre), add="+")
        target.bind("<B1-Motion>", lambda e: self._movimiento_dr(e, padre), add="+")
        target.bind("<ButtonRelease-1>", lambda e: self._fin_dr(), add="+")
        target.bind("<Button-3>", lambda e: self._inicio_rs(e, padre), add="+")
        target.bind("<B3-Motion>", lambda e: self._movimiento_rs(e, padre), add="+")
        
        for hijo in target.winfo_children():
            self._aplicar_escudo_total(hijo, padre)

    def _inicio_dr(self, e, w):
        if not self.activo: return
        self.drag_data["widget"] = w
        self.drag_data["x"] = e.x_root
        self.drag_data["y"] = e.y_root
        w.lift()

    def _movimiento_dr(self, e, w):
        if not self.activo or self.drag_data["widget"] is not w: return
        dx = e.x_root - self.drag_data["x"]
        dy = e.y_root - self.drag_data["y"]
        w.place(x=w.winfo_x() + dx, y=w.winfo_y() + dy)
        self.drag_data["x"] = e.x_root
        self.drag_data["y"] = e.y_root

    def _fin_dr(self):
        self.drag_data["widget"] = None

    def _inicio_rs(self, e, w):
        if not self.activo: return
        self.drag_data["x"] = e.x_root
        self.drag_data["y"] = e.y_root

    def _movimiento_rs(self, e, w):
        if not self.activo: return
        dx = e.x_root - self.drag_data["x"]
        dy = e.y_root - self.drag_data["y"]
        nw = max(20, w.winfo_width() + dx)
        nh = max(10, w.winfo_height() + dy)
        w.configure(width=nw, height=nh)
        self.drag_data["x"] = e.x_root
        self.drag_data["y"] = e.y_root