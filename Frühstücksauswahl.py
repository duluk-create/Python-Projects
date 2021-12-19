print("1. Rührei")
print("2. Brötchen")
print("3. Croissants")
print("4. Müsli")

ErsteAuswahl = int(input("Wählen Sie ein Frühstück aus: "))

if(ErsteAuswahl == 2):
    Essen = "Brötchen"
elif (ErsteAuswahl == 3):
    Essen = "Croissants"
    
if (ErsteAuswahl == 1):
    print("1. Toast")
    print("2. Mischbrot")
    print("3. Schwarzbrot")
    print("4. Vollkorntoast")
    Brot = int(input("Wählen Sie ein Brot aus: "))

    if (Brot == 1):
        print("Sie haben Rührei mit Toast ausgewählt.")
    elif (Brot == 2):
        print("Sie haben Rührei mit Mischbrot ausgewählt.")
    elif (Brot == 3):
        print("Sie haben Rührei mit Schwarzbrot ausgewählt.")
    elif (Brot == 4):
        print("Sie haben Rührei mit Vollkorntoast ausgewählt.")
    else:
        print("Wir haben Rührei, aber diese Brotsorte haben wir nicht.")

elif (ErsteAuswahl == 2) or (ErsteAuswahl == 3):
     print("1. Iska´s Spezialmarmelade")
     print("2. Frischkäse")
     print("3. Schokocreme")

     Belag = int(input("Wählen Sie einen Belag aus: "))

     if(Belag == 1):
         print("Sie haben " + Essen + " mit Iska´s Spezialmarmelade ausgewählt.")
     elif(Belag == 2):
         print("Sie haben " + Essen + " mit Frischkäse ausgewählt.")
     elif(Belag == 3):
         print("Sie haben " + Essen + " mit Schokocreme ausgewählt.")
     else:
         print("Wir haben " + Essen + ", aber diesen Belag haben wir nicht.")



elif (ErsteAuswahl == 4):
    print("1. Haferflocken")
    print("2. Knuspermüsli")
    print("3. Spezialkreation von Lukas")

    Müsliart = int(input("Wählen Sie Ihr gewünschtes Müsli aus: "))
                   
    if  (Müsliart == 1):
        print("Sie haben sich für die Haferflocken entschieden, guten Appetit!")                     
    elif(Müsliart == 2):
        print("Sie haben sich für das Knuspermüsli entschieden, guten Appetit!")
    elif(Müsliart == 3):
        print("Sie haben sich für die Spezialkreation von Lukas entschieden, guten Appetit!")
    else:
        print("Dieses Müsli haben wir leider nicht!")          

        
        
























         
