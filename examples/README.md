# Examples - MultiLang-ASM

Functional code examples written with MultiLang-ASM.

**🚀 [QUICKSTART: Build a Kernel in 5 Minutes →](QUICKSTART.md)**

---

## 🚀 Kernel Mínimo en Español (50 líneas)

Un kernel básico completamente funcional escrito en **Español**.

### Archivos

- `boot.masm` - Bootloader (16 líneas)
- `kernel.masm` - Kernel (34 líneas)
- `Makefile` - Build automation

### ¿Qué hace?

1. **Bootloader** carga el kernel desde disco
2. **Kernel** muestra mensaje y captura teclas
3. **ESC** para detener

### Compilar y Ejecutar

```bash
cd examples
make run
```

Esto:
1. Traduce español → NASM
2. Compila con NASM
3. Crea imagen de disco
4. Ejecuta en QEMU

---

## 🇨🇳 Kernel Mínimo en Chino (中文核心)

**¡Demostración de lenguaje NO latino!**

El mismo kernel funcional escrito completamente en **Chino Tradicional** (繁體中文).

### Archivos

- `boot_zh.masm` - 啟動載入程式 (Bootloader)
- `kernel_zh.masm` - 核心 (Kernel)
- `Makefile.zh` - 建置自動化

### ¿Qué demuestra?

✅ **Scripts no latinos funcionan perfectamente**  
✅ **Caracteres Unicode/multibyte no son problema**  
✅ **Concepto verdaderamente universal**  
✅ **No solo para idiomas "occidentales"**

### Instrucciones Chinas Usadas

| 中文 | Español | NASM |
|------|---------|------|
| 移動 | mover | mov |
| 跳躍 | saltar | jmp |
| 呼叫 | llamar | call |
| 返回 | retornar | ret |
| 若相等 | si_igual | je |
| 中斷 | interrupcion | int |
| 推 入 | meter | push |
| 彈出 | sacar | pop |

### Compilar y Ejecutar

```bash
cd examples
make -f Makefile.zh run
```

**Resultado:**
```
========================================
   多語言核心 v0.1
   使用 MultiLang-ASM 建立
========================================

中文核心正在運作！
按鍵可見回顯...
ESC 停止系統。

> 
```

---

## 📊 Estadísticas Combinadas

| Métrica | Español | 中文 |
|---------|---------|------|
| Líneas de código | 50 | 50 |
| Idioma | 100% Español | 100% 中文 |
| Instrucciones usadas | 11 diferentes | 11 diferentes |
| Tamaño final | 5.5 KB | 5.5 KB |
| **Funcionalidad** | **Idéntica** | **Idéntica** |

---

## 🎯 Instrucciones Españolas Usadas

- `mover` (mov)
- `saltar` (jmp)
- `llamar` (call)
- `retornar` (ret)
- `comparar` (cmp)
- `si_igual` (je)
- `meter` (push)
- `sacar` (pop)
- `interrupcion` (int)
- `detener` (hlt)
- `cargar_byte` (lodsb)

---

## 🔍 Ver Código Traducido

```bash
# Español
make debug

# 中文
make -f Makefile.zh debug
```

Muestra el código NASM generado.

---

## 🧪 Pruebas

**En QEMU:**
- Presiona teclas → Verás echo
- Presiona ESC → Sistema se detiene

**Funciona igual en ambos idiomas.**

---

## 🌍 Mensaje

**MultiLang-ASM no discrimina entre scripts:**
- ✅ Latino (Español, Francés, Alemán)
- ✅ Cirílico (Ruso)
- ✅ Árabe (العربية)
- ✅ CJK (中文, 日本語, 한국어)

**Todos generan el mismo código máquina.**  
**Todos funcionan perfectamente.**

---

## 📚 Documentación Completa

Ver `KERNEL-EXAMPLE.md` en la raíz del proyecto para tutorial completo.

---

**Creado con MultiLang-ASM v0.3** 🛡️
