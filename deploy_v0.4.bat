@echo off
color 0A
cls
echo ==========================================================
echo    MultiLang-ASM: DEPLOYMENT SYSTEM (v0.4) - SECURE MODE
echo ==========================================================
echo.
echo  [SECURE INPUT]
echo  Please paste your GitHub Personal Access Token (ghp_...)
echo  and press ENTER.
echo.
set /p TOKEN=">> PASTE TOKEN HERE: "

if "%TOKEN%"=="" (
    echo [ERROR] Token cannot be empty.
    pause
    exit /b
)

set BASH_PATH="C:\msys64\usr\bin\bash.exe"
set REPO_PATH="/c/Users/cyber/OneDrive/Documentos/NeuroOs/Neuro-OS-Genesis/MultiLang-ASM"
set REMOTE_URL="https://%TOKEN%@github.com/cyberenigma-lgtm/MultiLang-ASM.git"

echo.
echo [1/4] Configuring Remote Credentials...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git remote set-url origin %REMOTE_URL%"

echo.
echo [2/4] Staging files...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git add ."

echo.
echo [3/4] Committing v0.4 Release...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git commit -m 'Release v0.4: 16 Languages, Macros, Auto-Detect, Comprehensive Documentation' --allow-empty"

echo.
echo [4/4] Pushing to GitHub (origin main)...
%BASH_PATH% -l -c "cd '%REPO_PATH%' && git push origin main"

echo.
echo ==========================================================
echo    DEPLOYMENT FINISHED
echo ==========================================================
echo.
pause
