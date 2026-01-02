import subprocess
import os
import sys


project_root = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(project_root, "src", "main.py")
pythonw_path = sys.executable.replace("python.exe", "pythonw.exe")

#Запускаем основной скрипт в фоновом режиме
subprocess.Popen([pythonw_path, main_script],
                 creationflags=subprocess.CREATE_NO_WINDOW)