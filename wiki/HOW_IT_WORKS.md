# MultiLang-ASM: ¿Cómo Actúa el Motor Babel?

Este documento detalla el funcionamiento interno de MultiLang-ASM v0.7+, explicando cómo se logra la traducción en tiempo real de múltiples lenguas a código máquina.

## ⚙️ El Ciclo de Vida de la Traducción

Cuando ejecutas `python mlasm.py <lang> <archivo>.masm`, el motor realiza los siguientes pasos:

### 1. Carga Dinámica de Packs
El motor escanea la carpeta `langs/`. Cada archivo `.py` es un módulo independiente que contiene los diccionarios `KEYWORDS` (traducción estándar) y `KIDS_KEYWORDS` (simplificado).

### 2. Análisis y Tokenización
MultiLang-ASM procesa el archivo `.masm` línea por línea.
- Ignora comentarios (denotados por `;`).
- Identifica "tokens" (instrucciones, registros, etiquetas).

### 3. El Motor de Traducción (Mapping)
Si el token es una palabra clave nativa (ej: `sumar` en español), el motor consulta la tabla del idioma cargado y la reemplaza por su mnemónico NASM equivalente (ej: `add`).
- **Registros**: Los registros (rax, rbx, etc.) se mantienen estándar para asegurar compatibilidad técnica universal.
- **Directivas**: Secciones como `.data` y `.text` también son traducibles según el paquete de idioma.

### 4. Generación de NASM y Ensamblado
Una vez traducido todo el código a NASM puro, el motor:
1. Crea un archivo temporal `.asm`.
2. Llama a `nasm` para generar el objeto binario.
3. Llama a `ld` (linker) para crear el ejecutable final.

## 🕵️ Autodetección de Idioma
Si no especificas un idioma, MultiLang-ASM analiza las primeras líneas del archivo buscando palabras clave características. Si detecta una coincidencia de alta confianza (ej: `moure` indica Catalán), carga el pack automáticamente.

## 🛠️ Cómo Corregir Problemas del Motor
Si necesitas ajustar cómo "actúa" el motor para un idioma específico:
- **Prioridad de Mapeo**: El motor siempre busca primero en `KEYWORDS` y luego en las palabras clave estándar.
- **Modo Kids**: Si activas `--kids`, el motor utiliza una tabla reducida de comandos ultra-legibles, ideal para educación sin perder potencia técnica.
