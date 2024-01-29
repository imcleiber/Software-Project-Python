def bluetooth():
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
                access_value = int(access_value)
                if(access_value == access):
                    new_device = pair_device(device, access)
                    self.devices[f'{device}'] = new_device
                    print('Device paired succesfully!\n\n')
                else:
                    print("Wrong access code!")
        def print_devices(self):
            for dispositivos in self.devices:
                self.devices[f'{dispositivos}'].print_device()
        def unpair_device(self, unpair):
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
                print('Device connected!')
            else:
                print('Device not found')
        def disconnect(self):
            self.Is_connected = False
            self.device_connected = 'None'
            print('Device disconnected.')
        def status(self):
            if self.Is_connected == True:
                print('The Bluetooth is currently connected to a device')
                print('Device connected: ', self.device_connected)
            else:
                print('Currently, there is no device connected on Bluetooth')
        def check_device(self):
            return self.device_connected

    devices_paired = paired_devices()
    connect = connection()

    while True:
        print('\n\n')
        print('1 - Pair a device on Bluetooth')
        print('2 - Unpair device')
        print('3 - Connect a paired device')
        print('4 - Disconnect device')
        print('5 - Show the current device connected')
        print('6 - Show all paired devices')
        print('7 - Quit')

        option = input('Select and option: ')
        if option == '1':
            pair_this_device = input('Enter the device name: ')
            random_code = random.randint(1000, 9999)
            print('Working on it...\n.\n.')
            new_device = devices_paired.pair_device(pair_this_device, random_code)
            print('Done!')
        elif option == '2':
            devices_paired.print_devices()
            unpaired = input('Which device would you like to unpair? ')
            unpaired = unpaired.upper()
            current_connection = connect.check_device()
            if current_connection == unpaired:
                connect.disconnect()
            print('Working on it...\n.\n.')
        
            devices_paired.unpair_device(unpaired)
            print('Done!')
        elif option == '3':
            devices_paired.print_devices()
            connect_this_device = input('Which paired device you wish to connect? ')
            print('Working on it...\n.\n.')
            connect.connect(connect_this_device, devices_paired.devices)
        elif option == '4':
            print('Working on it...\n.\n.')
            connect.disconnect()
            print('Done!')
        elif option == '5':
            print('Working on it...\n.\n.')
            connect.status()
        elif option == '6':
            devices_paired.print_devices()
        elif option == '7':
            break
        else:
            print('Please, select a valid option!')
            continue    
