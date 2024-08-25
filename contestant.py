from datetime import datetime
import pandas as pd

class contestant:
    def __init__(self,Name:str,group:int,id,number:int) -> None:
        self.Name = Name
        self.id = id
        self.number = number
        #any information about contestant can be added here.
        self.initialized_time = datetime.now()
        self.group = group
        self.start_time = None
        self.finished_time = None
        self.person_race_duration = None 
        self.accepted_for_running = False
        self.in_running = False
        self.finished_competition = False
    def change_group(self, group:int):
        self.group= group
    def finished(self):
        self.finished_time = datetime.now()
        self.person_race_duration = self.finished_time -  self.start_time
        self.in_running = False
        self.finished_competition = True

    def to_pandas_DF(self):
        return pd.DataFrame([[self.id,self.Name,self.number,self.group,self.start_time,self.finished_time]]\
                            ,columns=['ID','Name','Number','Group','Start','Finish'])

