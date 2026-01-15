@echo off
set GIT_PATH="C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

echo ===========================================
echo   MULTILANG-ASM v0.5 - REPO UPDATER
echo ===========================================
echo.

REM Verify Git status
%GIT_PATH% status

echo.
echo [1/3] Adding changes...
%GIT_PATH% add .
echo.

echo [2/3] Committing (v0.5 Babel Release)...
%GIT_PATH% commit -m "feat(v0.5): MultiLang-ASM Global Release - 27 Languages, Kids Mode, Wiki v0.5"

echo.
echo [3/3] Pushing to GitHub...
echo.
echo    Repo: https://github.com/cyberenigma-lgtm/MultiLang-ASM
echo.
%GIT_PATH% push -u origin main

echo.
echo ===========================================
echo   UPDATE COMPLETE!
echo ===========================================


