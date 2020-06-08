#!/usr/bin/python
import sys
import json
import requests

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    response = requests.get('http://flask-motivation-ws:5000/motivation')
    motivation = response.json()['message']
    return motivation

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
print(printExercise())
