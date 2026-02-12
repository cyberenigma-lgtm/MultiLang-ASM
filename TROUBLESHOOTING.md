# 🛠️ Solución de Problemas (Troubleshooting)

Aquí encontrarás respuesta a los problemas más comunes reportados por la comunidad.

## 1. Error de Codificación (UTF-8) en Windows
**Problema**: Caracteres especiales (como la `ñ` o caracteres árabes/asiáticos) se ven mal o causan error.
**Solución**: MultiLang-ASM v0.6 incluye un fix automático para la consola de Windows. Si el problema persiste, asegúrate de guardar tus archivos con codificación **UTF-8 sin BOM**.

## 2. El idioma no aparece en `--list-langs`
**Problema**: He creado un archivo en `langs/` pero no aparece en la lista.
**Solución**:
- Verifica que el archivo termine en `.py`.
- Asegúrate de que tenga el diccionario `METADATA` correctamente definido.
- Revisa si hay errores de sintaxis en tu archivo de idioma (el motor imprimirá un aviso si falla la carga).

## 3. `ModuleNotFoundError: No module named 'importlib'`
**Problema**: Python no encuentra el cargador de módulos.
**Solución**: Estás usando una versión muy antigua de Python. MultiLang-ASM v0.6 requiere **Python 3.6+**.

## 4. Error al compilar con NASM
**Problema**: El archivo `.asm` generado por MultiLang-ASM da error en NASM.
**Solución**: MultiLang-ASM traduce las palabras clave, pero no valida la lógica de registros o memoria. Verifica que los operandos sean válidos para la arquitectura x86_64.

## 5. Comandos del CLI no reconocidos
**Problema**: `--list-langs` da error de argumentos.
**Solución**: Asegúrate de estar usando el script principal: `python mlasm.py --list-langs`. El orden de los argumentos importa.
