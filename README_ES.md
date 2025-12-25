# 🛡️ MultiLang-ASM v0.2

> *"No saber inglés no debería impedirte crear. La imaginación no tiene idioma."*

**El primer ensamblador multilingüe. Escribe ensamblador x86_64 en tu idioma nativo.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-10-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/INSTRUCCIONES_ES.md)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

📖 **Español** | **[English](README.md)**

---

## 🚀 ¿Qué es esto?

Ya no necesitas dominar inglés para crear kernels, drivers o firmware.

Este proyecto demuestra que las barreras lingüísticas en la programación son **artificiales** y eliminables.

## 💡 ¿Por qué importa?

La mayoría de las herramientas de bajo nivel fueron diseñadas en un contexto angloparlante hace décadas. Esto ha creado una barrera invisible que excluye a millones de personas con talento, creatividad e ideas brillantes.

**MultiLang-ASM rompe esa herencia** y abre la puerta a:
- Estudiantes que aprenden en su idioma nativo
- Autodidactas sin acceso a educación formal en inglés
- Comunidades enteras que hoy están fuera del bajo nivel
- Niños que pueden experimentar sin barreras artificiales

No es solo código. Es **justicia tecnológica**.

## ✨ Características

- 🌐 **Multilingüe:** Escribe en Español, Árabe, Francés, Italiano, Portugués...
- 🔄 **Reversible:** Visualiza el mismo código en diferentes idiomas sin modificarlo
- 🛠️ **Compatible:** Genera ASM estándar compatible con NASM, FASM y GAS
- 📚 **Educativo:** Ideal para estudiantes y autodidactas sin conocimientos previos de inglés
- 🎯 **Universal:** El binario final es idéntico, sin importar el idioma usado

## 📖 Ejemplo Rápido

### Código en Español
```asm
mover rax, rbx
sumar rax, 4
saltar etiqueta_fin
```

### Código en Árabe
```asm
نقل rax, rbx
جمع rax, 4
اقفز etiqueta_fin
```

### Ambos generan el mismo ASM estándar
```asm
mov rax, rbx
add rax, 4
jmp etiqueta_fin
```

## 🎯 Uso

### 1. Traducir de tu idioma a NASM
```bash
python mlasm.py es demo_es.masm demo.asm
```

### 2. Compilar normalmente
```bash
nasm -f elf64 demo.asm -o demo.o
ld demo.o -o demo
```

### 3. Visualizar en otro idioma (modo reversible)
```bash
python mlasm.py fr demo.asm demo_fr.masm --reverse
```

## 📊 Mapa de Instrucciones Soportadas

| Idioma | Ejemplo | Traducción | ASM Estándar |
|--------|---------|------------|-------------|
| Español | `mover rax, rbx` | → | `mov rax, rbx` |
| Árabe | `نقل rax, rbx` | → | `mov rax, rbx` |
| Francés | `depl rax, rbx` | → | `mov rax, rbx` |
| Alemán | `bewegen rax, rbx` | → | `mov rax, rbx` |
| Ruso | `перенести rax, rbx` | → | `mov rax, rbx` |
| Japonés | `移動 rax, rbx` | → | `mov rax, rbx` |
| Coreano | `이동 rax, rbx` | → | `mov rax, rbx` |

Ver diccionario completo en [`mlasm.py`](mlasm.py).

## 🌟 Filosofía

Este proyecto nace de una convicción simple:

- El inglés no es un requisito **técnico**, es una convención **histórica**
- La CPU entiende **opcodes**, no idiomas humanos
- Eliminar barreras lingüísticas **democratiza** la tecnología
- La creatividad no debería depender del idioma que hablas

## 🗺️ Idiomas Soportados

| Idioma | Código | Estado |
|--------|--------|--------|
| Español | `es` | ✅ Activo |
| Francés | `fr` | ✅ Activo |
| Italiano | `it` | ✅ Activo |
| Árabe | `ar` | ✅ Activo |
| Alemán | `de` | ✅ Activo |
| Ruso | `ru` | ✅ Activo |
| Coreano | `ko` | ✅ Activo |
| Indonesio | `id` | ✅ Activo |
| Chino Tradicional | `zh` | ✅ Activo |
| Japonés | `ja` | ✅ Activo |
| Portugués | `pt` | 📋 Planeado |
| Hindi | `hi` | 📋 Planeado |
| Swahili | `sw` | 📋 Planeado |

## 🛠️ Instalación

```bash
git clone https://github.com/tuusuario/MultiLang-ASM.git
cd MultiLang-ASM
python mlasm.py --help
```

No se requieren dependencias externas. Solo Python 3.6+.

## 📈 Estado del Proyecto

| Característica | Estado |
|----------------|--------|
| Prototipo funcional | ✅ Completado |
| Traducción bidireccional | ✅ Completado |
| Soporte para 10 idiomas | ✅ Completado |
| Preservación de comentarios | ✅ Completado |
| Alias múltiples | ✅ Completado |
| Expansión sintáctica (macros) | 🔄 En desarrollo |
| Detección automática de idioma | 🔄 Planeado |
| Integración con IDEs | 🔄 Planeado |
| Validación sintáctica ASM | 🔄 Planeado |

## ⚠️ Limitaciones Actuales (v0.2)

