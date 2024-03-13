from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
def recommendations():

    
    class Handler(ABC):
        @abstractmethod
        def handle_request(self, request: int) -> Optional[str]:
            pass

        def set_successor(self, successor: Handler) -> None:
            self.successor = successor


    class idoso(Handler):
        def handle_request(self, request: int) -> Optional[str]:
            if request > 44:
                return f"A properly designed resistance training program for older adults should include an individualized, periodized approach working toward 2–3 sets of 1–2 multijoint exercises per major muscle group, achieving intensities of 70–85% of 1 repetition maximum (1RM), 2–3 times per week, including power exercises performed at higher velocities in concentric movements with moderate intensities"
            elif self.successor:
                return self.successor.handle_request(request)
            else:
                return None

    class adulto(Handler):
        def handle_request(self, request: int) -> Optional[str]:
            if request > 17:
                return f"You are at your maximal potencial with fitness journey, just lift weights that you can lift for 8 to 10 reps in a set, listen to your coach advices for each exercise and respect your current limit to prevent injuries"
            elif self.successor:
                return self.successor.handle_request(request)
            else:
                return None

    class adolescente(Handler):
        def handle_request(self, request: int) -> Optional[str]:
            if  request > 12:
                return f"You should start slowly with lighter weights, gradually progressing to heavier loads. It’s important to maintain good form and control during all repetitions to avoid injury and make the most of a routine."
            else:
                return None
    class profile():
        def __init__(self, diet, training, age):
            self.age = age
            self.diet = diet
            self.training = training
        
        def print_profile(self):
            print("Recommendations on yout age:")
            print(self.age)
            print()
            print("Recommendations on diet:")
            print(self.diet)
            print()
            print("Recommendations on training:")
            print(self.training)

    def age_recommend(handler: Handler, request: int) -> str:
        result = handler.handle_request(request)
        if result is not None:
            return result
        else:
            return None

    handler1 = idoso()
    handler2 = adulto()
    handler3 = adolescente()
    handler1.set_successor(handler2)
    handler2.set_successor(handler3)
    prof = profile("","","")
    while True:
        print("1 - Create a new profile")
        print("2 - Check on your profile")
        print("3 - Quit\n")

        action = input("Enter your wanted option: ")
        if action == '1':
            print("We'll need you to answer some questions in order to create your profile.")
            while True:
                answer0 = input("First of all, how old are you?")
                try:
                    age = int(answer0)
                    if age < 0:
                        print("Please enter a positive number!")
                        continue
                except ValueError:
                    print("Please, enter a valid number!")
                    continue
                
                recommend_on_age = age_recommend(handler1, age)
                if recommend_on_age is not None:
                    break
                else:
                    print()
                    print("You're still a child, the best exercise is to play with your friends!")
                    print()
                    print()
                    return
                    

            while True:
                answer1 = input("Do you want to lose or gain weight? (lose or gain)")
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
            prof = profile(decision1, decision2, recommend_on_age)
            print("Your profile is ready! select the option 2 to check our recommendations for you!\n\n")
        elif action == '2':
            prof.print_profile()
            print()
        elif action == '3':
            break
        else:
            print("Please, select a valid option")
            