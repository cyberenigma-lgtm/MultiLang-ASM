# Arquitectura Nativa ANSI C99 & Integración UPL+

MultiLang-ASM v1.0.0 abandona la sobrecarga de intérpretes para convertirse en un componente de infraestructura de bajo nivel.

---

## 🏛️ Diseño del Motor C99

```
[ Código Fuente .masm ]
          │
          ▼
┌──────────────────────────────────────────────┐
│  Motor Nativo MultiLang-ASM (mlasm_core.c)   │
│  - Preprocesador de Macros (%define)         │
│  - Detector Automático de Idioma             │
│  - Tablas Monolíticas Constantes (C99)       │
│  - Diccionario de 150 Idiomas (masm_tables.h)│
└──────────────────────────────────────────────┘
          │
          ▼
[ Código Ensamblador Estándar (.asm) ]
          │
          ▼
[ NASM / FASM / GAS ] ──► [ Objeto .o ] ──► [ Enlazador GCC / LD ] ──► [ Ejecutable .exe / Kernel .bin ]
```

### Características Técnicas
1. **Zero Heap Allocation durante la traducción**: La mayoría de las líneas se procesan en buffers estáticos de pila, eliminando problemas de fragmentación de memoria.
2. **Tablas Constantes en Memoria de Solo Lectura (.rodata)**: Las tablas de 150 idiomas están compiladas directamente en el segmento de código, lo que permite que el sistema operativo comparta páginas de memoria entre múltiples procesos.
3. **Latencia < 2 ms**: La transpilación de programas de ensamblador completos toma menos de 2 milisegundos.
4. **Independiente de Runtime**: No requiere libc compleja, ni Python, ni Node, ni Rust. Se ejecuta directamente en cualquier entorno POSIX o Win32.
