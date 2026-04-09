from core.precios import PRECIOS_MODELOS


class CalculadoraCostes:

    def __init__(self, modelo: str):
        if modelo not in PRECIOS_MODELOS:
            raise ValueError(f"Modelo no soportado: {modelo}")

        self.modelo = modelo
        self.precios = PRECIOS_MODELOS[modelo]

    def calcular_costes(self, tokens_input: int, tokens_output: int) -> dict:
        coste_input = (tokens_input / 1_000_000) * self.precios["input"]
        coste_output = (tokens_output / 1_000_000) * self.precios["output"]
        coste_total = coste_input + coste_output

        return {
            "coste_input_usd": coste_input,
            "coste_output_usd": coste_output,
            "coste_total_usd": coste_total,
            "coste_input_cent": coste_input * 100,
            "coste_output_cent": coste_output * 100,
            "coste_total_cent": coste_total * 100
        }