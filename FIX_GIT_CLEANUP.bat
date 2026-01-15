@echo off
set GIT_PATH="C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

echo ===========================================
echo   FIXING GIT REPO (Removing node_modules)
echo ===========================================

REM Unstage everything
%GIT_PATH% rm -r --cached .

REM Add everything back (respecting new .gitignore)
%GIT_PATH% add .

REM Commit cleanup
%GIT_PATH% commit -m "chore: apply gitignore and remove node_modules"

echo ===========================================
echo   REPO CLEANED!
echo ===========================================
