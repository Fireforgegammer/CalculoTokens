import customtkinter as ctk
from ui.app import iniciar_app

def selector_de_version():
    bienvenida = ctk.CTk()
    bienvenida.title("Selector de Versión")
    bienvenida.geometry("400x350")
    ctk.set_appearance_mode("light")
    bienvenida.configure(fg_color="#f0f2f5")

    ctk.CTkLabel(bienvenida, text="Calculadora de Tokens", font=("Comic Sans MS", 20, "bold"), text_color="#2c3e50").pack(pady=(40, 10))
    ctk.CTkLabel(bienvenida, text="Selecciona el modo de visualización", font=("Comic Sans MS", 12), text_color="#7f8c8d").pack(pady=(0, 30))

    def abrir(personalizable):
        bienvenida.destroy()
        iniciar_app(es_personalizable=personalizable)

    ctk.CTkButton(bienvenida, text="Versión Oficial (Empresa)", command=lambda: abrir(False), height=45, width=250, fg_color="#2c3e50", corner_radius=15, font=("Comic Sans MS", 12, "bold")).pack(pady=10)
    ctk.CTkButton(bienvenida, text="Versión Personalizable", command=lambda: abrir(True), height=45, width=250, fg_color="#34495e", corner_radius=15, font=("Comic Sans MS", 12, "bold")).pack(pady=10)

    bienvenida.mainloop()

if __name__ == "__main__":
    selector_de_version()