@echo off
set "scriptPath=%~dp0run.pyw"
set "shortcutPath=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\MemoryCards.lnk"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%shortcutPath%'); $Shortcut.TargetPath = '%scriptPath%'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.Save()"

echo [Готово, вы прекрасны!]
pause