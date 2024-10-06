from datetime import datetime
import contestant
import pandas as pd
class contest:
    def __init__(self,round:int) -> None:
        self.round = round
        self.group_cap = 1
        self.exel_file_name = None
        self.start_time = None
        self.started = False
        self.contestants = []
        self.calculated_times_for_groups = {}
        self.calculated_times_for_competitors = {}
        self.people_in_groups = {}
        
        print(f"contest created, round {self.round}")
    def add_contestant(self,contestant:contestant.contestant):
        Already_in_game = False
        try:
            res = self.people_in_groups[contestant.group]
        except:
            res = 0
        if res < self.group_cap:
            for con_ in self.contestants:
                if con_.number == contestant.number or contestant.id == con_.id:
                    Already_in_game = True
            if not Already_in_game:
                self.contestants.append(contestant)
                contestant.accepted_for_running = True
                self.people_in_groups.update({contestant.group:1+res})
                return True
            else:
                print("already in game")
                raise RuntimeError
                
        else:
            print("no group cap for new person, change group")
            raise ValueError
    def start_competition(self):
        self.data_save_addr = f"{self.exel_file_name}{self.round}.xlsx"
        self.start_time = datetime.now()
        self.started = True
        for contestant_ in self.contestants: 
            contestant_.start_time = self.start_time
            contestant_.in_running = True
        self.save_to_xl_file(self.data_save_addr)

    def calculate_times_for_groups(self):
        self.calculated_times_for_groups ={}
        for contestant_ in self.contestants:
            try:
                res = self.calculated_times_for_groups[contestant_.group]
            except:
                res = 0
            self.calculated_times_for_groups.update({contestant_.group:\
                                                     contestant_.person_race_duration+res})
            
    def calculate_times_for_competitors(self):
        for contestant_ in self.contestants:
            if contestant_.finished_competition:
                self.calculated_times_for_competitors.update({str(contestant_.number)\
                                        +": "+contestant_.Name:contestant_.person_race_duration})
    
    def add_finished_competitor_time(self,contestant:contestant.contestant):
        if contestant.finished_competition:
            self.calculated_times_for_competitors.update({str(contestant.number)\
                                        +": "+contestant.Name:contestant.person_race_duration})
        else:
            print("not finished yet.")
            
    def calculate_people_in_groups(self):
        self.people_in_groups = {}
        for contestant_ in self.contestants:
            try:
                res = self.people_in_groups[contestant_.group]
            except:
                res = 0
            self.people_in_groups.update({contestant_.group:1+res})
    def finish_competition(self):
        for contestant_ in self.contestants:
            if contestant_.finished_competition == False:
                contestant_.finished()

        self.save_to_xl_file(self.data_save_addr)

    def return_contestant_by_id(self , id):
        for contestant_ in self.contestants:
            if contestant_.id == id:
                return contestant_ 
    def save_to_xl_file(self, addr:str):
        try:
            data_to_save = pd.DataFrame()
            for contestant_ in self.contestants:
                data_to_save = pd.concat([data_to_save,contestant_.to_pandas_DF()])
    
            data_to_save.to_excel(self.data_save_addr,index=False)
            print(f'DataFrame is written to Excel File {self.data_save_addr} successfully.')
        except:
            print("error saving file, maybe file is open.")
        