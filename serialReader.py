import serial

class serialConnector:
    def __init__(self,port:str,baudrate:int) -> None:
        try:
            self.connector = serial.Serial(\
                port=port,\
                baudrate=baudrate,\
                parity=serial.PARITY_NONE,\
                stopbits=serial.STOPBITS_ONE,\
                bytesize=serial.EIGHTBITS,\
                timeout=0)
        except:
            self.connector = None
           
    def get_ID(self):
        try:
            return int(self.connector.readline().decode()) #can be String, Integer is prefered.
        except:
            return 0 #"" if String
    def is_connected(self):
        try:
            self.connector.in_waiting
            return True
        except:
            return False

    def reconnect(self,port:str,baudrate:int):
        self.__init__(port=port,baudrate=baudrate)

