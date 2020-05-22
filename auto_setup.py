import subprocess
from pathlib import Path
from platform import system as getsystem

VIRTUAL_ENVIRONMENT_PATH = "venv"
if not Path(VIRTUAL_ENVIRONMENT_PATH).exists():
    print(f"Creating virtual environment: {VIRTUAL_ENVIRONMENT_PATH}.")
    subprocess.run(["python", "-m", VIRTUAL_ENVIRONMENT_PATH, VIRTUAL_ENVIRONMENT_PATH])

REQUIREMENTS = [
    "black",
    "flake8",
    "flake8-bandit",
    "flake8-black",
    "flake8-bugbear",
    "mypy",
    "pytest",
    "pytest-cov",
    "nox",
    "sphinx",
    "sphinx_rtd_theme",
    "sphinx-autodoc-typehints",
    "darglint",
]

print("Installing requirements.")
BASE_ACTIVATION_PATH = "venv/Scripts/activate"
environment_activation_path = Path(
    BASE_ACTIVATION_PATH + ".bat" if getsystem() == "Windows" else BASE_ACTIVATION_PATH
).absolute()

requirements = " ".join(REQUIREMENTS)
requirements_result = subprocess.run(
    f"{environment_activation_path} && pip install {requirements}"
)
print(requirements_result)

print("Finished! :)")
