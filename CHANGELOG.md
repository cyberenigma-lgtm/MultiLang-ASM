# 📋 MultiLang-ASM: Changelog

## v1.0.0 - "Sovereign UPL+ Edition: 100% C99 & 150 Languages" (2026-10-17)

### 🚀 Revolución Arquitectónica: Motor Nativo ANSI C99
- **Cero Dependencias de Runtime**: MultiLang-ASM pasa de ser un prototipo en Python a un **motor nativo ultraligero y autónomo en ANSI C99** (`src/mlasm_core.c` y `src/masm_tables.h`).
- **Rendimiento Instantáneo**: Compilación y transpilación en <2 milisegundos con cero sobrecarga de intérprete.
- **Portabilidad Universal UPL**: Compatible con cualquier compilador estándar C99 (`gcc`, `clang`, `tcc`, `msvc`) en Windows, Linux, macOS, BSD o bare-metal.

### 🌍 Expansión Global a 150 Lenguas del Mundo
- **Cobertura Planetaria**: Expansión desde 57 a **150 idiomas oficiales** cubriendo los 5 continentes (Europa, América, África, Asia y Oceanía), incluyendo lenguas clásicas e indígenas (Latín, Esperanto, Guaraní, Náhuatl, Quechua, Suajili, Cheroqui, Inuktitut, Navajo, etc.).
- **200+ Instrucciones x86_64 Canónicas**: Soporte exhaustivo para transferencia de datos, aritmética, lógica, bits, cadenas, bucles, llamadas al sistema, tablas de descriptores (GDT/IDT/LDT) y operaciones FPU/x87.

### ✨ Nuevas Características de la Línea de Comandos
- **Preprocesador de Macros Nativo**: Soporte directo en C para directivas `%define`.
- **Detección Automática de Idioma**: Algoritmo de frecuencia léxica instantáneo (`mlasm auto archivo.masm`).
- **Modo Reversible Bidireccional**: Visualización de código NASM estándar en cualquiera de las 150 lenguas (`mlasm --reverse <lang> archivo.asm`).
- **Pipeline de Construcción Directa**: Compilación de `.masm` a ejecutable binario en un solo comando (`mlasm --build <lang> archivo.masm`).
- **Suite de Pruebas Integrada**: Suite nativa de validación ejecutable con `mlasm --test` o `test.bat`/`test.sh`.

---

## v0.7 - "Babel Edition - Global Expansion" (2026-02-12)

### ✨ Nuevas Características
- **Expansión Global Masiva**: Soporte para **56 variantes lingüísticas** totales.
- **Cobertura Regional**: Implementación de lenguas de Europa (Catalán, Noruego, Gallego, Euskera, Irlandés, Ucraniano, Finlandés, Rumano), América (Quechua, Aymara, Náhuatl, Maya), África (Hausa, Yoruba, Igbo, Zulú, Afrikaans, Amárico, Akan) y Asia/Oceanía (Tagalo, Persa, Malayo, Bengalí, Tamil, Telugu, Javanés, Sundanés, Maorí, Tok Pisin, Cantonés).
- **Listado Maestro de Países**: Nuevo documento `LISTA_PAISES_LENGUAS.md` para referencia geográfica.
- **Suite de Manuales Localizados**: Generación de 50+ archivos `INSTRUCCIONES_<LANG>.md` con documentación técnica per-idioma.
- **Wiki de Soporte Avanzado**: Guías de Troubleshooting y funcionamiento técnico del motor.
- **Localización del Motor**: Mensajes de error y ayuda extendidos a más idiomas.

### 🔧 Mejoras Técnicas
- **Autodetección Optimizada**: Mejor detección de idiomas regionales basada en léxico técnico.
- **Mapeo de Instrucciones**: Paridad técnica total con 80+ instrucciones x86_64 en todos los nuevos paquetes.
- **Saneamiento de Privacidad**: Eliminación de metadatos internos en la documentación pública.

---

## v0.6 - "Babel Community" (2026-01-15)

### ✨ Nuevas Características
- **Arquitectura Modular**: Soporte para paquetes de idioma externos en `langs/`.
- **CLI de Contribuidores**: Comandos `--list-langs` y `--new-lang` para facilitar la expansión comunitaria.
- **Gobernanza**: Adición de Código de Conducta, Visión Comunitaria y Política de Seguridad.

---

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
