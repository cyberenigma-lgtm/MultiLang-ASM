# 🚀 Guía de Inicio Rápido (v0.6 Babel)

Bienvenido a la versión más potente de MultiLang-ASM. Esta guía te enseñará a configurar y usar el ensamblador en menos de 5 minutos.

## 1. Requisitos
- Python 3.6 o superior.
- NASM (si deseas compilar el código resultante).

## 2. Instalación
Simplemente clona el repositorio o descarga los archivos. No requiere instalación de dependencias externas (`importlib` y `os` son parte de la librería estándar de Python).

## 3. Uso Básico (Traducción)
Para traducir un archivo de tu idioma nativo a NASM estándar:
```bash
python mlasm.py es programa.masm programa.asm
```

## 4. Comandos de la Comunidad (Novedad v0.6)
### Listar idiomas instalados
```bash
python mlasm.py --list-langs
```
### Crear tu propio paquete de idioma
```bash
python mlasm.py --new-lang <iso_code>
```

## 5. Próximos Pasos
- Consulta el [Manual Avanzado](../MANUAL_AVANZADO.md) para conocer las directivas y macros.
- Mira los [Ejemplos](../examples/) para inspirarte.
- Únete a la [Babel Community](../BABEL_COMMUNITY.md).
