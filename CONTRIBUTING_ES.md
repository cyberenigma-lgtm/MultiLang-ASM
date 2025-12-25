# 🤝 Contribuir a MultiLang-ASM

📖 **[English](CONTRIBUTING.md)** | **Español**

---

¡Gracias por tu interés en contribuir a MultiLang-ASM! Este proyecto busca democratizar la programación de bajo nivel eliminando barreras lingüísticas.

## 🌍 Formas de Contribuir

### 1. Añadir un Nuevo Idioma

**Lo que necesitas:**
- Ser hablante nativo o tener dominio avanzado del idioma
- Conocer términos naturales de programación en ese idioma
- 30-60 minutos de tiempo

**Pasos:**

1. Fork el repositorio
2. Edita `mlasm.py` y añade tu idioma a la tabla `TABLE`:

```python
TABLE["tu_codigo"] = {
    # Movimiento
    "palabra_nativa": "mov",
    "otra_palabra": "add",
    # ... continuar con 80+ instrucciones
}
```

3. Crea la documentación en `docs/INSTRUCCIONES_TU.md` siguiendo el formato de los existentes
4. Actualiza `docs/README.md` para incluir tu idioma
5. Crea un pull request

**Idiomas que necesitamos:**
- 🇵🇹 Português
- 🇹🇷 Türkçe
- 🇵🇱 Polski
- 🇻🇳 Tiếng Việt
- 🇹🇭 ไทย
- 🇬🇷 Ελληνικά
- Y más...

---

### 2. Mejorar Traducciones Existentes

Si eres hablante nativo de un idioma soportado y encuentras que algunos términos podrían ser más naturales:

1. Abre un issue describiendo la mejora
2. Propón el término alternativo y por qué suena más natural
3. Haz un pull request con el cambio

**Principio:** Naturalidad > Literalidad

---

### 3. Expandir Documentación

- Tutoriales en tu idioma
- Ejemplos de proyectos reales
- Casos de uso específicos
- Videos explicativos

---

### 4. Reportar Bugs

**Formato del issue:**
```markdown
## Descripción
[Describe el problema]

## Pasos para reproducir
1. ...
2. ...

## Comportamiento esperado
[Qué debería pasar]

## Comportamiento actual
[Qué pasa realmente]

## Entorno
- OS: [Windows/Linux/macOS]
- Python: [versión]
- MultiLang-ASM: [versión]
```

---

### 5. Solicitar Funcionalidades

Abre un issue con la etiqueta `enhancement` describiendo:
- Qué funcionalidad quieres
- Por qué es útil
- Ejemplos de uso

---

## 📋 Guías de Estilo

### Código Python

```python
# Usar nombres descriptivos
def translate_token(token, lang):  # ✅
def tt(t, l):  # ❌

# Documentar funciones complejas
def foo():
    """Explica qué hace la función"""
    pass

# Seguir PEP 8 (pero no obsesionarse)
```

### Documentación Markdown

- Usa emojis para secciones (mejora scannability)
- Incluye ejemplos de código funcionales
- Enlaza a otros documentos cuando sea relevante
- Mantén líneas de 80 columnas cuando sea posible

### Traducciones

**Principios:**
1. **Naturalidad sobre Literalidad** - Usa términos que suenen naturales, no traducciones palabra por palabra
2. **Claridad sobre Brevedad** - `comparar` es mejor que `comp`
3. **Consistencia** - Si usas infinitivos verbales, manténlo en todo el idioma
4. **Compatibilidad** - Las instrucciones en inglés siempre deben seguir funcionando

---

## 🔄 Proceso de Pull Request

1. **Fork** el repositorio
2. **Crea una rama** para tu contribución:
   ```bash
   git checkout -b feat/añadir-portugues
   ```
3. **Haz tus cambios** siguiendo las guías de estilo
4. **Prueba** que todo funciona:
   ```bash
   python mlasm.py tu_idioma demo.masm demo.asm
   ```
5. **Commit** con mensaje descriptivo:
   ```bash
   git commit -m "feat: añadir soporte para Português"
   ```
6. **Push** a tu fork:
   ```bash
   git push origin feat/añadir-portugues
   ```
7. **Abre un Pull Request** en GitHub

---

## ✅ Checklist para Nuevos Idiomas

- [ ] Añadido a `TABLE` en `mlasm.py`
- [ ] Creado `docs/INSTRUCCIONES_XX.md`
- [ ] Actualizado `docs/README.md`
- [ ] Actualizado `README.md` principal
- [ ] Probado con al menos 3 ejemplos diferentes
- [ ] Verificado que instrucciones en inglés siguen funcionando

---

## 🎯 Prioridades Actuales

**Alta prioridad:**
- Expansión de `PRETTY` para todos los idiomas (modo reversible)
- Más idiomas en `TABLE`
- Ejemplos de proyectos reales

**Media prioridad:**
- Tests automatizados
- Plugin VSCode
- Detección automática de idioma

**Baja prioridad:**
- Soporte para arquitecturas ARM
- Modo interactivo

---

## 💬 Comunicación

- **Issues:** Para bugs, features, preguntas
- **Discussions:** Para ideas, debates largos
- **Pull Requests:** Para contribuciones de código

---

## 📜 Código de Conducta

**Regla de oro:** Trata a los demás como quieres ser tratado.

Específicamente:
- ✅ Sé respetuoso con todos los contribuidores
- ✅ Acepta críticas constructivas
- ✅ Enfócate en lo mejor para el proyecto
- ❌ No toleramos discriminación de ningún tipo
- ❌ No toleramos comportamiento hostil

---

## 🙏 Reconocimientos

Todos los contribuidores serán listados en:
- `README.md` (sección Contributors)
- Notas de lanzamiento de cada versión
- Documentación del idioma que añadan

---

## 📞 ¿Preguntas?

Abre un issue con la etiqueta `question` o inicia una Discussion.

---

**Gracias por ayudar a democratizar la programación de bajo nivel.** 🛡️✨

---

**MultiLang-ASM** - Parte del ecosistema Neuro-OS  
https://github.com/cyberenigma-lgtm/MultiLang-ASM
