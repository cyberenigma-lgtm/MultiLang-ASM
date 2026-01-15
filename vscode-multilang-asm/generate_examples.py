import os

# Define the examples data manually to ensure it matches the TS implementation
EXAMPLES = {
    "es": {"dir": "Spanish", "code": "pon rax a 5\npon rbx a 10\nsuma rax con rbx\nenseña rax"},
    "en": {"dir": "English", "code": "put rax 5\nput rbx 10\nadd rax and rbx\nlook rax"},
    "fr": {"dir": "French", "code": "mets rax a 5\nmets rbx a 10\najoute rax avec rbx\nmontre rax"},
    "de": {"dir": "German", "code": "setze rax auf 5\nsetze rbx auf 10\naddiere rax mit rbx\nzeige rax"},
    "it": {"dir": "Italian", "code": "metti rax a 5\nmetti rbx a 10\naggiungi rax con rbx\nmostra rax"},
    "pt": {"dir": "Portuguese", "code": "coloca rax a 5\ncoloca rbx a 10\nsoma rax com rbx\nmostra rax"},
    "ru": {"dir": "Russian", "code": "положи rax 5\nположи rbx 10\nдобавь rax с rbx\nпокажи rax"},
    "ja": {"dir": "Japanese", "code": "irete rax 5\nirete rbx 10\ntashite rax rbx\nmisete rax"},
    "zh": {"dir": "Chinese", "code": "fang rax 5\nfang rbx 10\njia rax rbx\nkan rax"},
    "ar": {"dir": "Arabic", "code": "da rax 5\nda rbx 10\nijma rax rbx\nanzur rax"},
    "ko": {"dir": "Korean", "code": "neoh rax 5\nneoh rbx 10\ndeohae rax rbx\nboyeo rax"},
    "hi": {"dir": "Hindi", "code": "rakho rax 5\nrakho rbx 10\njodo rax rbx\ndikhao rax"},
    "tr": {"dir": "Turkish", "code": "koy rax 5\nkoy rbx 10\nekle rax rbx\ngoster rax"},
    "pl": {"dir": "Polish", "code": "wsadz rax 5\nwsadz rbx 10\ndodaj rax rbx\npokaz rax"},
    "sv": {"dir": "Swedish", "code": "stall rax 5\nstall rbx 10\naddera rax med rbx\nvisa rax"},
    "nl": {"dir": "Dutch", "code": "zet rax op 5\nzet rbx op 10\ntel_op rax met rbx\ntoon rax"},
    "el": {"dir": "Greek", "code": "bale rax 5\nbale rbx 10\nprosthese rax rbx\ndiekse rax"},
    "he": {"dir": "Hebrew", "code": "sim rax 5\nsim rbx 10\nhosef rax rbx\nhare rax"},
    "th": {"dir": "Thai", "code": "sai rax 5\nsai rbx 10\nbuak rax rbx\nsadang rax"},
    "vi": {"dir": "Vietnamese", "code": "dat rax 5\ndat rbx 10\nthem rax rbx\nhien rax"},
    "sw": {"dir": "Swahili", "code": "weka rax 5\nweka rbx 10\nongeza rax rbx\nonyesha rax"},
    "tl": {"dir": "Tagalog", "code": "lagay rax 5\nlagay rbx 10\ndagdag rax rbx\npakita rax"},
    "ms": {"dir": "Malay", "code": "letak rax 5\nletak rbx 10\ntambah rax rbx\ntunjuk rax"},
    "fa": {"dir": "Persian", "code": "bezor rax 5\nbezor rbx 10\njam rax rbx\nneshon rax"},
    "uk": {"dir": "Ukrainian", "code": "polozhy rax 5\npolozhy rbx 10\ndodaty rax rbx\npokazhy rax"},
    "ro": {"dir": "Romanian", "code": "pune rax 5\npune rbx 10\nadauga rax rbx\narata rax"},
    "id": {"dir": "Indonesian", "code": "taruh rax 5\ntaruh rbx 10\ntambah rax rbx\ntampil rax"}
}

BASE_DIR = "examples"

if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

for lang, data in EXAMPLES.items():
    lang_dir = os.path.join(BASE_DIR, f"{data['dir']}_{lang.upper()}")
    if not os.path.exists(lang_dir):
        os.makedirs(lang_dir)
    
    file_path = os.path.join(lang_dir, "hello_world.masm")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"; MultiLang-ASM - {data['dir']} Example\n")
        f.write("; Kids Mode / Modo Niños\n\n")
        f.write(data['code'])
    
    # Generate README for the language
    readme_path = os.path.join(lang_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# MultiLang-ASM: {data['dir']} ({lang.upper()})\n\n")
        f.write(f"This directory contains examples for **{data['dir']}**.\n\n")
        f.write("## Hello World\n")
        f.write("```masm\n")
        f.write(data['code'] + "\n")
        f.write("```\n\n")
        f.write("## Usage\n")
        f.write("Open `.masm` files in VSCode with the MultiLang-ASM extension installed.\n")

    print(f"Generated: {file_path} and README.md")

print("All examples and documentation generated!")
