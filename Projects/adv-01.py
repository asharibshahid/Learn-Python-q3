#  Command Robo Speaker

import pyttsx3

print("Hey Welcone To My Auto Speaker")
while (True):
    s = input("Enter The Comand Which You Want Me to Speak: ")
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()
    if s == "exit":
        break

       
    print("To Exit The Program Enter exit")