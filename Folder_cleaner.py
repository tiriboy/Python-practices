from pathlib import Path
import sys
import pyinputplus

Folders_extensions = {
    'Image': ['jpg','png','jpeg', 'gif'],
    'PDF': ['pdf'],
    "Archives": ['zip', 'rar'],
    "Python Files": ['py'],
    "Text": ['txt'],
    "Word": ['docx']

}

def sorter(path):
    main_folder_path = Path(path)
    if main_folder_path.is_dir():
        for folder,extensions in Folders_extensions.items():
            folder_final_path = main_folder_path / folder
            if not folder_final_path.is_dir():
                folder_final_path.mkdir()
            data = []    
            for extentsion in extensions:
                data += main_folder_path.glob(f'*.{extentsion}')
            for d in data:
                d.rename(folder_final_path/d.name)
                print('Moved')
    else: 
        print('Invalid path')                   

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sorter(sys.argv[1])
    else:
        try:
            path = pyinputplus.inputFilepath(prompt='Enter a valid file path: ',limit=5)
            sorter(path)
        except Exception as e:
            print(e) 
        except pyinputplus.RetryLimitException:
            print('Out of attempts')       
            

        

