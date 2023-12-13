def content():
    class video():
        def __init__(self, title, URL):
            self.title = title
            self.link = URL
        def show_video(self):
            print(self.title)
            print(self.link)
    
    chest = video("COMO DESENVOLVER PEITORAL - FAÇA ISSO ! TREINO PARA INICIANTES", "https://youtu.be/0u-yvb_ruDo?si=ArBhLmfZSskElEEj")
    arms = video("TREINO DE BÍCEPS E TRÍCEPS COM RENATO CARIANI | RÁPIDO E EFICIENTE", "https://youtu.be/XwZ3QZDHPiM?si=mwiRNk747Rqb-ukD")
    back = video("COMO TREINAR DORSAIS - COSTAS COMPLETAS", "https://youtu.be/szjTZHFVWzo?si=TZcy-4m2pEHcHv4_")
    legs = video("TUDO O QUE VC PRECISA SABER, PARA AUMENTAR AS SUAS PERNAS", "https://youtu.be/6m3CnfrXp1M?si=iDQzs4FZQd0ixyR2")
    shoulders = video("Treino de ombro completo *ombro de PRO*", "https://youtu.be/CEI_jdo6e3U?si=j-O3oJwI6ELcsh3l")
    abdomen = video("Treino de abdomen *para um abdomen trincado*", "https://youtu.be/090Gwx4MqDQ?si=wGNGBmwWlz17De34")
    forearms = video("Treino de antebraço em casa *completo*", "https://youtu.be/izIG8eZIQZc?si=fg5IOZl8hFvNyVzj")

    dictionary = {'chest': chest, 'arms': arms, 'back': back, 'legs': legs, 'shoulders': shoulders, 'abdomen': abdomen, 'forearms': forearms}

    while True:
        print("Your options are: ")
        for group in dictionary:
            print(group)
        option = input("Enter the option you want to know more about: ")
        option = option.lower()
        if option in dictionary:
            print("Here are a video about you want to know:")
            content = dictionary[option]
            content.show_video()
            print()
            break
        else:
            print("Invalid option, please, enter a valid one.")
            quit = input("Do you want to quit? (yes or no)")
            quit = quit.lower()
            if quit == 'yes':
                break
            else:
                continue