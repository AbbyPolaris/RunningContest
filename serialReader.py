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
        return self.connector.readline()
    def reconnect(self,port:str,baudrate:int):
        self.__init__(port=port,baudrate=baudrate)
    
