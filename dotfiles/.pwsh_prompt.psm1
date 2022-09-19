function Write-BranchName () {
    try {
        $Branch = git rev-parse --abbrev-ref HEAD 2>$null
        if ("${Branch}" -eq "") {
            # We're not in a git repo
            return
        }

        if ("${Branch}" -eq "HEAD") {
            # we're probably in detached HEAD state, so print the SHA
            $Branch = git rev-parse --short HEAD
            Write-Host " [${Branch}]" -NoNewline -ForegroundColor "Red"
        } else {
            # we're on an actual Branch, so print it
            Write-Host " [${Branch}]" -NoNewline -ForegroundColor "Magenta"
        }
    } catch {
        # we'll end up here if we're in a newly initiated git repo
        Write-Host " [No Branches]" -NoNewline -ForegroundColor "Magenta"
    }
}

function Write-CondaEnv ($Color) {
    $CondaEnv = "$env:CONDA_DEFAULT_ENV"
    if (("${CondaEnv}" -ne "") -And ("${CondaEnv}" -ne "base")) {
        Write-Host "(${CondaEnv})" -NoNewline -ForegroundColor "${Color}"
    }
}

function Write-CurrentDir ($Color) {
    $Path = "$($executionContext.SessionState.Path.CurrentLocation)"
    $Path = "${Path}" -Replace [Regex]::Escape("${env:USERPROFILE}"), "~"
    Write-Host "${Path}" -NoNewline -ForegroundColor "${Color}"
}

function Write-User ($Color) {
    Write-Host "${env:UserName}" -NoNewline -ForegroundColor "${Color}"
}

function prompt {
    $UserPrompt = "$('$' * (${NestedPromptLevel} + 1)) "
    Write-User "green"
    Write-CondaEnv "white"
    Write-Host ":" -NoNewline
    Write-CurrentDir "blue"
    Write-BranchName

    return ${UserPrompt}
}

Export-ModuleMember -Function prompt
