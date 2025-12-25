# 📋 MultiLang-ASM: Changelog

## v0.2 - "Production Ready" (2025-12-25)

### ✨ Nuevas Características
- **Alias Múltiples:** Ahora puedes escribir `mover`, `mov`, o `copiar` y todos funcionan.
- **Soporte Unicode Completo:** Regex mejorado para detectar etiquetas, puntos, guiones y caracteres especiales.
- **Preservación de Comentarios:** Los comentarios con `;` se mantienen intactos durante la traducción.
- **CLI Mejorado:** Mensajes más claros y humanos que muestran idioma, modo y estado.
- **Case-Insensitive:** Los mnemónicos en idiomas latinos no distinguen mayúsculas/minúsculas.

### 🔧 Mejoras Técnicas
- **Regex Robusto:** Ahora soporta `movzx`, `jmp.short`, `call qword`, etiquetas como `_start:`.
- **Manejo de Errores:** Mensajes específicos para archivos no encontrados vs errores inesperados.
- **Optimización de Reversa:** Solo se usa el primer alias encontrado para evitar confusiones.

### 🌐 Idiomas Expandidos
- Soporte completo para 10 idiomas: ES, FR, IT, AR, DE, RU, KO, ID, ZH, JA
- Cada idioma incluye alias comunes y formas verbales alternativas

### 📖 Ejemplos de Nuevo Soporte

```asm
; Español tradicional
mover rax, rbx

; Español alternativo (todos válidos)
mov rax, rbx
copiar rax, rbx

; Con comentarios preservados
saltar inicio  ; Este comentario se mantiene
```

### 🚀 Uso

```bash
# Traducir de español a NASM
python mlasm.py es programa_es.asm programa.asm

# Ver en otro idioma (modo reversible)
python mlasm.py fr programa.asm programa_fr.asm --reverse
```

---

## v0.1 - "Primer Prototipo" (2025-12-25)

### ✨ Características Iniciales
- Traducción básica entre idiomas nativos y NASM
- Soporte para 10 idiomas
- Modo reversible para visualización
- Diccionario de instrucciones base

---

> [!NOTE]
> Esta herramienta está en desarrollo activo. Las contribuciones son bienvenidas.
