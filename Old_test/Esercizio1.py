#Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata. 
# Deve poter stampare una lista singola o tutte.   
# Richiede: un oggetto come esecutore


class GestoreListe:
    #Inizializzo le liste
    def __init__(self):
        self.lista_numeri = []
        self.lista_float = []
        self.lista_stringhe = []

    #Metodo per aggiungere il dato alla lista
    def aggiungi_dato(self):
        print("Che tipo di dato vuoi inserire?")
        print("1. Numero intero")
        print("2. Numero decimale")
        print("3. Parola o frase")
        tipodidato = input("Scegli (1, 2 o 3): ")

        if tipodidato == "1":
            numero = int(input("Inserisci il numero intero: "))
            self.lista_numeri.append(numero)
            print(f"Il numero {numero} è stato aggiunto alla lista dei numeri interi.")
        elif tipodidato == "2":
            numero_float = float(input("Inserisci il numero decimale: "))
            self.lista_float.append(numero_float)
            print(f"Il numero {numero_float} è stato aggiunto alla lista dei numeri decimali.")
        elif tipodidato == "3":
            stringa = input("Inserisci la parola/frase: ")
            self.lista_stringhe.append(stringa)
            print(f"La stringa '{stringa}' è stata aggiunta alla lista delle stringhe.")
        else:
            print("Opzione non valida! Scegli correttamente.")

    #Metodo per stampare la lista
    def stampa_lista(self):
        print("Quale lista vuoi stampare?:")
        print("Digita 1 per la lista dei numeri")
        print("Digita 2 per la lista dei nuemri decimali")
        print("Digita 3 per la lista delle stringhe")
        tipo = int(input("Digita 4 per stamparle tutte: "))
        if tipo == 1:
            print("Lista dei numeri interi:", self.lista_numeri)
        elif tipo == 2:
            print("Lista dei numeri decimali:", self.lista_float)
        elif tipo == 3:
            print("Lista delle stringhe:", self.lista_stringhe)
        elif tipo == 4:
            print("Lista dei numeri interi:", self.lista_numeri)
            print("Lista dei numeri decimali:", self.lista_float)
            print("Lista delle stringhe:", self.lista_stringhe)
        else:
            print("Tipo di lista non riconosciuto.")


# Utilizzo dell'oggetto GestoreListe
gestore = GestoreListe()

#Loop per consentire all'utente di inserire quanti dati vuole
while True:
    gestore.aggiungi_dato()
    continuare = input("Vuoi inserire un altro dato? (si/no): ").lower()
    if continuare != "si":
        break

#Richiamo metodo per stampare la lista
gestore.stampa_lista()
