# Set the config directory environment variable
$Env:DOTFILES_DIR = Split-Path "${PSScriptRoot}"

# Configure aliases and the prompt
Import-Module "${Env:DOTFILES_DIR}/dotfiles/.pwsh_aliases.psm1"
Import-Module "${Env:DOTFILES_DIR}/dotfiles/.pwsh_functions.psm1"
if (Get-Command oh-my-posh) {
    $Env:POSH_GIT_ENABLED = $true
    $ThemesDir = "${Env:DOTFILES_DIR}/apps/oh-my-posh/themes"
    $ThemeName = "agnoster-custom"
    oh-my-posh init pwsh --config "${ThemesDir}\${ThemeName}.omp.json" `
        | Invoke-Expression
} else {
    Import-Module "${Env:DOTFILES_DIR}/dotfiles/.pwsh_prompt.psm1"
}

# Import external modules
Import-Module Terminal-Icons
Import-Module PsFzf
Import-Module posh-git
if (Test-Command zoxide) {
    Invoke-Expression (& { (zoxide init --hook pwd powershell | Out-String) })
}

# System path additions
Add-PathVariableIfExists "${Env:LocalAppData}/Programs/fd"
$Env:PATH = Remove-PathDuplicates "${Env:PATH}"

# Console options
$Colors = @{}
$Colors['String'] = [System.ConsoleColor]::DarkGreen
$Colors['Parameter'] = [System.ConsoleColor]::DarkCyan
Set-PSReadLineOption -Colors ${Colors}
Set-PSReadLineKeyHandler -Key Tab -Function Complete
Set-PSReadLineOption -BellStyle None
Set-PsFzfOption -PSReadLineChordProvider 'Ctrl+f' -PSReadLineChordReverseHistory 'Ctrl+r'
