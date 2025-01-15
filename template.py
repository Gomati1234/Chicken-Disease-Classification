import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='cnnClassifier'
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]




for file_path in list_of_files:
    filePath=Path(file_path) #making path to windows specific path
    file_dir,file_name=os.path.split(file_path)
    
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f" folder {file_dir} created for {file_name}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as file_obj:

# Opens the file at the path specified by filepath in write mode ("w").
# If the file does not exist, it creates a new file at the specified location.
# If the file already exists, it clears its content, making it empty.
            pass
            logging.info(f"file created for {file_name}")
    else:
        logging.info(f"{file_name} already exists")