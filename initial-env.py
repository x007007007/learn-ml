import os
import subprocess

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
VENV_PATH = os.path.join(ROOT_PATH, "venv")
if not os.path.exists(VENV_PATH):
    import venv
    venv.create(VENV_PATH, with_pip=True, prompt="pytorch-venv")

