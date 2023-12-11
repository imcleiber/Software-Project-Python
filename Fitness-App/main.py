import nutrition
import goal_tracking
import workout_plan
import activity_tracking

print("Welcome to the Fitness App from Software Project discipline!")
print("This app was created by Cleiber de Meireles\n\n\n\n\n")
    
while True:
    print("1 - Workout Plan Creation")
    print("2 - Nutrition and Diet Tracking")
    print("3 - Activity Tracking")
    print("4 - Goal Setting and Progress Tracking")
    print("5 - Quit")

    action = input("Please, choose an option: ")
    print()
    print()

    if action == '1':
        workout_plan.workout_plan()
    elif action == '2':
        nutrition.nutrition()
    elif action == '3':
        activity_tracking.activity_tracking()
    elif action == '4':
        goal_tracking.goal_tracking()
    elif action == '5':
        break
    else:
        print("please, select a valid option")