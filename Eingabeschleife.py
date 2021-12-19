Nochmal = True

while Nochmal:
    try:
        Wert = int(input("Geben Sie eine ganze Zahl ein: "))
    except ValueError:
        print("Sie müssen eine ganze Zahl eingeben!")

        try:
            Wiederholen = input("Nochmal versuchen (j/n)? ")
            
        except:
            Nochmal = False
            print("OK, bis zum nächsten Mal!")
          
            
        else:
            if (str.upper(Wiederholen) == "N"):
                Nochmal = False

    except KeyboardInterrupt:
        print("Sie habn Strg+C gedrückt!")
        print("Bis zum nächsten Mal!")
        Nochmal = False
    else:
        print(Wert)
        Nochmal = False
