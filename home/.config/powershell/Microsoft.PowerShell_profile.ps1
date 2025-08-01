# Environment variables
$Env:DOTFILES_DIR = Split-Path (Split-Path (Split-Path "${PSScriptRoot}"))
$Env:DOTFILES_HOME = Join-Path $Env:DOTFILES_DIR "home"
$Env:VIRTUAL_ENV_DISABLE_PROMPT = 1  # oh-my-posh deals with venv display

# Configure aliases and the prompt
Import-Module "${PSScriptRoot}/aliases.psm1"
Import-Module "${PSScriptRoot}/functions.psm1"
if (Test-Command oh-my-posh) {
    $Env:POSH_GIT_ENABLED = $true
    $ThemesDir = "${Env:DOTFILES_HOME}/.oh-my-posh/themes"
    oh-my-posh init pwsh --config "${ThemesDir}/amro-custom.omp.json" `
        | Invoke-Expression
} else {
    Import-Module "${PSScriptRoot}/prompt.psm1"
}

# Import external modules
Import-Module Terminal-Icons
Import-Module PsFzf
Import-Module posh-git
if (Test-Command zoxide) {
    Invoke-Expression (& { (zoxide init powershell | Out-String) })
}

# System path additions
$Env:PATH = Remove-PathDuplicates "${Env:PATH}"

# Console options
$Colors = @{}
$Colors['String'] = [System.ConsoleColor]::DarkGreen
$Colors['Parameter'] = [System.ConsoleColor]::DarkCyan
Set-PSReadLineOption -Colors ${Colors}
Set-PSReadLineKeyHandler -Key Tab -Function Complete
Set-PSReadLineOption -BellStyle None
Set-PsFzfOption -PSReadLineChordProvider 'Ctrl+f' -PSReadLineChordReverseHistory 'Ctrl+r'

# Set up autocomplete for some executables
function Invoke-AutoComplete() {
    param([string] $ExeName, [string] $RelativeScriptPath)
    $ExePath = (Get-Command "${ExeName}" -ErrorAction Ignore).Path
    if ("${ExePath}".Length -Gt 0) {
        $AutoComplete = Join-Path (Split-Path "${ExePath}") "${RelativeScriptPath}"
        if (Test-Path "${AutoComplete}") {
            . "${AutoComplete}"
        }
    }
}
Invoke-AutoComplete fd "autocomplete/fd.ps1"
Invoke-AutoComplete bat "autocomplete/_bat.ps1"
Invoke-AutoComplete rg "complete/_rg.ps1"
Remove-Item -Path Function:\Invoke-AutoComplete
(& pixi completion --shell powershell) | Out-String | Invoke-Expression
