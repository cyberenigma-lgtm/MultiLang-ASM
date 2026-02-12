# 🎓 Manual Avanzado (MultiLang-ASM v0.6)

Este manual está dirigido a desarrolladores que desean exprimir al máximo el motor Babel o contribuir con nuevos idiomas.

## 1. El Interfaz de Línea de Comandos (CLI)

### Comandos de Inspección
- `python mlasm.py --list-langs`: Muestra la lista de idiomas instalados, sus autores y versiones. Útil para verificar que tu nuevo pack se cargó correctamente.

### Comandos de Creación
- `python mlasm.py --new-lang <código>`: Genera un archivo `.py` en `langs/` con la estructura mínima requerida. El código debe ser preferiblemente el estándar ISO de 2 letras (ej. `fr`, `jp`).

## 2. Creación de Paquetes de Idiomas

Un paquete de idioma es un módulo Python con tres diccionarios clave:

### METADATA
```python
METADATA = {
    "name": "Nombre Visual",
    "author": "Tu Nombre",
    "version": "1.0",
    "description": "Breve descripción del pack."
}
```

### KEYWORDS
Mapeo directo de palabras nativas a mnemónicos de NASM.
```python
KEYWORDS = {
    "palabra_nativa": "mov",
    "otra_palabra": "add"
}
```

### KIDS_KEYWORDS
Diccionario anidado para el modo educativo.
```python
KIDS_KEYWORDS = {
    "iso": {"pon": "mov", "suma": "add"}
}
```

## 3. Directivas de Preprocesador
MultiLang-ASM v0.6 soporta:
- `%define <NOMBRE> <VALOR>`: Sustitución de constantes.
- Estas directivas funcionan de forma global independientemente del idioma seleccionado.

## 4. Mejores Prácticas para Contribuyentes
1. **Consistencia**: Usa términos técnicos aceptados en tu comunidad lingüística.
2. **Reversibilidad**: Asegúrate de que los mapeos sean claros para que el modo `--reverse` tenga sentido.
3. **Dialectos**: Si creas un dialecto (ej. `es_and`), basa tu pack en el pack estándar e incluye solo las variaciones.
