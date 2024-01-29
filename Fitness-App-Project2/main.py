from nutrition import *
from goal_tracking import *
from workout_plan import *
from activity_tracking import *
from forum import *
from content import *
from recommendations import *
from bluetooth import *

print("Welcome to the Fitness App from Software Project discipline!")
print("This app was created by Cleiber de Meireles\n\n\n")
    
while True:
    print("1 - Workout Plan Creation")
    print("2 - Nutrition and Diet Tracking")
    print("3 - Activity Tracking")
    print("4 - Goal Setting and Progress Tracking")
    print("5 - Comunity and Forum Access")
    print("6 - Video Tutorial and Guides")
    print("7 - Personalized Recommendations")
    print("8 - Bluetooth connection")
    print("9 - Quit")

    action = input("Please, choose an option: ")
    print()
    print()

    if action == '1':
        workout_plan()
    elif action == '2':
        nutrition()
    elif action == '3':
        activity_tracking()
    elif action == '4':
        goal_tracking()
    elif action == '5':
        forum()
    elif action == '6':
        content()
    elif action == '7':
        recommendations()
    elif action == '8':
        bluetooth()
    elif action == '9':
        break
    else:
        print("Please, select a valid option")