from pathlib import Path
import sys

Folders_extensions = {
    'Image': ['jpg','png','.jpeg', '.gif'],
    'PDF': ['.pdf'],
    "Archives": ['.zip', '.rar'],
    "Python Files": ['.py'],

}
folder_final_paths = []

def sorter(path):
    folder_path = Path(path)
    if folder_path.is_dir():
        images = []
        Pdfs = []
        archives = []
        python_files = []
        for folder,extensions in Folders_extensions.items():
            folder_final_path = folder_path / folder
            if not folder_final_path.isdir():
                folder_final_path.mkdir()
                folder_final_paths.append(folder_final_path)
            data = []    
            for extentsion in extensions:
                data += folder_path.glob(extentsion)
                #continue from here

        

