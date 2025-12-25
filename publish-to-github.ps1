# MultiLang-ASM v0.2 - GitHub Publishing Script
# Run this script to publish the project to GitHub

Write-Host "MultiLang-ASM v0.2 - GitHub Publisher" -ForegroundColor Cyan
Write-Host ""

$REPO_URL = "https://github.com/cyberenigma-lgtm/MultiLang-ASM.git"
$BRANCH = "main"

# Check if mlasm.py exists
if (-not (Test-Path "mlasm.py")) {
    Write-Host "ERROR: mlasm.py not found" -ForegroundColor Red
    Write-Host "Make sure you run this script from the MultiLang-ASM folder" -ForegroundColor Yellow
    exit 1
}

Write-Host "Directory verified" -ForegroundColor Green
Write-Host ""

# Step 1: Check Git
Write-Host "[1/6] Checking Git..." -ForegroundColor Cyan
try {
    $gitVersion = git --version
    Write-Host "   $gitVersion" -ForegroundColor Gray
}
catch {
    Write-Host "ERROR: Git is not installed" -ForegroundColor Red
    Write-Host "Download Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# Step 2: Initialize Git repository
Write-Host "[2/6] Initializing Git repository..." -ForegroundColor Cyan
if (Test-Path ".git") {
    Write-Host "   Git repository already exists" -ForegroundColor Gray
}
else {
    git init
    Write-Host "   Git repository initialized" -ForegroundColor Green
}
Write-Host ""

# Step 3: Add all files
Write-Host "[3/6] Adding files to staging..." -ForegroundColor Cyan
git add .
$numFiles = (git diff --cached --name-only | Measure-Object).Count
Write-Host "   $numFiles files added" -ForegroundColor Green
Write-Host ""

# Step 4: Create initial commit
Write-Host "[4/6] Creating initial commit..." -ForegroundColor Cyan
$commitMessage = "feat: MultiLang-ASM v0.2 - First multilingual assembler

Features:
- Support for 10 languages (ES, FR, DE, IT, AR, RU, KO, ID, ZH, JA)
- 80+ x86_64 instructions per language
- Canonical architecture with language-independent core
- Reversible mode for multilingual collaboration
- Complete documentation in 10 languages
- Integration with Make, CMake, VSCode
- 100% compatible with NASM/FASM/GAS"

git commit -m $commitMessage
Write-Host "   Commit created successfully" -ForegroundColor Green
Write-Host ""

# Step 5: Configure remote
Write-Host "[5/6] Configuring GitHub remote..." -ForegroundColor Cyan
try {
    git remote add origin $REPO_URL 2>$null
    Write-Host "   Remote 'origin' added" -ForegroundColor Green
}
catch {
    git remote set-url origin $REPO_URL
    Write-Host "   Remote 'origin' updated" -ForegroundColor Green
}
Write-Host ""

# Step 6: Push to GitHub
Write-Host "[6/6] Pushing to GitHub..." -ForegroundColor Cyan
Write-Host "   Branch: $BRANCH" -ForegroundColor Gray
Write-Host "   URL: $REPO_URL" -ForegroundColor Gray
Write-Host ""

git branch -M $BRANCH

Write-Host "   Starting push..." -ForegroundColor Yellow
git push -u origin $BRANCH

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "SUCCESS! Publication completed" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your repository is now at:" -ForegroundColor Cyan
    Write-Host "   https://github.com/cyberenigma-lgtm/MultiLang-ASM" -ForegroundColor White
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "   1. Go to GitHub and verify everything was uploaded" -ForegroundColor White
    Write-Host "   2. Create a Release v0.2 from the GitHub web interface" -ForegroundColor White
    Write-Host "   3. Configure Topics and Description" -ForegroundColor White
    Write-Host "   4. Enable Discussions" -ForegroundColor White
    Write-Host ""
    Write-Host "See detailed instructions in PUBLISHING.md" -ForegroundColor Gray
    Write-Host ""
}
else {
    Write-Host ""
    Write-Host "ERROR during push" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible causes:" -ForegroundColor Yellow
    Write-Host "   1. Repository does not exist on GitHub" -ForegroundColor White
    Write-Host "      Create it first at: https://github.com/new" -ForegroundColor Gray
    Write-Host "   2. You don't have permissions" -ForegroundColor White
    Write-Host "      Check your Git authentication" -ForegroundColor Gray
    Write-Host "   3. Repository already has commits" -ForegroundColor White
    Write-Host "      Use: git push -u origin main --force" -ForegroundColor Gray
    Write-Host ""
    exit 1
}

Write-Host "MultiLang-ASM v0.2 is now available to the world!" -ForegroundColor Cyan
Write-Host ""
