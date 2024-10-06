import pandas as pd
from os import listdir

class exelReader:
    def __init__(self) -> None:
        self.commulated_data = None
    def __call__(self,files_to_read:str,dir:str) -> list:
        self.commulated_data = []
        n_files_found = 0
        try:
            for file in listdir(dir):
                if file.startswith(files_to_read):
                    n_files_found += 1
                    for row in pd.read_excel(f"{dir}{file}").values:
                        self.commulated_data.append(row)
            return self.commulated_data,n_files_found
        except:
            return None