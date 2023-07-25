import os
import launch

os.system("bash webui.sh --skip-torch-cuda-test")
launch.prepare_environment()
launch.start()
