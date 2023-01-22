# Console options
$Colors = @{}
$Colors['String'] = [System.ConsoleColor]::DarkGreen
$Colors['Parameter'] = [System.ConsoleColor]::DarkCyan
Set-PSReadLineOption -Colors ${Colors}
Set-PSReadLineKeyHandler -Key Tab -Function Complete
Set-PSReadLineOption -BellStyle None

# Set the config directory environment variable
$env:DOTFILES_DIR = Split-Path "${PSScriptRoot}"

# Configure aliases and the prompt
Import-Module "${env:DOTFILES_DIR}/dotfiles/.pwsh_aliases.psm1"
Import-Module "${env:DOTFILES_DIR}/dotfiles/.pwsh_functions.psm1"
if (Get-Command oh-my-posh) {
    $env:POSH_GIT_ENABLED = $true
    $ThemesDir = "${env:DOTFILES_DIR}/apps/oh-my-posh/themes"
    $ThemeName = "multiverse-neon-custom"
    oh-my-posh init pwsh --config "${ThemesDir}\${ThemeName}.omp.json" `
        | Invoke-Expression
} else {
    Import-Module "${env:DOTFILES_DIR}/dotfiles/.pwsh_prompt.psm1"
}

# Import external modules
Import-Module Color
Import-Module posh-git
if (${PSVersionTable}.PSEdition -Eq 'Core') {
    Import-Module ZLocation  # ZLocation doesn't work in normal PowerShell
}

$env:PATH = Remove-PathDuplicates "${env:PATH}"
if (Test-Path $env:LocalAppData\Programs\fd) {
    Add-PathVariable $env:LocalAppData\Programs\fd
    if (Test-Path $env:LocalAppData\Programs\fd\autocomplete\fd.ps1) {
        . $env:LocalAppData\Programs\fd\autocomplete\fd.ps1
    }
}
