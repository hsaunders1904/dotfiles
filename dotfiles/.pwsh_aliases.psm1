if (Test-Path alias:ls) {
    Remove-Alias ls
}
Set-Alias lsa Get-ChildItem
function ls() { Get-ChildItem -Exclude '.*' ${Args} }

Set-Alias addpath Add-PathVariable
Set-Alias apath Add-PathVariable
Set-Alias bak New-Backup
Set-Alias cdg Set-LocationGitRoot
Set-Alias cg Set-LocationGitRoot
Set-Alias cpath Copy-Path
Set-Alias IM Import-Module
Set-Alias IVS Import-VisualStudio
Set-Alias ipy ipython
Set-Alias notepad++ ${Env:ProgramFiles}\Notepad++\notepad++.exe
Set-Alias npp ${Env:ProgramFiles}\Notepad++\notepad++.exe
Set-Alias op Invoke-Item
Set-Alias open Invoke-Item
Set-Alias print Write-Output
Set-Alias py python
Set-Alias pyt pytest
Set-Alias pycharm Invoke-PyCharm
Set-Alias sha sha1
Set-Alias shutdown-in Invoke-ShutdownIn
Set-Alias shred sdelete
Set-Alias touch ni
Set-Alias tp Test-Path
Set-Alias VisualStudio Invoke-VisualStudio
Set-Alias vs-init New-VSCodeDir
Set-Alias zip Compress-Archive

# Typos
## git
$_GitTypos = @(
    "giot",
    "gitf",
    "gitg",
    "gitr",
    "giut",
    "giyt",
    "goit",
    "got",
    "gt",
    "gti",
    "guit",
    "gut",
    "ggit"
)
foreach ($_Typo in ${_GitTypos}) { Set-Alias ${_Typo} git }

## cd
$_CdTypos = @("cds", "dc")
foreach ($_Typo in ${_CdTypos}) { Set-Alias ${_Typo} cd }

## ls
$_LsTypos = @("kls", "ks")
foreach ($_Typo in ${_LsTypos}) { Set-Alias ${_Typo} ls }

Export-ModuleMember -Function * -Alias *