Ser transparente sobre lo que **no** hace (todavía) es tan importante como mostrar lo que sí hace:

- ❌ No soporta macros complejas
- ❌ No traduce estructuras de control de alto nivel
- ❌ No detecta automáticamente el idioma del código fuente
- ❌ No valida sintaxis ASM avanzada (eso lo hace NASM)
- ❌ No traduce nombres de secciones (`.text`, `.data`)

Estas limitaciones están en el roadmap para versiones futuras.

## 🔬 Ejemplo Completo de Flujo

### Paso 1: Escribir en tu idioma
Crea `hola.masm` en Español:
```asm
; Programa: Hola Mundo
seccion .texto
global _inicio

_inicio:
    mover rax, 1        ; syscall write
    mover rdi, 1        ; stdout
    mover rsi, mensaje
    mover rdx, 12
    interrupcion 0x80
    
    mover rax, 60       ; syscall exit
    mover rdi, 0
    interrupcion 0x80

seccion .datos
    mensaje db "Hola Mundo!", 0xA
```

### Paso 2: Traducir a NASM estándar
```bash
python mlasm.py es hola.masm hola.asm
```

Salida:
```
🛡️ MultiLang-ASM v0.2
   Idioma: ES
   Modo: Estándar (NASM)
   Entrada: hola.masm
   Salida: hola.asm
   Estado: ✅ OK
```

### Paso 3: Compilar con NASM
```bash
nasm -f elf64 hola.asm -o hola.o
ld hola.o -o hola
```

### Paso 4: Ejecutar
```bash
./hola
# Salida: Hola Mundo!
```

### Bonus: Ver en otro idioma
```bash
python mlasm.py ar hola.asm hola_ar.masm --reverse
# Ahora hola_ar.masm usa mnemónicos en árabe
```

## 🤝 Contribuir

¿Quieres añadir tu idioma? ¡Perfecto!

1. Edita `mlasm.py`
2. Añade tu tabla de traducción en el diccionario `TABLE`
3. Haz un pull request
4. ¡Listo! Habrás democratizado el bajo nivel para tu comunidad

## 📄 Documentación

- [Visión y Arquitectura](VISION_Y_ARQUITECTURA.md)
- [Informe de Concepto](INFORME_DE_CONCEPTO.md)
- [Changelog](CHANGELOG.md)
- **[🌍 Documentación Multilingüe](docs/)** ← Referencias completas en 10 idiomas

### Referencias de Instrucciones por Idioma (80+ instrucciones cada uno)
- 🇪🇸 [Español](docs/INSTRUCCIONES_ES.md)
- 🇫🇷 [Français](docs/INSTRUCCIONES_FR.md)
- 🇩🇪 [Deutsch](docs/INSTRUCCIONES_DE.md)
- 🇮🇹 [Italiano](docs/INSTRUCCIONES_IT.md)
- 🇸🇦 [العربية (Arabic)](docs/INSTRUCCIONES_AR.md)
- 🇷🇺 [Русский (Russian)](docs/INSTRUCCIONES_RU.md)
- 🇰🇷 [한국어 (Korean)](docs/INSTRUCCIONES_KO.md)
- 🇮🇩 [Bahasa Indonesia](docs/INSTRUCCIONES_ID.md)
- 🇨🇳 [中文 (Traditional Chinese)](docs/INSTRUCCIONES_ZH.md)
- 🇯🇵 [日本語 (Japanese)](docs/INSTRUCCIONES_JA.md)

## ⚖️ Disclaimer Técnico

**MultiLang-ASM no reemplaza a NASM, FASM o GAS.**

Es una **capa de accesibilidad** que traduce mnemónicos nativos a ASM estándar. El archivo generado es 100% compatible con cualquier ensamblador tradicional. La CPU nunca ve la diferencia.

Piénsalo como un "preprocesador humano" que elimina la barrera del idioma sin modificar la arquitectura subyacente.

## 💭 Mensaje del Autor

**"No saber inglés no debería ser una barrera para crear. El conocimiento debe fluir en todos los idiomas."**

Si este proyecto te ayudó, compártelo. Cada persona que programa en su idioma nativo es una victoria contra las barreras artificiales en tecnología.

---

## 🤝 ¿Quieres Contribuir?

**MultiLang-ASM está abierto a colaboraciones de todo el mundo.**

No necesitas saber ensamblador: si hablas otro idioma, puedes ayudar a traducir, documentar o crear ejemplos.

**¿Cómo puedes ayudar?**
- 🌍 Añadir soporte para nuevos idiomas
- 📝 Mejorar traducciones existentes
- 📚 Crear tutoriales en tu idioma
- 🐛 Reportar bugs o sugerir mejoras
- ⭐ Dar una estrella al repo

**Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para empezar.**

Issues etiquetados con `good first issue` son perfectos para nuevos contribuidores.

---

**Versión:** v0.2  
**Licencia:** MIT  
**Autor:** J / Neuro-OS Project  
**Repositorio:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

— J

## 📜 Licencia

MIT License - Libertad total para usar, modificar y distribuir.

---

🛡️ **Este proyecto es un manifiesto. No es solo código; es una declaración de que la tecnología debe adaptarse a las personas, no al revés.**
