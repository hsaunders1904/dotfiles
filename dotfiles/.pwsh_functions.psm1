function ca { conda activate "${Args}" }
function cl($DirPath) { Set-Location "${DirPath}"; Get-ChildItem . }
function ctestD { ctest -C Debug ${Args} --output-on-failure }
function ctestR { ctest -C Release ${Args} --output-on-failure }
function l { Get-ChildItem ${Args} -Exclude ".*" }
function md5($File) { (Get-FileHash -Algorithm MD5 ${File}).Hash.ToLower() }
function mkcd($Dir) { New-Item -ItemType Directory "${Dir}"; Set-Location "${Dir}" }
function path { ${Env:PATH}.split(";") }
function sha1($File) { (Get-FileHash -Algorithm SHA1 ${File}).Hash.ToLower() }
function sha256($File) { (Get-FileHash -Algorithm SHA256 ${File}).Hash.ToLower() }
function vim($File) { ${File} = ${File} -replace "\\", "/"; bash -c "vi ${File}" }
function New-VSCodeDir() { python $(Join-Path ${Env:DOTFILES_DIR} scripts vscode_init.py) }
function which($Command) { (Get-Command ${Command} -ErrorAction SilentlyContinue).Path }

function Add-PathVariableIfExists() {
    param([string] $Path)
    if (Test-Path "${Path}" -PathType Container) {
        Add-PathVariable "${Path}"
    }
}

function Copy-Path() {
    param([string] $FilePath = "")

    if ("${FilePath}" -eq "") {
        $_AbsPath = Resolve-Path . | Select-Object -ExpandProperty Path
    } else {
        $_AbsPath = Resolve-Path "${FilePath}" | Select-Object -ExpandProperty Path
    }
    try {
        Set-Clipboard -Value "${_AbsPath}"
    } catch {
        Set-Clipboard -Text "${_AbsPath}"
    }
    Write-Host "Path '${_AbsPath}' copied to clipboard"
}

function Get-HistoryFull() {
    Get-Content (Get-PSReadLineOption).HistorySavePath
}

function Import-VisualStudio() {
    param([string] $Arch = "${Env:PROCESSOR_ARCHITECTURE}")
    Import-VisualStudioVars -Architecture "${Arch}"
}

function Invoke-PyCharm() {
    $RegKey = "HKCR\Applications\pycharm64.exe\shell\open\command"
    $Key = Get-ItemProperty -LiteralPath Registry::${RegKey}
    if (-Not ${Key}) {
        return
    }
    $Command = ${Key}."(default)"
    # Registry command has form '"<path to exe>" "%1"', so split on '" "' and
    # remove the quotes
    $ExePath = ${Command}.split(" """)[0].replace('"', '')
    Start-Process -FilePath ${ExePath} -ArgumentList ${Args}
}

function Invoke-ShutdownIn($Mins) {
    $Seconds = ${Mins} * 60
    Start-Sleep ${Seconds}; shutdown -s
}

function Invoke-VisualStudio() {
    if (-Not (Test-Command Get-VSSetupInstance)) {
        throw "Command 'Get-VSSetupInstance' does not exist. " `
            + "Is the VSSetup module installed?"
    }
    $VsInstance = Get-VSSetupInstance -All | Select-VSSetupInstance -Latest
    $DevEnvPath = Join-Path ${VsInstance}.InstallationPath "Common7\IDE\devenv.exe"
    . "${DevEnvPath}" ${Args}
}

function New-Backup() {
    param(
        [string] $Path,
        [string][Alias("o")] $OutputDir = "",
        [switch][Alias("m")] $Move = $false
    )
    if (${OutputDir}) {
        $OutPath = "$(Join-Path ${OutputDir} (Split-Path ${Path} -Leaf)).bak"
    } else {
        $OutPath = "${Path}.bak"
    }
    if (${Move}) {
        Move-Item -Path "${Path}" -Destination "${OutPath}"
    } else {
        Copy-Item -Path "${Path}" -Destination "${OutPath}"
    }
}

if (${PSVersionTable}.PSEdition -Eq "Core") {
    if (Test-Path alias:rm) {
        Remove-Alias rm
    }
    function rm {
        param(
            [switch][Alias("rf")]$RecurseForce,
            [switch][Alias("r")]$Recurse,
            [switch][Alias("f")]$Force
        )
        $RmCmd = "Remove-Item ""${Args}"""
        if (${RecurseForce}) { ${RmCmd} += " -Recurse -Force" }
        if (${Recurse}) { ${RmCmd} += " -Recurse" }
        if (${Force}) { ${RmCmd} += " -Force" }
        Invoke-Expression "${RmCmd}"
    }
}

function Remove-PathDuplicates([string]$PathString) {
    $PathList = ${PathString}.split(";")
    $NewPathList = @()
    foreach (${Path} in ${PathList}) {
        if (${Path}.trim() -and (${NewPathList} -notcontains ${Path})) {
            ${NewPathList} += ${Path}.trim()
        }
    }
    return ${NewPathList} -Join ";"
}

function Set-LocationGitRoot {
    $_RepoRoot = (git rev-parse --show-toplevel)
    if (${_RepoRoot}) {
        Set-Location ${_RepoRoot}
    }
}

function Show-Colours {
    $Colors = [enum]::GetValues([System.ConsoleColor])
    foreach ($BgColor in ${Colors}) {
        foreach ($FgColor in ${Colors}) {
            Write-Host "${FgColor}|"  -ForegroundColor ${FgColor} `
                -BackgroundColor ${BgColor} -NoNewline
        }
        Write-Host " on ${BgColor}"
    }
}

function Show-EnvVars {
    Get-ChildItem Env:* | Sort-Object name
}

function Test-Command() {
    param ([string]$Command)
    $OldActionPreference = ${ErrorActionPreference}
    $ErrorActionPreference = "Stop"
    try {
        if (Get-Command ${Command}) {
            return ${true}
        }
    } catch {
        return ${false}
    } finally {
        $ErrorActionPreference = ${OldActionPreference}
    }
}
