import os
import importlib.util

def test_language_integrity():
    langs_dir = "langs"
    essential_mnemonics = ["mov", "add", "sub", "jmp", "call", "ret", "int", "syscall"]
    
    files = [f for f in os.listdir(langs_dir) if f.endswith(".py") and f != "__init__.py"]
    print(f"🔍 Auditoría de Integridad Babel v0.7... ({len(files)} idiomas)")
    print("-" * 50)
    
    passed = 0
    failed = 0
    
    for f in files:
        lang_code = f[:-3]
        filepath = os.path.join(langs_dir, f)
        
        spec = importlib.util.spec_from_file_location(lang_code, filepath)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            
            if not hasattr(module, "KEYWORDS"):
                print(f"❌ {lang_code}: Falta diccionario KEYWORDS")
                failed += 1
                continue
                
            # Verificar paridad técnica (mnemónicos NASM presentes)
            available_mnemonics = set(module.KEYWORDS.values())
            missing = [m for m in essential_mnemonics if m not in available_mnemonics]
            
            if missing:
                print(f"⚠️ {lang_code}: Parcial (Faltan: {', '.join(missing)})")
            else:
                print(f"✅ {lang_code}: Integridad verificada ({len(module.KEYWORDS)} comandos)")
                passed += 1
                
        except Exception as e:
            print(f"❌ {lang_code}: Error en carga - {str(e)}")
            failed += 1
            
    print("-" * 50)
    print(f"Resumen: {passed} OK, {failed} ERR")

if __name__ == "__main__":
    test_language_integrity()
