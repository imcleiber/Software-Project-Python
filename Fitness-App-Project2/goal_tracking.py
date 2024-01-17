def goal_tracking():
    class User:
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.weight = weight
            self.goals = []
    
        def add_goal(self, goal):
            self.goals.append(goal)
    
        def track_progress(self, goal, progress):
            goal.track_progress(progress)

    class Goal:
        def __init__(self, goal_type, target):
            self.goal_type = goal_type
            self.target = target
            self.progress = 0
    
        def track_progress(self, progress):
            self.progress += progress

    def view_progress(user):
        for goal in user.goals:
            print(f"{goal.goal_type} Goal: Target = {goal.target}, Progress = {goal.progress}")

    print("First of all, we need some informations about you\n")

    Lname = input("Please, enter your name: ")
    Lage = input("Please, enter your age: ")
    Lweight = input("Please, enter your current weight: ")

    user = User(name=Lname, age=Lage, weight=Lweight)

    print("Perfect! We just created your user account. Let's proceed.")

    while True:
        print("1 - Set Goal")
        print("2 - Track Progress")
        print("3 - View Progress")
        print("4 - Quit\n")

        action = input("Please, enter your choice: ")
        print()

        if action == '1':
            goal_type = input("Enter the goal type: ")
            target = float(input("Enter target: "))
            goal = Goal(goal_type, target)
            user.add_goal(goal)
            print("Goal set successfully!")

        elif action == '2':
            goal_type = input("Enter the goal type: ")
            progress = float(input("Enter  progress: "))
            for goal in user.goals:
                if goal.goal_type == goal_type:
                    user.track_progress(goal, progress)
                    print("Progress tracked successfully!")
                else:
                    print("Could not found the goal type. Please, try seeing all the goals available on the option 3 - View Progress")

        elif action == '3':
            view_progress(user)
            print()
    
        elif action == '4':
            break

        else:
            print("Please, select a valid option.")


