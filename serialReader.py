import serial
#if you know what the dataType is, you can add modify return_if_good_type function to filter bad data.

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
            Id = int(self.connector.readline().decode())
            return self.return_if_good_type(data=Id)
        except:
            return 0 #"" if String
    def is_connected(self):
        try:
            self.connector.in_waiting
            return True
        except:
            return False
    def return_if_good_type(self,data):
        return data
    def reconnect(self,port:str,baudrate:int):
        self.__init__(port=port,baudrate=baudrate)

