import os

modules = ['pyserial','pyqtdarktheme','pyside6==6.4.1','screeninfo']
for module in modules:
    returned_value = os.system('pip install '+module)
    print('returned value:', returned_value)
print(os.system('mkdir storage'))