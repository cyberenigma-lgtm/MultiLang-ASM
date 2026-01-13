@echo off
color 0A
cls
echo ==========================================================
echo    MultiLang-ASM: DEPLOYMENT SYSTEM (v0.4)
echo ==========================================================
echo.
echo  [INFO] Preparing to deploy Version 0.4.
echo  [CONTENT] 16 Languages, Macros, Auto-Detect, Docs, Examples.
echo.
echo  [NOTE] If git authentication is required, have your Token ready.
echo.
rem pause

set BASH_PATH="C:\msys64\usr\bin\bash.exe"
set REPO_PATH="/c/Users/cyber/OneDrive/Documentos/NeuroOs/Neuro-OS-Genesis/MultiLang-ASM"

echo.
echo [1/3] Staging all files...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git add ."

echo.
echo [2/3] Committing changes...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git commit -m 'Release v0.4: 16 Languages, Macros, Auto-Detect, Comprehensive Documentation' --allow-empty"

echo.
echo [3/3] Pushing to GitHub (origin main)...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git push origin main"

echo.
echo ==========================================================
echo    DEPLOYMENT FINISHED
echo ==========================================================
echo.
rem pause
