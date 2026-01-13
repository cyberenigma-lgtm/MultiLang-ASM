import unittest
import sys
import os

# Add parent directory to path to import mlasm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mlasm

class TestTranslation(unittest.TestCase):
    def test_standard_instruction_remains(self):
        """Test that standard mnemonics are preserved"""
        code = "mov eax, 1"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertEqual(result.strip(), "mov eax, 1")

    def test_spanish_translation(self):
        """Test native to standard translation for Spanish"""
        code = "mover eax, 1"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertEqual(result.strip(), "mov eax, 1")

    def test_spanish_reverse_translation(self):
        """Test standard to native translation for Spanish"""
        code = "mov eax, 1"
        result = mlasm.translate(code, "es", to_standard=False)
        self.assertEqual(result.strip(), "mover eax, 1")

    def test_case_insensitivity(self):
        """Test that input case doesn't matter"""
        code = "MOVER eax, 1"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertEqual(result.strip(), "mov eax, 1")

    def test_comment_preservation(self):
        """Test that comments are kept"""
        code = "mover eax, 1 ; set eax to 1"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertIn("; set eax to 1", result)
        self.assertTrue(result.strip().startswith("mov eax, 1"))

    def test_auto_detection_es(self):
        """Test language auto-detection for Spanish"""
        code = "mover eax, 1\nsumar ebx, 2"
        detected = mlasm.detect_language(code)
        self.assertEqual(detected, "es")

    def test_auto_detection_fr(self):
        """Test language auto-detection for French"""
        code = "deplacer eax, 1\najouter ebx, 2"
        detected = mlasm.detect_language(code)
        self.assertEqual(detected, "fr")

class TestReverseMapping(unittest.TestCase):
    def test_reverse_es(self):
        """Test Standard -> Spanish (PRETTY)"""
        code = "mov eax, 1\ncall function"
        result = mlasm.translate(code, "es", to_standard=False)
        self.assertIn("mover eax, 1", result)
        self.assertIn("llamar function", result)

    def test_reverse_fr(self):
        """Test Standard -> French (PRETTY)"""
        code = "jmp label\nret"
        result = mlasm.translate(code, "fr", to_standard=False)
        self.assertIn("sauter label", result)
        self.assertIn("retourner", result)

    def test_reverse_de(self):
        """Test Standard -> German (PRETTY)"""
        code = "mov eax, 1\nadd ebx, 2"
        result = mlasm.translate(code, "de", to_standard=False)
        self.assertIn("bewegen eax, 1", result)
        self.assertIn("addieren ebx, 2", result)
    
    def test_reverse_id_consistency(self):
        """Test Standard -> Indonesian (PRETTY) consistency"""
        # Ensure 'mov' maps back to 'pindah' (or alias 'salin' -> 'mov', but reverse prefers canonical)
        # Checking mlasm.py PRETTY table for ID: "mov": "pindah"
        code = "mov eax, 1"
        result = mlasm.translate(code, "id", to_standard=False)
        self.assertIn("pindah eax, 1", result)

class TestMacros(unittest.TestCase):
    def test_simple_define(self):
        """Test %define macro replacement"""
        code = "%define VAL 10\nmov eax, VAL"
        result = mlasm.translate(code, "en", to_standard=True)
        # Should replace VAL with 10 and remove %define line
        self.assertIn("mov eax, 10", result)
        self.assertNotIn("%define", result)

    def test_macro_in_spanish(self):
        """Test macros work with native instructions"""
        code = "%define SALUDO 0x1\nmover eax, SALUDO"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertIn("mov eax, 0x1", result)

class TestDictionaryExpansion(unittest.TestCase):
    def test_spanish_synonyms(self):
        """Test new semantic variants in Spanish"""
        # agregar -> add, cargar -> mov
        code = "agregar eax, 1\ncargar ebx, 2"
        result = mlasm.translate(code, "es", to_standard=True)
        self.assertIn("add eax, 1", result)
        self.assertIn("mov ebx, 2", result)

    def test_new_languages(self):
        """Test basic existence of new languages (HI, TR, PL, SV, NL)"""
        # Turkish
        self.assertIn("mov eax, 1", mlasm.translate("taşı eax, 1", "tr"))
        # Polish
        self.assertIn("mov eax, 1", mlasm.translate("przesun eax, 1", "pl"))
        # Swedish
        self.assertIn("add eax, 1", mlasm.translate("addera eax, 1", "sv"))
        # Dutch
        self.assertIn("sub eax, 1", mlasm.translate("aftrekken eax, 1", "nl"))
        # Hindi (Transliterated)
        self.assertIn("jmp label", mlasm.translate("kudo label", "hi"))

class TestInstructionExpansion(unittest.TestCase):
    def test_missing_instructions_new_langs(self):
        """Test xor, cmp, test, lea, inc, dec for new languages"""
        
        # Turkish: xor -> ozel_veya, cmp -> karsilastir
        code_tr = "ozel_veya eax, ebx\nkarsilastir eax, 0"
        res_tr = mlasm.translate(code_tr, "tr")
        self.assertIn("xor eax, ebx", res_tr)
        self.assertIn("cmp eax, 0", res_tr)

        # Polish: inc -> zwieksz, dec -> zmniejsz
        code_pl = "zwieksz eax\nzmniejsz ebx"
        res_pl = mlasm.translate(code_pl, "pl")
        self.assertIn("inc eax", res_pl)
        self.assertIn("dec ebx", res_pl)

        # Swedish: and -> och, or -> eller
        code_sv = "och eax, ebx\neller ecx, edx"
        res_sv = mlasm.translate(code_sv, "sv")
        self.assertIn("and eax, ebx", res_sv)
        self.assertIn("or ecx, edx", res_sv)

        # Hindi: lea -> pata_load (approx), test -> pariksha
        code_hi = "pata_load eax, [ebx]\npariksha eax, eax"
        res_hi = mlasm.translate(code_hi, "hi")
        self.assertIn("lea eax, [ebx]", res_hi)
        self.assertIn("test eax, eax", res_hi)
        
        # Dutch: not -> niet, xchg -> wissel
        code_nl = "niet eax\nwissel eax, ebx"
        res_nl = mlasm.translate(code_nl, "nl")
        self.assertIn("not eax", res_nl)
        self.assertIn("xchg eax, ebx", res_nl)

if __name__ == '__main__':
    unittest.main()
