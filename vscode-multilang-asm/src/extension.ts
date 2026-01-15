import * as vscode from 'vscode';
import { INSTRUCTIONS, KIDS_INSTRUCTIONS, SystemInstruction } from './instructions';

export function activate(context: vscode.ExtensionContext) {
    console.log('MultiLang-ASM extension is now active!');

    // Register autocomplete provider
    const provider = vscode.languages.registerCompletionItemProvider('masm', {
        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {
            const completions: vscode.CompletionItem[] = [];

            // Get configuration
            const config = vscode.workspace.getConfiguration('multilangasm');
            const defaultLang = config.get<string>('defaultLanguage', 'es');
            const kidsMode = config.get<boolean>('enableKidsMode', false);
            const autoDetect = config.get<boolean>('autoDetect', true);

            // Determine effective language
            // TODO: Implement actual auto-detect logic from document content if needed
            // For now, respect the configuration
            const lang = defaultLang;

            // Get Instructions
            let validInstructions: SystemInstruction[] = [];

            if (kidsMode) {
                // Try to find kids instructions for the language
                if (KIDS_INSTRUCTIONS[lang]) {
                    validInstructions = KIDS_INSTRUCTIONS[lang];
                } else {
                    // Fallback to Spanish kids mode if not available for language? 
                    // Or fallback to standard instructions?
                    // Let's fallback to standard for safety, but maybe show a warning?
                    // For now, just load standard.
                    const instrMap = INSTRUCTIONS[lang] || INSTRUCTIONS['es'];
                    validInstructions = Object.values(instrMap);
                }
            } else {
                const instrMap = INSTRUCTIONS[lang] || INSTRUCTIONS['es']; // Default to ES if invalid
                validInstructions = Object.values(instrMap);
            }

            // Create completion items
            validInstructions.forEach(instr => {
                const item = new vscode.CompletionItem(instr.name, vscode.CompletionItemKind.Keyword);
                item.detail = instr.description;
                item.documentation = new vscode.MarkdownString(`**Standard:** \`${instr.standard}\`\n\n${instr.description}`);
                item.insertText = new vscode.SnippetString(instr.snippet);
                completions.push(item);
            });

            // Add standard registers (x86-64)
            const registers = [
                'rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rbp', 'rsp',
                'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
                'eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'ebp', 'esp',
                'ax', 'bx', 'cx', 'dx', 'si', 'di', 'bp', 'sp',
                'al', 'bl', 'cl', 'dl'
            ];

            registers.forEach(reg => {
                const item = new vscode.CompletionItem(reg, vscode.CompletionItemKind.Variable);
                item.detail = 'Register (x86_64)';
                completions.push(item);
            });

            return completions;
        }
    });

    context.subscriptions.push(provider);

    // Register hover provider
    const hoverProvider = vscode.languages.registerHoverProvider('masm', {
        provideHover(document, position, token) {
            const range = document.getWordRangeAtPosition(position);
            const word = document.getText(range).toLowerCase();

            // Get configuration
            const config = vscode.workspace.getConfiguration('multilangasm');
            const defaultLang = config.get<string>('defaultLanguage', 'es');
            const kidsMode = config.get<boolean>('enableKidsMode', false);

            let instruction: SystemInstruction | undefined;

            if (kidsMode) {
                if (KIDS_INSTRUCTIONS[defaultLang]) {
                    instruction = KIDS_INSTRUCTIONS[defaultLang].find(i => i.name === word);
                }
            }

            // If not found in kids mode (or not active), look in standard
            if (!instruction) {
                const instrMap = INSTRUCTIONS[defaultLang];
                if (instrMap && instrMap[word]) {
                    instruction = instrMap[word];
                }
            }

            // Also check 'en' (standard asm) as fallback or cross-reference?
            // If user types 'mov' in Spanish mode, maybe we should show it?
            if (!instruction && INSTRUCTIONS['en'][word]) {
                instruction = INSTRUCTIONS['en'][word];
            }

            if (instruction) {
                const contents = new vscode.MarkdownString();
                contents.appendCodeblock(`${instruction.name} ${instruction.standard !== instruction.name ? '(' + instruction.standard + ')' : ''}`, 'masm');
                contents.appendMarkdown(`**${instruction.description}**\n\n`);

                if (kidsMode && instruction.description.includes('🧸')) {
                    contents.appendMarkdown(`\n\n_Modo Niños Activo_ 🎈`);
                }

                return new vscode.Hover(contents);
            }
        }
    });

    context.subscriptions.push(hoverProvider);
}

export function deactivate() { }
