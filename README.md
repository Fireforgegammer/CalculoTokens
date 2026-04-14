# CalculoTokens

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.10+-3776ab?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue?logo=semver&logoColor=white)](https://github.com/Fireforgegammer/CalculoTokens/releases)
[![License](https://img.shields.io/badge/license-MIT-green?logo=open-source-initiative&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/status-production-success?logo=checkmark&logoColor=white)](https://github.com/Fireforgegammer/CalculoTokens)
[![Code Size](https://img.shields.io/github/languages/code-size/Fireforgegammer/CalculoTokens?logo=github&logoColor=white)](https://github.com/Fireforgegammer/CalculoTokens)
[![Last Commit](https://img.shields.io/github/last-commit/Fireforgegammer/CalculoTokens?logo=git&logoColor=white)](https://github.com/Fireforgegammer/CalculoTokens)

**Calculadora profesional de tokens y costes para APIs de IA**

> Estima tokens y costes de llamadas a OpenAI, Anthropic y Google sin realizar llamadas reales. Totalmente local, configurable y de código abierto.

[🚀 Inicio rápido](#quick-start) • [📚 Documentación](#documentación-detallada) • [🏗️ Arquitectura](#-arquitectura-del-proyecto) • [🤝 Contribuir](#-contribuciones) • [👤 Autor](#-autor)

</div>

---

## 📋 Tabla de Contenidos

> Haz clic en cualquier sección para navegar

- [✨ Características principales](#-características-principales)
- [📦 Requisitos](#-requisitos)
- [🚀 Instalación y uso](#-instalación-y-uso)
- [🏗️ Arquitectura del proyecto](#-arquitectura-del-proyecto)
- [🔧 Cómo funciona](#-cómo-funciona)
- [📊 Modelos soportados](#-modelos-soportados)
- [🧪 Testing](#-testing)
- [📚 Documentación detallada](#-documentación-detallada)
- [🛣️ Roadmap](#-roadmap-y-mejoras-futuras)
- [❓ FAQ](#-faq)
- [📄 Licencia](#-licencia)
- [👤 Autor](#-autor)

---

## ✨ Características principales

### 💡 Funcionalidad central

- ✅ **Estimación de tokens** para 6 modelos de IA diferentes
- ✅ **Cálculo de costes** en USD y EUR (conversión automática)
- ✅ **Sin llamadas reales** - Todo local, sin dependencias externas de API
- ✅ **Interfaz gráfica moderna** - Construida con customtkinter
- ✅ **Arquitectura profesional** - Tres capas bien definidas (UI → Servicios → Core)
- ✅ **Totalmente testeable** - Suite de pruebas con pytest

### 🎨 Modos de visualización

| Modo | Descripción | Uso |
|------|-------------|-----|
| **Versión Oficial** | Interfaz limpia y profesional | Producción, equipos |
| **Versión Personalizable** | Personalización completa (tipografía, colores, drag&drop) | Desarrollo, preferencias personales |

### 🛠️ Panel de opciones (modo personalizable)

- 🎯 **Ajustes Visuales:** Tipografía y tamaño de fuente
- 🎨 **Colores de Fondos:** Personalización de secciones
- 🖼️ **Colores de Ventanas:** Interior de cajas de resultados
- ✏️ **Modo Diseño:** Repositorador de widgets con drag & drop

---

## 📦 Requisitos

### Sistema operativo

- ✅ Windows 10+
- ✅ macOS 10.14+
- ✅ Linux (Ubuntu 18.04+, Debian 10+)

### Software

- **Python:** 3.10 o superior
- **pip:** Gestor de paquetes Python (incluido con Python)

### Dependencias

```txt
customtkinter>=5.0.0   # GUI moderna y cross-platform
tiktoken>=0.5.0        # Tokenización (OpenAI)
pytest>=7.0.0          # Testing (desarrollo)
pytest-cov>=4.0.0      # Cobertura de tests (desarrollo)
```

---

## 🚀 Instalación y uso

### Opción 1: Desde GitHub (recomendado)

```bash
# 1. Clonar el repositorio
git clone https://github.com/Fireforgegammer/CalculoTokens.git
cd CalculoTokens

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# 3. Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requisitos.txt

# 5. Ejecutar la aplicación
python main.py
```

### Opción 2: Sin entorno virtual (rápido)

```bash
git clone https://github.com/Fireforgegammer/CalculoTokens.git
cd CalculoTokens
pip install -r requisitos.txt
python main.py
```

### Primer uso

1. **Selector de versión:** Elige entre "Oficial" o "Personalizable"
2. **Interfaz principal:** Ingresa tu texto en el área de texto
3. **Selecciona modelo:** GPT-4o, Claude 3 Sonnet, Gemini 1.5, etc.
4. **Calcular:** Haz clic en "Calcular"
5. **Resultados:** Observa tokens y costes en las secciones inferiores

---

## 🏗️ Arquitectura del proyecto

### Diseño en capas

La aplicación sigue una **arquitectura en capas rigurosa** que garantiza bajo acoplamiento y alta cohesión:

```
┌───────────────────────────────────────┐
│            UI Layer                   │
│  ui/app.py · ui/componentes.py        │
│  ui/editor.py · main.py              │
├───────────────────────────────────────┤
│          Service Layer                │
│   servicios/calculo_servicio.py       │
├───────────────────────────────────────┤
│            Core Layer                 │
│  core/calculadora.py · core/tokens.py │
│  core/precios.py                      │
└───────────────────────────────────────┘
```

### Regla fundamental

```
UI → Servicios → Core

✅ Permitido: UI llama a Servicios
❌ Prohibido: UI llama directamente a Core
❌ Prohibido: Core depende de UI
```

### Estructura de carpetas

```
CalculoTokens/
│
├── 📁 core/                    # Lógica de negocio (sin UI)
│   ├── calculadora.py          # CalculadoraCostes
│   ├── tokens.py               # estimar_tokens()
│   └── precios.py              # PRECIOS_MODELOS
│
├── 📁 servicios/               # Orquestación
│   └── calculo_servicio.py     # calcular_desde_texto()
│
├── 📁 ui/                      # Interfaz gráfica
│   ├── app.py                  # iniciar_app()
│   ├── componentes.py          # Widgets
│   └── editor.py               # Modo diseño
│
├── 📁 utils/                   # Utilidades
│   └── formateo.py
│
├── 📁 tests/                   # Tests
│   └── test_calculo.py
│
├── 📁 documentacion/           # Docs
│   └── *.md
│
├── main.py                     # 🚀 Entrada
└── requisitos.txt              # 📦 Deps
```

---

## 🔧 Cómo funciona

### 1. Estimación de tokens

CalculoTokens utiliza **tiktoken** (librería oficial de OpenAI):

```python
def estimar_tokens(texto, modelo) -> int:
    try:
        encoding = tiktoken.encoding_for_model(modelo)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(texto))
```

### 2. Cálculo de costes

Precios por **millón de tokens**:

```python
coste = (tokens / 1_000_000) × precio_por_millón
```

### 3. Conversión EUR

```python
coste_eur = coste_usd × 0.92
```

---

## 📊 Modelos soportados

### OpenAI

| Modelo | Input | Output |
|--------|-------|--------|
| **gpt-4o** | $2.50/M | $10.00/M |
| **gpt-4o-mini** | $0.15/M | $0.60/M |
| **gpt-4-turbo** | $10.00/M | $30.00/M |

### Anthropic

| Modelo | Input | Output |
|--------|-------|--------|
| **claude-3-sonnet** | $3.00/M | $15.00/M |

### Google

| Modelo | Input | Output |
|--------|-------|--------|
| **gemini-1.5-flash** | $0.075/M | $0.30/M |
| **gemini-1.5-pro** | $1.25/M | $5.00/M |

---

## 🧪 Testing

### Ejecutar tests

```bash
pytest
pytest --cov=core --cov=servicios
```

### Tests disponibles

- `test_calculo_texto_vacio` - Valida con texto vacío
- `test_coste_es_positivo` - Verifica costes no negativos
- `test_verificar_estructura_datos` - Valida estructura

---

## 📚 Documentación detallada

| Documento | Contenido |
|-----------|----------|
| [memoriafinal.md](documentacion/memoriafinal.md) | 📄 Análisis completo del proyecto |
| [core.md](documentacion/core.md) | 🧮 Lógica de negocio |
| [servicios.md](documentacion/servicios.md) | ⚙️ Capa de servicios |
| [ui.md](documentacion/ui.md) | 🖥️ Interfaz gráfica |
| [tests.md](documentacion/tests.md) | ✅ Estrategia de testing |

---

## 🛣️ Roadmap y mejoras futuras

### v1.1
- [ ] Tipo de cambio EUR/USD en tiempo real
- [ ] Tokens de salida personalizable
- [ ] Exportar a CSV/JSON/Excel
- [ ] Historial de cálculos

### v1.2
- [ ] Modelos multimodales
- [ ] Estimación de latencia
- [ ] Atajos de teclado

### v2.0
- [ ] Aplicación web
- [ ] API REST local
- [ ] Distribuible ejecutable

---

## ❓ FAQ

**¿Necesito una API key?**
No. CalculoTokens es completamente local.

**¿Por qué los costes no son exactos?**
Son estimaciones basadas en tiktoken, precios publicados y cambio EUR/USD.

**¿Puedo agregar más modelos?**
Sí. Edita `core/precios.py`.

**¿Funciona en Mac/Linux?**
Sí. Es cross-platform.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el repo
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

MIT License. Ver [LICENSE](LICENSE) para detalles.

---

## 👤 Autor

<div align="center">

### Fireforgegammer

[![GitHub](https://img.shields.io/badge/GitHub-Fireforgegammer-333?logo=github&logoColor=white&style=for-the-badge)](https://github.com/Fireforgegammer)

**Desarrollador independiente | Python Expert | Software Architect**

[GitHub](https://github.com/Fireforgegammer) • [Portfolio](https://fireforgegammer.dev)

</div>

---

<div align="center">

### ⭐ Si este proyecto te fue útil, por favor ⭐ deja una estrella

**[↑ Volver al inicio](#calculotokens)**

---

**Hecho con ❤️ por Fireforgegammer**

v1.0.0 • Abril 2026 • CalculoTokens

</div>