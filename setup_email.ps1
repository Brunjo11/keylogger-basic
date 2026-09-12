$Folder = "$env:USERPROFILE\file"
$PythonW = (Get-Command pythonw.exe).Source

$Action = New-ScheduledTaskAction `
    -Execute $PythonW `
    -Argument "`"$Folder\Email.pyw`"" `
    -WorkingDirectory $Folder

$Trigger = New-ScheduledTaskTrigger `
    -Daily `
    -At "10:55"

$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries

Register-ScheduledTask `
    -TaskName "PC Report Sender" `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Force
