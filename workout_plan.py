
while True:
    while True:
        print('1 - create a new workout plan')
        print('2 - check on your workout plan')
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
        workout = []
        for day in week:

            print("Your options are: chest, back, arms, legs, shoulders, forearms, abdomen")
            training = input(f"What would you like to train on {day.title()}? ")
            print()
            workout.append(training)
            print(f"Done! your training session has been added to your workout on {day.title()}")
    print()
    print('Your training routine is done for the week!')
    print()
    if select == '2':
        print("Here's your training routine for the week")
        count = 0
        for day in week:
            print(f"{day.title()}: {workout[count]}")
            count += 1
    if select == '3':
        break


        


