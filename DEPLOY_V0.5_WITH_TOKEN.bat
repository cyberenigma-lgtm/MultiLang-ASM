@echo off
set GIT_PATH="C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

echo ===========================================
echo   MULTILANG-ASM v0.5 - DEPLOY WITH TOKEN
echo ===========================================
echo.

REM 1. Configure Local Identity (Fixes 'Author identity unknown' error)
echo [CONFIG] Setting up local builder identity...
%GIT_PATH% config user.name "Neuro-OS Builder"
%GIT_PATH% config user.email "builder@neuro-os.local"

REM 2. Git Cleanup & Status
echo [STATUS] Checking repo...
%GIT_PATH% status

REM 3. Add & Commit
echo.
echo [ADD] Adding files...
%GIT_PATH% add .

echo.
echo [COMMIT] Committing v0.5...
%GIT_PATH% commit -m "feat(v0.5): MultiLang-ASM Global Release - 27 Languages, Kids Mode, Wiki v0.5"

REM 4. Token Prompt & Push
echo.
echo ===========================================
echo   AUTHENTICATION REQUIRED
echo ===========================================
echo.
set /p GITHUB_TOKEN="Pegue su GitHub Personal Access Token (ghp_...): "

echo.
echo [PUSH] Uploading to GitHub...
%GIT_PATH% push "https://%GITHUB_TOKEN%@github.com/cyberenigma-lgtm/MultiLang-ASM.git" main

echo.
echo ===========================================
echo   DEPLOYMENT COMPLETE!
echo ===========================================
pause
