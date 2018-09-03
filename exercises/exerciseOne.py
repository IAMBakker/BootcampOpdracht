#!/usr/bin/python
import sys
welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!\n"

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    return None

if len(welcomeMessage) != 92:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())

motivationMessage = "Hoi, Mijn motivatie om te werken is er niet, daarom wil ik graag leren automatiseren zodat ik zo min mogelijk werk hoef te verrichten.\n" \
                    "Ik wil graag meer tijd om uit mijn neus te eten.\n" \
                    "Daarnaast ontloop ik graag mijn verantwoordelijkheden en probeer ik met mijn collega's zoveel mogelijk langs elkaar heen te praten.\n" \
                    "Door te leren automatiseren hoop ik uiteindelijk helemaal niet meer met mijn collega's te hoeven praten.\n" \
                    "\n" \
                    "Graag leer ik zo ongestructureerd mogelijk programmeren zodat de business er niets van snapt.\n" \
                    "Hopelijk denken ze dan dat ik 'vast wel weet wat ik doe' en kan ik al slapend rijk worden"



def printExercise():
    motivatie = motivationMessage
    return motivatie

if len(motivationMessage.split()) >= 150:
    sys.exit("Nice try, but not quite right :)")

print(printExercise())