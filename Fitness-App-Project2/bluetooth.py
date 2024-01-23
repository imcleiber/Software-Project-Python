import random

class pair_device():
    def __init__(self, device_name, access_code):
        self.device_name = device_name
        self.access_code = access_code
    def print_device(self):
        print('Device Name: ', self.device_name, 'Bluetooth Access Code: ', self.access_code)
    
class paired_devices():
    def __init__(self):
        self.devices = {}
    def pair_device(self, device, access):
        device = device.upper()
        if device in self.devices:
            print("Device alrealdy paired")
            return
        new_device = device
        new_device = pair_device(device, access)
        self.devices[f'{device}'] = new_device
    def print_devices(self):
        for dispositivos in self.devices:
            dispositivos.print_device()

class connection():
    def __init__(self):
        self.Is_connected = False
        self.device_connected = 'None'
    def connect(self, device, access, device_list):
        device = device.upper()
        for dispositivo in device_list:
            if dispositivo == device:
                break
            else:
                print('Device not found')
                return
        codigo = dispositivo
        if access == codigo:
            self.Is_connected = True
            self.device_connected = dispositivo
        else:
            print('Wrong access code')
    def disconnect(self):
        self.Is_connected = False
        self.device_connected = 'None'

while True:
    print('1 - Pair a device on Bluetooth')
    print('2 - Connect a paired device')
    print('3 - Show all connected devices')

