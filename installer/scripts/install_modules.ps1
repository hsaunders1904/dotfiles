$MODULES = @(
    "Color"
    "PSReadLine",
    "PowerShellGet",
    "VSSetup",
    "ZLocation",
    "posh-git",
    "pscx",
    "PSFzf"
)

foreach ($Req in ${MODULES}) {
    Install-Module "${Req}" -Scope CurrentUser -AcceptLicense -AllowClobber
}
