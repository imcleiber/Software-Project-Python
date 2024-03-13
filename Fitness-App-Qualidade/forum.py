def forum():
    class post():
        def __init__(self, name, message):
            self.name = name
            self.message = message
    
    class topic():
        def __init__(self):
            self.messages = []
        def add_message(self, post):
            self.messages.append(post)
        def print_messages(self):
            for message in self.messages:
                print(message.name)
                print(message.message)
                print()
            
    
    class forum:
        def __init__(self):
            self.topics = {}
        def add_topic(self, topic_string):
            new_topic = topic_string
            new_topic = topic()
            topic_string = topic_string.title()
            self.topics[f'{topic_string}'] = new_topic
        def print_topics(self):
            for topic in self.topics:
                print(topic)


    new_forum = forum()
    new_forum.add_topic('Motivation')

    while True:
        print("1 - Post a new message")
        print("2 - Look into the topics")
        print("3 - Create a new topic")
        print("4 - Quit\n")    

        action = input("Enter your option: ")

        if action == '1':
            print("These are the topics available in the moment:")
            new_forum.print_topics()
            while True:
                
                subject = input("Enter the topic you want to post your message: ")
                subject = subject.title()
                if subject in new_forum.topics:
                    my_topic = new_forum.topics[subject]
                    name = input("Enter your name: ")
                    message = input("Enter your message: ")
                    posting = post(name, message)
                    my_topic.add_message(posting)
                    print("Message posted!")
                    break
                else:
                    print("Topic not found, please choose an existed topic or create a new one on the menu.")
        elif action == '2':
            print("These are the topics available")
            new_forum.print_topics()
            print()
            while True: 
                choose = input("Which one do you want to check? ")
                choose = choose.title()
                if choose in new_forum.topics:
                    wanted_topic = new_forum.topics[choose]
                    wanted_topic.print_messages()
                    print()
                    break
                else:
                    print("Please, select a valid topic.\n")
        elif action == '3':
            new_t = input("Enter the topic name you want to add: ")
            new_t = new_t.title()
            if new_t in new_forum.topics:
                print("This topic already exists.\n")
            else:
                new_forum.add_topic(new_t)
                print("New topic added!\n")
        elif action == '4':
            break
        else:
            print("Choose a valid option, please.")
            