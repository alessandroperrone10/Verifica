#Crea una sistema ripetibile che dopo aver preso in input X parole e/o numeri e li aggiunga a una collezione, 
# si deve ripetere tante volte quante l'utente richiede e poi stampare tutti gli elementi nella lista che non si ripetono.
# Richiede: Che ogni valore o aggregazione dell'oggetto siano incapsulati 



class GestioneLista:
    #Inizializzo la lista
    def __init__(self):
        self.lista = []

    #Metodo per aggiunegre i dati alla lista
    def aggiungi_dato(self):
        ripetizione = int(input("Quanti dati mi vuoi inserire?"))
        for i in range(ripetizione):
            dato = input("Inserisci una parola o un numero che vuoi: ")
            self.lista.append(dato)
            i += 1

    #Stampo la lista, trasformata prima in un insieme per non avere duplicati
    def stampa_lista(self):
        insieme = set(self.lista)

        print(f"La lista senza duplicati è: {insieme}")



esecuzione = GestioneLista()

esecuzione.aggiungi_dato()

esecuzione.stampa_lista()