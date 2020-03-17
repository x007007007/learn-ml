import os
import subprocess
import platform


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
VENV_PATH = os.path.join(ROOT_PATH, "pytorch", "venv")

PYTORCH_PIP_PATH = os.path.join(ROOT_PATH, "pytorch", "venv", "scripts", "pip.exe")
PYTORCH_PIP_requirement = os.path.join(ROOT_PATH, "pytorch", "requirements.txt")

if not os.path.exists(VENV_PATH):
    import venv
    venv.create(VENV_PATH, with_pip=True, prompt="pytorch-venv")

install_arguments = [PYTORCH_PIP_PATH, "-r", PYTORCH_PIP_requirement]
subprocess.call(install_arguments, shell=True)

