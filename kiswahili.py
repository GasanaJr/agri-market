import mpunga
import miwa
import majanichai
import viazi
import maharage
import ndizi
import mahindi
import mboga
import kabeji
import muhogo
def Kiswahili() :
    print("Karibu sana Agri-app")
    print("Je, wewe ni mkulima wa aina gani?")
    print("Je, wewe ni mkulima wa aina gani?") 
    print("1. Mkulima wa kiwango cha juu")
    print("2. Mkulima wa kiwango cha chini")
    print("3. Mkulima wa kawaida/kujikimu")
    mkulima = int(input("Chagua nambari kulingana na kilimo unachofanya: "))
    if (mkulima == 1) :
        print("Umechagua mkulima wa kiwango cha juu")
        print("Chagua mmea utakao")
        print("1. Mpunga")
        print("2. Miwa")
        print("3. Majani chai")
        mmea = int(input("Chagua nambari kulingana na mmea utakao: "))
        if (mmea == 1) :
            mpunga.mpunga()
        elif (mmea == 2) :
            miwa.miwa()
        elif (mmea == 3) :
            majanichai.majanichai()
    elif (mkulima == 2):
        print("Umechagua mkulima wa kiwango cha chini")
        print("1. viazi")
        print("2. maharage")
        print("3. mahindi")
        print("4. ndizi")
        mmea = int(input("Chagua nambari kulingana na mmea utakao: "))
        if (mmea == 1) :
            viazi.viazi()
        elif (mmea == 2) :
            maharage.maharage()
        elif (mmea == 3) :
            mahindi.mahindi()
        elif (mmea == 4):
            ndizi.ndizi()
    elif (mkulima == 3):
        print("Umechagua mkulima wa kawaida/kujikimu")
        print("1. mboga(sukumawiki)")
        print("2. kabeji")
        print("3. muhogo")
        mmea = int(input("Chagua nambari kulingana na mmea utakao: "))
        if (mmea == 1) :
            mboga.sukumawiki()
        elif (mmea == 2) :
            kabeji.kabeji()
        elif (mmea == 3) :
            muhogo.muhogo()
