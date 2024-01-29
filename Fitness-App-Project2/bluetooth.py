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
    def unpair_device(self):
        self.print_devices()
        unpair = input('Which device you wish to unpair?')
        unpair = unpair.upper()
        if unpair in self.devices:
            del self.devices[f'{unpair}']
        else:
            print('the', unpair, 'device is not on the paired devices list.')

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
        print('Device disconnected.')

devices_paired = paired_devices()
connect = connection()

while True:
    print('1 - Pair a device on Bluetooth')
    print('2 - Unpair device')
    print('3 - Connect a paired device')
    print('4 - Disconnect device')
    print('5 - Show all paired devices')
    print('6 - Quit')

    option = input('Select and option: ')
    if option == '1':
        pair_this_device = input('Enter the device name: ')
        random_code = random.randint(1000, 9999)
        new_device = devices_paired.pair_device(pair_this_device, random_code)

    elif option == '2':
        devices_paired.unpair_device()
    elif option == '3':
        devices_paired.print_devices()
        connect_this_device = input('Which paired device you wish to connect? ')
        connect.connect(connect_this_device, devices_paired.devices)
    elif option == '4':
    elif option == '5':
    elif option == '6':
    else:
        print('Please, select a valid option!')
        continue    
