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
        else:
            new_device = device
            print("acess code:", access)
            access_value = input("Enter the access code: ")
            if(access_value == access):
                new_device = pair_device(device, access)
                self.devices[f'{device}'] = new_device
            else:
                print("Wrong access code!")
    def print_devices(self):
        for dispositivos in self.devices:
            dispositivos.print_device()

class connection():
    def __init__(self):
        self.Is_connected = False
        self.device_connected = 'None'
    def connect(self, device, device_list):
        device = device.upper()
        if device in device_list:
            self.Is_connected = True
            self.device_connected = device
        else:
            print('Device not found')
            return
    def disconnect(self):
        self.Is_connected = False
        self.device_connected = 'None'

while True:
    print('1 - Pair a device on Bluetooth')
    print('2 - Connect a paired device')
    print('3 - Show all connected devices')

