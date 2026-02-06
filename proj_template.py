
#--------------------------------------------------------------------
# This script sets up a standardized project structure for a text summarization project.
# It creates necessary directories and files to ensure consistency and organization.
#--------------------------------------------------------------------
import os
from pathlib import Path
import logging
#--------------------------------------------------------------------
# Define project structure and create directories/files
#--------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "research/trials.ipynb"
]
#--------------------------------------------------------------------
# Create directories and files
#--------------------------------------------------------------------
for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Created directory: %s", file_dir)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w',encoding='utf-8') as f:
            pass
        logging.info("Created file: %s", file_path)
    else:
        logging.info("File already exists: %s", file_path)
#--------------------------------------------------------------------