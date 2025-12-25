# Examples - MultiLang-ASM

Ejemplos funcionales de código escrito con MultiLang-ASM.

---

## 🚀 Kernel Mínimo (50 líneas)

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

## 📊 Estadísticas

| Métrica | Valor |
|---------|-------|
| Líneas de código | 50 |
| Idioma | 100% Español |
| Instrucciones usadas | 11 diferentes |
| Tamaño final | 5.5 KB |

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
make debug
```

Muestra el código NASM generado.

---

## 🧪 Pruebas

**En QEMU:**
- Presiona teclas → Verás echo
- Presiona ESC → Sistema se detiene

**En hardware real (USB):**
```bash
# ⚠️ PELIGRO: Esto sobrescribe el dispositivo USB
sudo dd if=kernel.img of=/dev/sdX bs=512
```

---

## 📚 Documentación Completa

Ver `KERNEL-EXAMPLE.md` en la raíz del proyecto para tutorial completo.

---

**Creado con MultiLang-ASM v0.3** 🛡️
