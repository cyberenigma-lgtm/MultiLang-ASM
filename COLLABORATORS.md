# 🤝 Guía para Añadir Colaboradores

## Opciones de Colaboración en MultiLang-ASM

### 1. Colaboradores Directos (Repository Collaborators)

**Para añadir colaboradores con acceso de escritura:**

1. Ve a: https://github.com/cyberenigma-lgtm/MultiLang-ASM/settings/access
2. Click en "Add people"
3. Busca por username de GitHub
4. Selecciona el nivel de permisos:
   - **Write:** Puede hacer push directamente
   - **Maintain:** Write + gestión de issues/PRs
   - **Admin:** Control total

**Colaboradores recomendados:**
- Hablantes nativos de cada idioma soportado
- Expertos en ensamblador x86_64
- Mantenedores de documentación

---

### 2. Contribuidores via Pull Requests (Recomendado)

**Cualquier persona puede contribuir sin necesidad de permisos especiales:**

1. Fork el repositorio
2. Clonar su fork
3. Crear rama para su feature
4. Hacer cambios
5. Abrir Pull Request

**Ventajas:**
- No requiere permisos especiales
- Code review automático
- Historial claro de cambios
- Tests automáticos (GitHub Actions)

---

### 3. Mantenedores por Idioma

**Configuración recomendada:**

Asignar un mantenedor nativo para cada idioma:

| Idioma | Código | Mantenedor Actual | Buscando |
|--------|--------|-------------------|----------|
| Español | es | @cyberenigma-lgtm | - |
| Français | fr | - | ✅ |
| Deutsch | de | - | ✅ |
| Italiano | it | - | ✅ |
| العربية | ar | - | ✅ |
| Русский | ru | - | ✅ |
| 한국어 | ko | - | ✅ |
| Bahasa | id | - | ✅ |
| 中文 | zh | - | ✅ |
| 日本語 | ja | - | ✅ |

**Responsabilidades del mantenedor de idioma:**
- Revisar traducciones propuestas
- Asegurar naturalidad del lenguaje
- Actualizar documentación en su idioma
- Reportar inconsistencias

---

### 4. CODEOWNERS Configurado

El archivo `.github/CODEOWNERS` ya está configurado:

```
/mlasm.py @cyberenigma-lgtm
/docs/INSTRUCCIONES_ES.md @cyberenigma-lgtm
/docs/INSTRUCCIONES_FR.md @mantenedor-fr
...
```

**Funcionamiento:**
- PRs que modifican archivos específicos requieren aprobación del CODEOWNER
- Asegura que expertos revisen cambios críticos
- Automático: GitHub asigna revisores

**Para actualizar:**
1. Editar `.github/CODEOWNERS`
2. Añadir `@username` junto al archivo que mantienen
3. Commit y push

---

### 5. GitHub Teams (Para organizaciones más grandes)

Si el proyecto crece, se pueden crear equipos:

**Equipos sugeridos:**
- `@multilang-asm/core` - Mantenedores principales
- `@multilang-asm/lang-es` - Mantenedores español
- `@multilang-asm/lang-fr` - Mantenedores francés
- `@multilang-asm/docs` - Documentación

**Configuración:**
1. Crear organización GitHub
2. Transferir repositorio a la organización
3. Crear teams
4. Asignar permisos por team

---

### 6. Configuración Actual de Permisos

**Branch Protection (Main):**
- ✅ Require pull request antes de merge
- ✅ Require al menos 1 aprobación
- ✅ Require status checks (tests automáticos)
- ✅ No permitir force push
- ✅ Requiere branches actualizados

**Para configurar:**
1. Settings → Branches
2. "Add rule" para branch `main`
3. Marcar opciones de protección

---

### 7. Proceso de Onboarding para Nuevos Colaboradores

**Checklist para nuevo colaborador:**

```markdown
- [ ] Presentación en Discussions
- [ ] Leer CONTRIBUTING.md
- [ ] Configurar entorno local
- [ ] Hacer primer PR pequeño (typo, documentación)
- [ ] Si es mantenedor de idioma: revisar traducciones existentes
- [ ] Añadir a CODEOWNERS (si aplica)
```

---

### 8. Automatizaciones Configuradas

**GitHub Actions ya configurados:**

✅ **Test Workflow** (`.github/workflows/test.yml`)
- Prueba traducciones en múltiples OS
- Ejecuta en cada PR y push
- Verifica Python 3.7-3.11

**Para añadir más workflows:**
- Crear archivo en `.github/workflows/`
- YAML con triggers y jobs
- Se ejecuta automáticamente

---

### 9. Cómo Buscar Colaboradores

**Estrategias:**

1. **Issues "good first issue"**
   - Etiquetar issues simples
   - Atraen nuevos contribuidores

2. **Anunciar en comunidades:**
   - Reddit: r/programming, r/assembly
   - Twitter/X con hashtags relevantes
   - Foros de idiomas específicos

3. **Documentar necesidades:**
   - Crear issue: "Looking for [Language] native speakers"
   - Listar en README: "Help Wanted"

---

### 10. Comandos Útiles para Colaboración

**Para colaboradores sin permisos directos:**
```bash
# Fork el repo en GitHub primero, luego:
git clone https://github.com/TUUSUARIO/MultiLang-ASM.git
cd MultiLang-ASM
git remote add upstream https://github.com/cyberenigma-lgtm/MultiLang-ASM.git

# Crear rama para feature
git checkout -b feat/add-portuguese

# Hacer cambios...

# Push a tu fork
git push origin feat/add-portuguese

# Abrir PR desde GitHub web
```

**Para colaboradores con acceso directo:**
```bash
git clone https://github.com/cyberenigma-lgtm/MultiLang-ASM.git
git checkout -b feat/nueva-feature
# Cambios...
git push origin feat/nueva-feature
# Crear PR en GitHub
```

---

## 📞 Contacto para Colaboración

**Para convertirte en colaborador:**
1. Abre un issue describiendo cómo quieres contribuir
2. Menciona tu experiencia (idioma nativo, expertise técnico)
3. Propón algunas mejoras iniciales

**Email:** [tu email o info de contacto]

---

**Última actualización:** 2025-12-25  
**Versión:** v0.2
