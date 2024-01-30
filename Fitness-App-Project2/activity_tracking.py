import csv
import matplotlib.pyplot as plt
from datetime import datetime

def activity_tracking():
    class recorder():
        def __init__(self):
            self.data = []
        
        def record(self, activity, minutes, calories_burned):
            time_counter = datetime.now().strftime('%m/%d %H:%M')
            recorded = {'timestamp': time_counter, 'activity': activity, 'duration': minutes, 'calories burned': calories_burned}
            self.data.append(recorded)

        def save_progress(self, filename):
            with open(filename, 'w', newline='') as file:
                fieldnames = ['timestamp', 'activity', 'duration', 'calories burned']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)

        def plot_activities(self):
            activities = [entry['activity'] for entry in self.data]
            durations = [entry['duration'] for entry in self.data]

            plt.plot(activities, durations, marker='o', linestyle='')
            plt.xlabel('activities')
            plt.ylabel('Duration (minutes)')
            plt.title('Fitness Activities Made')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    class tracker():
        def __init__(self):
            self._activity = ''
            self._minutes = ''
            self._calories_burned = 'not specified'

        def set_activity(self, activity):
            self._activity = activity

        def set_minutes(self, minutes):
            self._minutes = minutes

        def set_calories(self):
            self._calories_burned = self.calories_burned(self.get_minutes())
        
        def get_activity(self):
            return self._activity

        def get_minutes(self):
            return self._minutes
        
        def get_calories(self):
            return self._calories_burned

        def calories_burned(self, minutes):
            variable = 'not specified'
            return variable
    
        def record(self, record_here):
            record_here.record(self.get_activity(), self.get_minutes(), self.get_calories())
    
    class running(tracker):
        def calories_burned(self, minutes):
            burned = 11.4 * minutes
            return burned
    class cycling(tracker):
        def calories_burned(self, minutes):
            burned = 5.0 * minutes
            return burned
    class walking(tracker):
        def calories_burned(self, minutes):
            burned = 8.3 * minutes
            return burned
    class jumping(tracker):
        def calories_burned(self, minutes):
            burned = 8.33 * minutes
            return burned
    
    record_on_me = recorder()
    while True:
        print('1 - Record an activity')
        print('2 - Check on my activities')
        print('3 - Save my progress')
        print('4 - Quit\n')

        action = input('What would you like to do? ')
        if action == '1':
            act = input('What activity are you going to do today?' )
            act = act.lower()
            if(act == 'running'):
                run = running()
                while True:
                    time = input('For how much minutes?' )
                    try:
                        number_time = int(time)
                        break
                    except  number_time < 0:
                        print('Please, enter a positive number!\n')
                        continue
                    except ValueError:
                        print('Please, enter a number!\n')
                        continue
                print()
                print('Working on it...')
                run.set_activity(act)
                run.set_minutes(number_time)
                run.set_calories()
                run.record(record_on_me)
                print('Done!')
            elif(act == 'cycling'):
                bike = cycling()
                while True:
                    time = input('For how much minutes?' )
                    try:
                        number_time = int(time)
                        break
                    except  number_time < 0:
                        print('Please, enter a positive number!\n')
                        continue
                    except ValueError:
                        print('Please, enter a number!\n')
                        continue
                print()
                print('Working on it...')
                bike.set_activity(act)
                bike.set_minutes(number_time)
                bike.set_calories()
                bike.record(record_on_me)
                print('Done!')
            elif(act == 'jumping'):
                walk = walking()
                while True:
                    time = input('For how much minutes?' )
                    try:
                        number_time = int(time)
                        break
                    except  number_time < 0:
                        print('Please, enter a positive number!\n')
                        continue
                    except ValueError:
                        print('Please, enter a number!\n')
                        continue
                print()
                print('Working on it...')
                walk.set_activity(act)
                walk.set_minutes(number_time)
                walk.set_calories()
                walk.record(record_on_me)
                print('Done!')
            elif(act == 'jumping'):
                jump = jumping()
                while True:
                    time = input('For how much minutes?' )
                    try:
                        number_time = int(time)
                        break
                    except  number_time < 0:
                        print('Please, enter a positive number!\n')
                        continue
                    except ValueError:
                        print('Please, enter a number!\n')
                        continue
                print()
                print('Working on it...')
                jump.set_activity(act)
                jump.set_minutes(number_time)
                jump.set_calories()
                jump.record(record_on_me)
                print('Done!')
            else:
                tracking = tracker()
                while True:
                    time = input('For how much minutes?' )
                    try:
                        number_time = int(time)
                        break
                    except  number_time < 0:
                        print('Please, enter a positive number!\n')
                        continue
                    except ValueError:
                        print('Please, enter a number!\n')
                        continue
                print()
                print('Working on it...')
                tracking.set_activity(act)
                tracking.set_minutes(number_time)
                tracking.set_calories()
                tracking.record(record_on_me)
                print('Done!')
        elif action == '2':
            record_on_me.plot_activities()
        elif action == '3':
            record_on_me.save_progress('fitness_data.csv')
        elif action == '4':
            break
        else:
            print('Select a valid option!\n')
            continue