$MODULES = @(
    "PSReadLine",
    "PowerShellGet",
    "VSSetup",
    "ZLocation",
    "posh-git",
    "pscx"
)

function Install-Requirement() {
    param ([string] $Req)

    if (Get-Module -ListAvailable -Name ${Req}) {
        Write-Output "Module '${Req}' already installed."
    } else {
        Install-Module "${Req}" -Scope CurrentUser -AcceptLicense -AllowClobber
    }
}

foreach ($Req in ${MODULES}) {
    Install-Requirement "${Req}"
}
