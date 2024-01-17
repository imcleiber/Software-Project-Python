def nutrition():
    class food():
        # calories per gram of a food
        def __init__(self, kcalpgram):
            self.kcalpgram = kcalpgram
        # calories eaten by the quantity of food
        def calories_eaten(self, grams):
            calories = self.kcalpgram * grams
            return calories

    # creating objects with the class food
    chicken = food()
    # changing the kcalpgram from the food
    chicken.kcalpgram = 2.39
    rice = food()
    rice.kcalpgram = 1.30
    broccoli = food()
    broccoli.kcalpgram = 0.34
    bread = food()
    bread.kcalpgram = 2.65
    steak = food()
    steak.kcalpgram = 2.71
    pizza = food()
    pizza.kcalpgram = 2.66
    hamburguer = food()
    hamburguer.kcalpgram = 2.95
    fries = food()
    fries.kcalpgram = 3.12

    # Creating the dictionary with foods
    foods = {}
    # Associating keys with the object
    foods['chicken'] = chicken
    foods['rice'] = rice
    foods['broccoli'] = broccoli
    foods['bread'] = bread
    foods['steak'] = steak
    foods['pizza'] = pizza
    foods['hamburguer'] = hamburguer
    foods['fries'] = fries

    #Initial calorie = 0
    calories = 0
    while True:
        print('1 - Add food to my calorie intake')
        print('2 - Check my calorie intake')
        print('3 - Quit\n')
        action = input('What would you like to do? ')
    
        # if the user wants to add calories eated
        if action == '1':
            while True:
                eated = input('What did you eat? ')
                # puts the string on lowercase
                eated = eated.lower()
                # accesses the dictionary to find the object
                value = foods[eated]
                quantity = input('How much grams you consumed from that food? ')
                while True:
                    # checks if the quantity input is a number
                    try:
                        number = float(quantity)
                        # adds to the calories intake
                        calories_eaten = value.calories_eaten(number)
                        calories += calories_eaten
                        print()
                        print(f'You eated {calories_eaten} calories from {eated}!')
                        break
                    except ValueError:
                        print('Invalid quantity, please enter a valid number!')
                selection = input('Is that all? (yes or no) ')
                print()
                selection = selection.lower()
                if selection == 'no' or selection == 'n':
                    continue
                else:
                    break
        # if the user wants to check the calorie intake       
        elif action == '2':
            print(f'Your current calories intake is: {calories}kcal!\n')
        elif action == '3':
            break
        else:
            print('Select a valid option\n')
            continue