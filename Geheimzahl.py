Eins = int(input("Geben Sie eine Zahl zwischen 1 und 10 ein: "))
Zwei = int(input("Geben Sie eine Zahl zwischen 1 und 10 ein: "))
if (Eins >= 1) and (Eins <= 10):
    if (Zwei >= 1) and (Zwei <= 10):
        print("Ihre Geheimzahl ist ", Eins * Zwei)
    else:
        print("Ungültiger zweiter Wert!")
else:
    print("Ungültiger erster Wert!")
    
