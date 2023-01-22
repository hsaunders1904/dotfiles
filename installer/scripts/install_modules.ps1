$MODULES = @(
    "Color"
    "PSReadLine",
    "PowerShellGet",
    "VSSetup",
    "ZLocation",
    "posh-git",
    "pscx"
)

foreach ($Req in ${MODULES}) {
    Install-Module "${Req}" -Scope CurrentUser -AcceptLicense -AllowClobber
}
