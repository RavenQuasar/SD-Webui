import os
import launch

os.system("bash webui.sh --use-cpu all")
launch.prepare_environment()
launch.start()
