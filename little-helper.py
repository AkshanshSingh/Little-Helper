import os
import pyttsx3 as pt

def actions():
    pt.speak("Press 1 to open Chrome Browser")
    pt.speak("Press 2 to open Notepad")
    pt.speak("Press 3 to open VS Code")
    pt.speak("Press 4 to open Jupyter Notebook")
    pt.speak("Press 0 to listen to the menu again")
    pt.speak("Enter your choice")

pt.speak("Choose from the following options to perform an action.")

actions()

choice = input("Enter your choice : ")

while choice == '0':
    actions()
    choice = input("Enter your choice : ")

if choice == '1':
    pt.speak("Opening Chrome Browser")
    os.system("chrome")
elif choice == '2':
    pt.speak("Opening Notepad")
    os.system("notepad")
elif choice == '3':
    pt.speak("Opening VS Code")
    os.system("code")
elif choice == '4':
    pt.speak("Opening Jupyter Notebook")
    os.system("jupyter notebook")
else:
    pt.speak("Unidentified choice")
