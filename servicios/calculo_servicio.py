from core.calculadora import CalculadoraCostes
from core.tokens import estimar_tokens

def calcular_desde_texto(texto_usuario: str, modelo_seleccionado: str):
    calculadora = CalculadoraCostes(modelo_seleccionado)

    tokens_entrada = estimar_tokens(texto_usuario, modelo_seleccionado)
    tokens_salida = 200

    resultado_costes = calculadora.calcular_costes(
        tokens_input=tokens_entrada,
        tokens_output=tokens_salida
    )

    return {
        "tokens_entrada": tokens_entrada,
        "tokens_salida": tokens_salida,
        "tokens_totales": tokens_entrada + tokens_salida,
        "costes": resultado_costes
    }