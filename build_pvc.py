import os
import sys

sys.stdout = open("PVC_Runcard_log.txt", "w")
sys.stderr = sys.stdout
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thickness_device.settings")

from django.core.management import execute_from_command_line
execute_from_command_line(["manage.py", "runserver", "0.0.0.0:10001", "--noreload"])


"""
----------------------BUILD DJANGO TO EXE COMMAND----------------------------


pyinstaller --onefile --windowed --name=PVC_Runcard --hidden-import=django --hidden-import=sql_server.pyodbc --hidden-import=pyodbc --hidden-import=ckeditor --hidden-import=ckeditor_uploader --add-data="runcard/templates;runcard/templates" --add-data="venv;venv" build_pvc.py


-----------------------------------------------------------------------------
"""