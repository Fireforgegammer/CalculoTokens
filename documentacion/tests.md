# tests/ — Suite de Pruebas

> Capa de testing automatizado con `pytest`.  
> **Objetivo:** Verificar que la capa de servicios se comporta correctamente ante distintas entradas.

---

## Índice

1. [Estructura](#1-estructura)
2. [test_calculo.py](#2-test_calculopy)
3. [Ejecución de tests](#3-ejecución-de-tests)
4. [Cobertura actual y gaps](#4-cobertura-actual-y-gaps)

---

## 1. Estructura

```
tests/
├── __pycache__/
└── test_calculo.py   ← Tests de integración del servicio de cálculo
```

Los tests se ejecutan sobre `servicios/calculo_servicio.py` y validan el contrato de la función `calcular_desde_texto`.

---

## 2. `test_calculo.py`

### Dependencias

```python
import pytest
from servicios.calculo_servicio import calcular_desde_texto
```

---

### `test_calculo_texto_vacio`

**Descripción:** Verifica el comportamiento con texto vacío.

**Assertions:**
- `resultado["tokens_entrada"] == 0`
- `resultado["tokens_totales"] == 200` _(tokens_salida fijo)_

```python
def test_calculo_texto_vacio():
    resultado = calcular_desde_texto("", "gpt-4o")
    assert resultado["tokens_entrada"] == 0
    assert resultado["tokens_totales"] == 200
```

---

### `test_coste_es_positivo`

**Descripción:** Verifica que el coste calculado es un valor positivo y que la estructura de respuesta incluye `tokens_entrada`.

**Assertions:**
- `resultado["costes"]["coste_total_usd"] >= 0`
- `"tokens_entrada" in resultado`

```python
def test_coste_es_positivo():
    resultado = calcular_desde_texto("Hola mundo", "gpt-4o")
    assert resultado["costes"]["coste_total_usd"] >= 0
    assert "tokens_entrada" in resultado
```

---

### `test_verificar_estructura_datos`

**Descripción:** Verifica que el dict de respuesta contiene exactamente las claves esperadas.

**Assertions:**
- `set(resultado.keys()) == {"tokens_entrada", "tokens_salida", "tokens_totales", "costes"}`

```python
def test_verificar_estructura_datos():
    resultado = calcular_desde_texto("Prueba técnica", "gpt-4o")
    campos_obligatorios = {"tokens_entrada", "tokens_salida", "tokens_totales", "costes"}
    assert set(resultado.keys()) == campos_obligatorios
```

---

## 3. Ejecución de tests

**Ejecutar todos los tests:**
```bash
pytest tests/
```

**Con reporte de cobertura:**
```bash
pytest tests/ --cov=.
```

**Con reporte HTML de cobertura:**
```bash
pytest tests/ --cov=. --cov-report=html
```

**Ejecutar un test específico:**
```bash
pytest tests/test_calculo.py::test_coste_es_positivo
```

---

## 4. Cobertura actual y gaps

### Cubierto ✅

| Escenario                         | Test                              |
|-----------------------------------|-----------------------------------|
| Texto vacío                       | `test_calculo_texto_vacio`        |
| Coste positivo con texto real     | `test_coste_es_positivo`          |
| Estructura del dict de respuesta  | `test_verificar_estructura_datos` |

### No cubierto ⚠️ (mejoras recomendadas)

| Escenario                                      | Riesgo         |
|------------------------------------------------|----------------|
| Modelo desconocido → `ValueError`              | 🔴 Alto        |
| Texto muy largo (>100k tokens)                 | 🟡 Medio       |
| Texto con caracteres Unicode / emojis          | 🟡 Medio       |
| Coste con modelo de Google o Anthropic         | 🟡 Medio       |
| Valores numéricos correctos de `coste_total`   | 🟡 Medio       |
| `tokens_totales == tokens_entrada + 200`       | 🟢 Bajo        |