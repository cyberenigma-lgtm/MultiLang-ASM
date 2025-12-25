# 🚀 DOCUMENTO DE VISIÓN Y ARQUITECTURA — Ensamblador Multilingüe para Bajo Nivel

**Autor:** J  
**Proyecto:** Post‑Neuro‑OS — Accesibilidad Universal al Bajo Nivel  
**Estado:** Documento de Concepto (Fase 0)

## 1. Propósito del Documento
Este documento define la visión, motivación y arquitectura preliminar del primer ensamblador multilingüe orientado a accesibilidad, cuyo objetivo es permitir que cualquier persona —independientemente de su idioma— pueda programar en bajo nivel sin barreras lingüísticas.

## 2. Resumen Ejecutivo
La programación de bajo nivel ha permanecido prácticamente inalterada durante 50 años. Los mnemónicos (`mov`, `jmp`, `push`) y la documentación están en inglés, lo que excluye a millones de personas con talento.

Este proyecto propone un ensamblador que:
- Permite escribir instrucciones en cualquier idioma (español, árabe, francés, japonés…).
- Traduce automáticamente a mnemónicos estándar compatibles con NASM/FASM/GAS.
- Mantiene un núcleo universal en inglés, garantizando compatibilidad total.
- Permite visualizar el código en el idioma preferido del usuario.

## 3. Motivación
El inglés no es un requisito técnico; es una convención histórica. La CPU no entiende inglés, entiende opcodes. Eliminar la barrera lingüística democratiza el acceso, permitiendo que la creatividad sea universal.

*"No saber inglés no debería impedirte crear. La imaginación no tiene idioma."*

## 4. Arquitectura Propuesta
La arquitectura se basa en un flujo reversible y universal:

`Usuario (Idioma Nativo) -> Lexer Multilingüe -> ASM Estándar -> Compilador (NASM/FASM/GAS) -> Binario Final`

### 4.1 Componentes Clave
- **Lexer Multilingüe:** Identificación de tokens en el idioma del usuario.
- **Tabla de Traducción:** Diccionarios especializados (ej. `mover` -> `mov`).
- **Modo Reversible:** Almacenamiento en estándar, visualización en nativo.
- **Selector de Idioma:** Activación dinámica de tablas de traducción.

## 5. Ejemplo de Funcionamiento
**Entrada (Español):**
```asm
mover rax, rbx
saltar etiqueta
```

**Visualización (Árabe):**
```asm
نقل rax, rbx
اقفز etiqueta
```

**Archivo Real (NASM):**
```asm
mov rax, rbx
jmp etiqueta
```

## 6. Casos de Uso
- Estudiantes y autodidactas globales.
- Formación técnica sin prerrequisitos lingüísticos.
- Niños y educación STEAM temprana.
- Accesibilidad cognitiva.

## 7. Roadmap de Desarrollo
### Fase 1 — Fundamentos
- Definir sintaxis base en español.
- Tabla mínima de equivalencias (10–20 instrucciones).
- Prototipo de traductor simple (Python).

### Fase 2 — Motor Multilingüe
- Soporte para francés, italiano, portugués.
- Selector de idioma y modo reversible.

### Fase 3 — Expansión Global
- Soporte para árabe (RTL), chino, japonés.
- Documentación multilingüe.

### Fase 4 — Ecosistema
- Publicación Open Source.
- Plugins para VSCode/Neovim.

## 8. Visión a Largo Plazo
Convertir el ensamblador en una herramienta humana donde el bajo nivel sea accesible y la tecnología se adapte al creador, no al revés.

## 9. Cómo Usarlo
Esta sección describe el flujo básico de uso del ensamblador multilingüe. El objetivo es que cualquier persona, incluso sin experiencia previa en ensamblador o sin conocimiento de inglés, pueda comenzar a crear de inmediato.

### 9.1 Selección de Idioma
Al iniciar la herramienta, el usuario elige su idioma preferido:

```
Seleccione idioma:
1. Español
2. Inglés
3. Francés
4. Italiano
5. Árabe
6. Portugués
7. Japonés
> 1
```

El ensamblador activa automáticamente la tabla de traducción correspondiente.

### 9.2 Escritura del Código en Lenguaje Nativo
El usuario escribe instrucciones en su propio idioma, utilizando palabras naturales y mnemónicos adaptados:

**Ejemplo (Español):**
```asm
mover rax, rbx
sumar rax, 4
saltar etiqueta_fin
```

**Ejemplo (Árabe):**
```asm
نقل rax, rbx
جمع rax, 4
اقفز etiqueta_fin
```

**Ejemplo (Francés):**
```asm
deplacer rax, rbx
ajouter rax, 4
sauter etiquette_fin
```

### 9.3 Traducción Automática a ASM Estándar
El ensamblador convierte internamente cada instrucción al mnemónico estándar:

```
mover   → mov
sumar   → add
saltar  → jmp
```

El archivo generado es 100% compatible con NASM, FASM o GAS:

```asm
mov rax, rbx
add rax, 4
jmp etiqueta_fin
```

### 9.4 Compilación con Herramientas Tradicionales
El usuario compila el archivo generado igual que cualquier otro `.asm`:

```bash
nasm -f elf64 programa.asm -o programa.o
ld programa.o -o programa
```

No se requiere ninguna herramienta especial para la fase final.

### 9.5 Visualización en Otros Idiomas
Cualquier usuario puede abrir el mismo archivo y verlo en su idioma:

**Archivo estándar:**
```asm
mov rax, rbx
add rax, 4
jmp etiqueta_fin
```

**Vista en Árabe:**
```asm
نقل rax, rbx
اضف rax, 4
اقفز etiqueta_fin
```

**Vista en Español:**
```asm
mover rax, rbx
sumar rax, 4
saltar etiqueta_fin
```

**Vista en Francés:**
```asm
deplacer rax, rbx
ajouter rax, 4
sauter etiquette_fin
```

El archivo no cambia. Solo cambia la vista.

### 9.6 Flujo Completo de Uso
```
1. Seleccionar idioma
2. Escribir código en lenguaje nativo
3. El ensamblador traduce a ASM estándar
4. Compilar con NASM/FASM/GAS
5. Ejecutar el binario
6. Opcional: visualizar el código en otros idiomas
```

### 9.7 Filosofía de Uso
El ensamblador está diseñado para:
- No exigir inglés
- No exigir conocimientos previos
- No imponer sintaxis rígida
- No limitar la creatividad

Su misión es permitir que cualquier persona pueda:
- Imaginar
- Crear
- Aprender
- Experimentar

Sin barreras ficticias.

---
> [!NOTE]
> *"Este ensamblador no es solo una herramienta. Es un manifiesto."*
