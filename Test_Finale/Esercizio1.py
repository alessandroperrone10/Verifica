class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

    def info_libro(self):
        print(f"Titolo: {self.titolo}")
        print(f"Autore: {self.autore}")
        print(f"Anno di pubblicazione: {self.anno}")
        print(f"Quantità: {self.quantita}\n")



class Libreria:
    def __init__(self):
        self.libri = {}

    def crea_libro(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = int(input("Inserisci l'anno di pubblicazione del libro: "))
        quantita = int(input("Inserisci la quantità del libro: "))

        if titolo in self.libri:
            print("Il libro esiste già. Aggiunta una copia.")
            self.libri[titolo].quantita += quantita
        else:
            libro = Libro(titolo, autore, anno, quantita)
            self.libri[titolo] = libro
            print("Libro creato con successo!")

    def visualizza_tutti_libri(self):
        if not self.libri:
            print("La libreria è vuota.")
        else:
            print("Tutti i libri nella libreria:")
            for libro in self.libri.values():
                libro.info_libro()

    def info_libro_per_titolo(self):
        titolo = input("Inserisci il titolo del libro: ").lower()
        for key, libro in self.libri.items():
            if key.lower() == titolo.lower(): 
                libro.info_libro()
            else:
                print("Libro non trovato!")


    def rimuovi_libro(self):
        self.visualizza_tutti_libri()
        titolo = input("Inserisci il titolo del libro da rimuovere: ").lower()
        for key in list(self.libri):  
            if key.lower() == titolo.lower():
                del self.libri[key]
                print("Libro rimosso con successo!")
            else:
                print("Libro non trovato!")

    def modifica_libro(self):
            self.visualizza_tutti_libri()
            titolo = input("Inserisci il titolo del libro da modificare: ").lower()
            for key, libro in self.libri.items():
                if key.lower() == titolo.lower():
                    campo = input("Vuoi modificare il titolo, autore, anno o quantità? ").lower()
                    if campo == "titolo":
                        nuovo_titolo = input("Inserisci il nuovo titolo: ")
                        self.libri[nuovo_titolo] = self.libri.pop(key)
                        self.libri[nuovo_titolo].titolo = nuovo_titolo
                        print("Titolo modificato con successo!")
                    elif campo == "autore":
                        nuovo_autore = input("Inserisci il nuovo autore: ")
                        libro.autore = nuovo_autore
                        print("Autore modificato con successo!")
                    elif campo == "anno":
                        nuovo_anno = int(input("Inserisci il nuovo anno di pubblicazione: "))
                        libro.anno = nuovo_anno
                        print("Anno modificato con successo!")
                    elif campo == "quantità":
                        nuova_quantita = int(input("Inserisci la nuova quantità: "))
                        libro.quantita = nuova_quantita
                        print("Quantità modificata con successo!")
                    else:
                        print("Campo non valido!")
                    return
            print("Libro non trovato!")


def main():
    libreria = Libreria()

    while True:
        print("\nBenvenuto nella libreria! Cosa vuoi fare?:")
        print("1. Aggiungere un nuovo libro")
        print("2. Visualizzare tutti i libri")
        print("3. Cercare un libro per titolo")
        print("4. Gestione libri (rimuovere, modificare)")
        print("5. Uscire dal programma")

        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            libreria.crea_libro()
        elif scelta == "2":
            libreria.visualizza_tutti_libri()
        elif scelta == "3":
            libreria.info_libro_per_titolo()
        elif scelta == "4":
            print("\nGestione libri:")
            print("1. Rimuovere un libro")
            print("2. Modifica un libro")
            scelta_gestione = input("Inserisci la tua scelta: ")

            if scelta_gestione == "1":
                libreria.rimuovi_libro()
            elif scelta_gestione == "2":
                libreria.modifica_libro()
            else:
                print("Scelta non valida.")
        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")



main()