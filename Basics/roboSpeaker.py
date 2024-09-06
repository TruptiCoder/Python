import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeacker 1.1 Created by Trupti ")

    engine = pyttsx3.init()
    engine.say("Welcome to RoboSpeacker 1.1 Created by Trupti ")
    engine.runAndWait()

    engine.say("May I know your name please; Type here")
    engine.runAndWait()

    name = input("Type here: ")
    engine.say(f"Hello {name}, Glad to know you name , welcome to Robo Speaker")
    engine.runAndWait()

    engine.say("You can write here what you want me to say")
    engine.runAndWait()

    while(True):
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say(f"Bye, my friend {name}; See you next time.")
            engine.runAndWait()
            break
        command = x
        engine.say(command)
        engine.runAndWait()