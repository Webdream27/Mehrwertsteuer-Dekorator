# Der Dekorator
# Er erh�lt eine Funktion als Argument
def mwst_dekorator(funktion):
    # Die innere Funktion, die zur�ckgeliefert wird
    # Sie nimmt die Argumente der urspr�nglichen Funktion entgegen
    def neue_funktion(netto_wert):
        # Den Wert modifizieren: 19% MwSt. aufschlagen
        brutto_wert = netto_wert * 1.19
        # Die urspr�ngliche Funktion mit dem neuen Wert aufrufen
        funktion(brutto_wert)
    
    # Die Referenz auf die neue Funktion zur�ckgeben
    return neue_funktion

# Der Dekorator wird auf die nachfolgende Funktion angewendet
@mwst_dekorator
def zeige_preis(preis):
    print(f"Der Endpreis betr�gt: {preis:.2f} EUR")
 
# Die dekorierte Funktion aufrufen
# ܜbergeben von den Nettowert 100. Der Dekorator macht daraus 119
zeige_preis(100.00)
# Weiteres Beispiel
zeige_preis(250.00)

