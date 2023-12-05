
class food():
    # calories per gram of a food
    def __init__(self):
        self.kcalpgram = 0
    # calories eaten by the quantity of food
    def calories_eaten(self, grams):
        calories = self.kcalpgram * grams

# creating objects with the class food
chicken = food()
# changing the kcalpgram from the food
chicken.kcalpgram = 2.39

# Creating the dictionary with foods
foods = {}
# Associating strings with the object
foods['chicken'] = chicken
