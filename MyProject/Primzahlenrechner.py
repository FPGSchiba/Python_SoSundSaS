#===============================================================================================================
# Autor: Lukas Meier
# Description: Möglichkeiten dieses Programmes
#              - Kontrollieren ob eine Zahl eine Primzahl ist
#              - Berechnen der vorherigen Primzahhl der angegebenen Zahl
#              - Berechnen der nächsten Primzahl der angegebenen Zahl
#              - Ausgeben einer Liste von allen Primzahlen bis 1000
# Date: 9.4.2020
# Version : Initial
#===============================================================================================================

def isPrimzahl(aZahl):

    isPrim = True
    if(aZahl ==2):
        isPrim = True
    else:
        isPrim = True
        obergrenze = int(aZahl/2) - 1
        for each in range(2, obergrenze + 1):
            if(each,(aZahl % each) == 0):
                isPrim = False
    return(isPrim)

def getNextPrimzahl(aZahl):
    return (aZahl)

def getPrevPrimzahl(aZahl):
    return (aZahl)

def getPrimzahlenListe():
    print()


def main():

    print('====Primzalenrechner====')
    print('+------------------------+')
    print('|1: Is it a Primzahl     |')
    print('|2: get Next Primzahl    |')
    print('|3: get Previous Primzahl|')
    print('|4: get Primzahlen List  |')
    print('|0: exit                 |')
    print('+------------------------+')


    antwort = input('Wählen sie einen Menüpunkt')
    antwort = int(antwort)
    if(antwort==1):
        isPrimzahl()
    if(antwort==2):
        getNextPrimzahl()
    if(antwort==3):
        getPrevPrimzahl()
    if(antwort==4):
        getPrimzahlenListe()
    if(antwort==0):
        print('Programende')
main()



#menu
# ist es eine Primzahl
#soll primzahl eingeben können
# somit soll es ausgeben ob es eine Primzahl ist oder nicht
# 1 ist es eine Primzahl
# menu 0 ist aufhören

#def isPrimzahl(aZahl):
 #   for i in range(1000):
  #      #isPrimzahl = aZahl/i
        #if