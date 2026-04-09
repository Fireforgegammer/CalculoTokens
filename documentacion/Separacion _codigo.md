🧠 CÓMO SEPARAR TU CÓDIGO (CLAVE)
🔹 1. core/ → lógica pura (SIN interfaz)

Aquí va lo importante:

👉 calculadora.py

class CalculadoraCostes:
    ...

👉 tokens.py

import tiktoken

def estimar_tokens(texto, modelo):
    try:
        encoding = tiktoken.encoding_for_model(modelo)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(texto))

👉 precios.py

PRECIOS = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    ...
}
🔹 2. services/ → conecta todo (MUY IMPORTANTE)

Aquí haces la “magia” que usa la UI.

👉 calculo_service.py

from core.calculadora import CalculadoraCostes
from core.tokens import estimar_tokens

def calcular_desde_texto(texto, modelo):
    calc = CalculadoraCostes(modelo)

    tokens_input = estimar_tokens(texto, modelo)
    tokens_output = 200  # tu estimación

    return calc.calcular_costes(tokens_input, tokens_output)

👉 Esto es CLAVE: la UI no piensa, solo llama a esto.

🔹 3. ui/ → interfaz (lo que tienes ahora)

Tu ventana va aquí.

👉 app.py

from services.calculo_service import calcular_desde_texto

def on_calcular_click():
    texto = input_text.get()
    modelo = modelo_input.get()

    resultado = calcular_desde_texto(texto, modelo)

    mostrar_resultados(resultado)
🔹 4. main.py → arranque limpio
from ui.app import iniciar_app

if __name__ == "__main__":
    iniciar_app()
⚠️ ERRORES QUE EVITAS CON ESTO

Con esta estructura evitas:

❌ Mezclar UI con lógica
❌ Código imposible de testear
❌ Repetición
❌ Dependencias raras entre archivos

💡 MAPA MENTAL (MUY IMPORTANTE)

Piensa así:

UI (botón)
   ↓
SERVICE (decide qué hacer)
   ↓
CORE (hace cálculos)
   ↓
RESULTADO
   ↑
UI (lo pinta)