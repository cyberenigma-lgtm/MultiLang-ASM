# MultiLang-ASM: Wiki de Troubleshooting (Resolución de Problemas)

Esta guía explica cómo actuar ante errores comunes y cómo corregir problemas de sintaxis o configuración en MultiLang-ASM v0.7+.

## 🗺️ Índice de Problemas Comunes

1. [Error de Idioma No Encontrado](#1-error-de-idioma-no-encontrado)
2. [Instrucción Inválida o No Mapeada](#2-instrucción-inválida-o-no-mapeada)
3. [Conflictos de Codificación (UTF-8)](#3-conflictos-de-codificación-utf-8)
4. [Problemas de Compilación con NASM](#4-problemas-de-compilación-con-nasm)

---

## 1. Error de Idioma No Encontrado
**Síntoma**: El motor lanza un error indicando que el paquete de idioma especificado no existe.
**Cómo Actuar**:
- Verifica el código de idioma usando `python mlasm.py --list-langs`.
- Asegúrate de que el archivo `.py` correspondiente esté en la carpeta `langs/`.
- **Corrección**: Si el idioma es nuevo, utiliza `python mlasm.py --new-lang <code>` para generar la plantilla base.

## 2. Instrucción Inválida o No Mapeada
**Síntoma**: "Token 'xyz' no reconocido en el idioma 'abc'".
**Cómo Actuar**:
- Consulta el manual `docs/INSTRUCCIONES_<LANG>.md` para verificar el mapeo exacto.
- Las instrucciones deben coincidir exactamente con las palabras clave definidas en el paquete de idioma.
- **Corrección**: Si falta una instrucción esencial, edita el archivo `langs/<lang>.py` y añádela al diccionario `KEYWORDS`.

## 3. Conflictos de Codificación (UTF-8)
**Síntoma**: Caracteres extraños en idiomas no latinos (Hindi, Árabe, Chino).
**Cómo Actuar**:
- Asegúrate de que tu editor de texto guarde los archivos `.masm` con codificación **UTF-8 (sin BOM)**.
- **Corrección**: En VS Code, verifica la esquina inferior derecha. Si dice "Windows-1252" o similar, cambia a "Reopen with encoding -> UTF-8".

## 4. Problemas de Compilación con NASM
**Síntoma**: MultiLang-ASM genera el `.asm` pero NASM falla al procesarlo.
**Cómo Actuar**:
- Revisa el archivo `.asm` generado temporalmente.
- MultiLang-ASM traduce tus palabras nativas a mnemónicos x86_64 estándar. Si el error persiste en NASM, el problema suele ser la sintaxis del operando (ej. registros mal nombrados).
- **Corrección**: Usa mnemónicos estándar dentro de los bloques de código si estás realizando operaciones muy avanzadas no cubiertas por el mapeo base.

---

## 💡 ¿Cómo actuar ante un error nuevo?
1. **Identifica el origen**: ¿Es un error de MultiLang (traducción) o de NASM (ensamblado)?
2. **Revisa la Wiki de Idiomas**: Verifica si el comando que usas está soportado para esa región.
3. **Modo Kids**: Si el código es muy complejo, intenta probarlo en Modo Kids (`--kids`) para ver si la lógica simplificada funciona.
