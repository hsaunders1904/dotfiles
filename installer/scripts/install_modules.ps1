$MODULES = @(
    "posh-git",
    "PowerShellGet",
    "pscx",
    "PSFzf",
    "PSReadLine",
    "Terminal-Icons"
    "VSSetup",
    "ZLocation",
)

foreach ($Req in ${MODULES}) {
    Install-Module "${Req}" -Scope CurrentUser -AcceptLicense -AllowClobber
}
