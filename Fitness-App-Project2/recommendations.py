def recommendations():
    class profile():
        def __init__(self, diet, training):
            self.diet = diet
            self.training = training
        
        def print_profile(self):
            print("Recommendations on diet:")
            print(self.diet)
            print()
            print("Recommendations on training:")
            print(self.training)
    
    prof = profile("","")
    while True:
        print("1 - Create a new profile")
        print("2 - Check on your profile")
        print("3 - Quit\n")

        action = input("Enter your wanted option: ")
        if action == '1':
            print("We'll need you to answer some questions in order to create your profile.")
            while True:
                answer1 = input("First of all, you want to lose or gain weight? (lose or gain)")
                answer1 = answer1.lower()
                if answer1 == 'lose':
                    decision1 = "You'll need to enter in a calorie deficit, need to consume less calories than you can burn.\n You can try search for a healthy nutrition with aliments with low calories p/gram."
                    break
                elif answer1 == 'gain':
                    decision1 = "You'll need to enter in a calorie surplus, need to consume more calories than you can burn.\n You can try search for food options which you have high calories p/gram\n Another thing you can do is eat a good amount of protein for muscle growth."
                    break  
                else:
                    print("Please, enter a valid option.\n")
            print()
            while True:
                answer2 = input("Now, when it comes to training objectives, you want to build resistance, definition to the body or grow muscle? (resistance, definition or muscle growth)")
                answer2 = answer2.lower()
                if answer2 == 'resistance':
                    decision2 = "In order to your body gain resistance, you'll need cardiovascular training.\n Choose a cardio training that you enjoy and can practice.\n To prevent injuries, you can talk to a doctor about what you can practice."
                    break
                elif answer2 == 'definition':
                    decision2 = "To maintain a muscular body with definition, you'll need to train with lower volumes of weight.\n You can try calisthenics or low weight musculation.\n Your main focus is on low volume, higher repetitions and isometrics."
                    break
                elif answer2 == 'muscle growth':
                    decision2 = "If you want to build bigger muscles, you'll need to train with higher volumes of weight and lower reps.\n It's indispensable that you rest appropriately for your body can heal and build new muscle tissues.\n It's recomendable that you consume high protein food."
                    break
                else:
                    print("Please, select a valid option.\n")
            prof = profile(decision1, decision2)
            print("Your profile is ready! select the option 2 to check our recommendations for you!\n\n")
        elif action == '2':
            prof.print_profile()
            print()
        elif action == '3':
            break
        else:
            print("Please, select a valid option")
            