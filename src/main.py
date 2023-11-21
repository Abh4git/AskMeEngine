# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyttsx3
import random
import keyboard
import sys


engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say("Welcome, I am Askme Engine! Your viva starts now")
questionsList =[]
already_askedList=[]
with open('questions.txt') as f:
    #[print(line) for line in f.readlines()]
    for line in f.readlines():
        questionsList.append(line)
f.close()

number_of_questions= len(questionsList)
while True:
    #try:

        if keyboard.is_pressed('c'):
            currentQuestion = questionsList[random.randint(0, number_of_questions)]
            questionsList.remove(currentQuestion)
            #number_of_questions = number_of_questions-1
            number_of_questions = number_of_questions-1
            #calready_askedList.append(currentQuestion)c
            engine.say(currentQuestion)
            engine.runAndWait()
            engine.stop()
        elif keyboard.is_pressed('ctrl+e'):

            print("\nyou pressed Esc, so exiting...")
            engine.runAndWait()
            engine.stop()
            sys.exit(0)
    #except:
     #   break





"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
#engine.save_to_file('Hello World', 'test.mp3')
#engine.runAndWait()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
