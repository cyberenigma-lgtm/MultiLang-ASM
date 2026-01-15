
import os
import sys

# Import mlasm to use its translation engine
sys.path.append(os.getcwd())
try:
    import mlasm
except ImportError:
    print("Error: Could not import mlasm.py")
    sys.exit(1)

# Standard Hello World (simplified for demonstration)
STANDARD_HELLO = """
; Hello World in MultiLang-ASM
section .text
global _start

_start:
    ; Write(1, msg, 13)
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, 13
    syscall

    ; Exit(0)
    mov rax, 60
    mov rdi, 0
    syscall

section .data
    msg db "Hello World!", 0xA
"""

# Language Names map (using same keys as mlasm.TABLE)
LANGUAGES = [
    "es", "fr", "de", "it", "pt", 
    "ru", "ja", "zh", "ko", "ar", 
    "id", "hi", "tr", "pl", "sv", "nl"
]

def generate_examples():
    print("Generating Example Files in 'examples/'...")
    
    if not os.path.exists("examples"):
        os.makedirs("examples")

    for lang in LANGUAGES:
        print(f"Generating hello_{lang}.masm...")
        
        try:
            # Reverse translate standard ASM to Native Language
            native_code = mlasm.translate(STANDARD_HELLO, lang, to_standard=False)
            
            # Add a header comment in the file
            header = f"; MultiLang-ASM Example ({lang})\n; Run with: python ../mlasm.py auto hello_{lang}.masm\n"
            
            filename = f"examples/hello_{lang}.masm"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(header + native_code)
                
        except Exception as e:
            print(f"Error generating {lang}: {e}")

    print("Done! 16 examples generated.")

if __name__ == "__main__":
    generate_examples()
