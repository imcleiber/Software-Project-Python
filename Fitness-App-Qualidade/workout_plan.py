def workout_plan():
    class day():
        def __init__(self):
            self.training = []
        
        def add_training(self, group):
            self.training.append(group)
        def remove_training(self, remove):
            self.training.remove(remove)
        def print_training(self):
            for group in self.training:
                print(group)

    class workout_plan():
        def __init__(self):
            self.week = {}
        
        def add_new_day(self, day, day_name):
            self.week[day_name] = day
        
        def print_days(self):
            for key in self.week.keys():
                print(key)
                print()
                self.week[key].print_training()
                print()

            
    
    class workouts():
        def __init__(self):
            self.workout_list = {}
            
        def add_workout(self, workout, workout_name):            
            self.workout_list[f'{workout_name}'] = workout

        def remove_workout(self, workout_name):
            if workout_name in self.workout_list():
                while True:
                    option = input(f'Are you sure you want to delete the {workout_name} workout? (yes or no)')
                    option = option.lower()
                    if option == 'yes':
                        del self.workout_list[f'{workout_name}']
                        print('Done!')
                        break
                    elif option == 'no':
                        print('Workout not removed')
                        break
                    else:
                        print('Please select a valid option!')
                        continue
            else:
                print('Workout not found')
        def list_workouts(self):
            print(list(self.workout_list.keys()))
        def print_workout(self, workout_name):
            self.workout_list[workout_name].print_days()
    
    workouts_select = workouts()

    while True:
        while True:
            print()
            print('1 - create a new workout plan')
            print('2 - check on your workouts')
            print('3 - quit')
            print()
            select = input('What do you want to do? ')
            print()
            if select == '1' or select == '2' or select == '3':
                break       
            else:
                print('choose a valid option, please')
                print()
                continue       
        week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if select == '1':
            workout_name = input('Name your new workout: ')
            if workout_name in workouts_select.workout_list:
                print('This workout name is already in use, please choose another name!')
            else:
                new_workout = workout_plan()
                for dia in week:
                    new_day = day()
                    while True:
                        print('(Type "next" to proceed to the next day)')
                        training = input(f"What would you like to train on {dia.title()}? ")
                        training = training.title()
                        print()
                        
                        if training == 'Next':
                            new_workout.add_new_day(new_day, dia)
                            break
                        else:
                            new_day.add_training(training)
                    print(f"Done! your training session has been added to your workout on {dia.title()}")
                workouts_select.add_workout(new_workout, workout_name)
                print()
                print('Your training routine is done for the week!')
                print()
                
        if select == '2':
            workouts_select.list_workouts()
            selection = input('Which one of your workouts you want to check?')
            if selection in workouts_select.workout_list:
                print()
                print('Working on it...')
                print()
                workouts_select.print_workout(selection)
            else:
                print('This workout does not exist!')
        if select == '3':
            break


        


