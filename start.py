import language
import english
import kiswahili
import kinyarwanda
language.language()
choice = int(input("Select choice of language: "))

if (choice == 1):
    english.english()
elif (choice == 2):
    kiswahili.Kiswahili()
elif (choice == 3):
    kinyarwanda.kinyarwanda()
