# utils/ — Utilidades Transversales

> Capa de utilidades compartidas. Disponible para cualquier capa del proyecto sin crear dependencias circulares.

---

## Índice

1. [Responsabilidad de la capa](#1-responsabilidad-de-la-capa)
2. [formateo.py](#2-formateopy)
3. [Propuestas de implementación futura](#3-propuestas-de-implementación-futura)

---

## 1. Responsabilidad de la capa

```
utils/
├── __init__.py
└── formateo.py   ← Vacío. Reservado para funciones de formateo y exportación.
```

La capa `utils` está pensada para funciones de apoyo que no pertenecen a ninguna capa concreta: formateo de números, exportación de datos, helpers de texto, etc.

---

## 2. `formateo.py`

**Estado actual:** vacío.

Este módulo está reservado para centralizar cualquier lógica de presentación o transformación de datos que sea reutilizable entre capas.

---

## 3. Propuestas de implementación futura

Las siguientes funciones serían candidatas naturales para este módulo:

### `formatear_usd(valor: float) -> str`
Formatea un valor float como cadena de dólares con 6 decimales.
```python
formatear_usd(0.000325)  # → "$0.000325"
```

### `formatear_eur(valor_usd: float, tipo_cambio: float = 0.92) -> str`
Convierte USD a EUR y formatea la cadena resultante.
```python
formatear_eur(0.000325)  # → "€0.000299"
```

### `exportar_resultado_txt(resultado: dict, ruta: str) -> None`
Guarda el resultado de un cálculo en un fichero `.txt`.

### `exportar_resultado_csv(resultado: dict, ruta: str) -> None`
Guarda el resultado en formato CSV para análisis posterior.

> ℹ️ Centralizar el formateo aquí evita tener el tipo de cambio hardcodeado en `ui/app.py` y facilita cambios futuros en un único lugar.