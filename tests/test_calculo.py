import pytest
from servicios.calculo_servicio import calcular_desde_texto

def test_calculo_texto_vacio():
    resultado = calcular_desde_texto("", "gpt-4o")
    assert resultado["tokens_entrada"] == 0
    assert resultado["tokens_totales"] == 200

def test_coste_es_positivo():
    resultado = calcular_desde_texto("Hola mundo", "gpt-4o")
    assert resultado["costes"]["coste_total_usd"] >= 0
    assert "tokens_entrada" in resultado

def test_verificar_estructura_datos():
    resultado = calcular_desde_texto("Prueba técnica", "gpt-4o")
    campos_obligatorios = {"tokens_entrada", "tokens_salida", "tokens_totales", "costes"}
    assert set(resultado.keys()) == campos_obligatorios