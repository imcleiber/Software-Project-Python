import csv
import matplotlib.pyplot as plt
from datetime import datetime

def activity_tracking():
    class tracker():
        def __init__(self):
            self.data = []
    
        def record(self, activity, minutes):
            time_counter = datetime.now().strftime('%m/%d %H:%M')
            recorded = {'timestamp': time_counter, 'activity': activity, 'duration': minutes}
            self.data.append(recorded)
    
        def save_progress(self, filename):
            with open(filename, 'w', newline='') as file:
                fieldnames = ['timestamp', 'activity', 'duration']
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
    
    tracking = tracker()

    while True:
        print('1 - Record an activity')
        print('2 - Check on my activities')
        print('3 - Save my progress')
        print('4 - Quit\n')

        action = input('What would you like to do? ')
        if action == '1':
            act = input('What activity are you going to do today?' )
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
            tracking.record(act, number_time)
            print('Done!')
        elif action == '2':
            tracking.plot_activities()
        elif action == '3':
            tracking.save_progress('fitness_data.csv')
        elif action == '4':
            break
        else:
            print('Select a valid option!\n')
            continue