# Der Dekorator
# Er erhält eine Funktion als Argument
def mwst_dekorator(funktion):
    # Die innere Funktion, die zurückgeliefert wird
    # Sie nimmt die Argumente der ursprünglichen Funktion entgegen
    def neue_funktion(netto_wert):
        # Den Wert modifizieren: 19% MwSt. aufschlagen
        brutto_wert = netto_wert * 1.19
        # Die ursprüngliche Funktion mit dem neuen Wert aufrufen
        funktion(brutto_wert)
    
    # Die Referenz auf die neue Funktion zurückgeben
    return neue_funktion

# Der Dekorator wird auf die nachfolgende Funktion angewendet
@mwst_dekorator
def zeige_preis(preis):
    print(f"Der Endpreis beträgt: {preis:.2f} EUR")
 
# Die dekorierte Funktion aufrufen
# Üœbergeben von den Nettowert 100. Der Dekorator macht daraus 119
zeige_preis(100.00)
# Weiteres Beispiel
zeige_preis(250.00)

