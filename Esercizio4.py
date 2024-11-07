#Crea un sistema che permetta di ordinare da varie classi figlie di autofficine, 
# ogni autofficina deve avere disponibile una funzione per riparare un tipo specifico di Veicolo.   
#Richiede: Classe autofficine (min 2 figli), Classe Veicolo (min 2 figli ), Classe App_Riparazioni (gestore)



class AutoOfficina:
    def __init__(self,nome,località):
        self.nome = nome
        self.località = località
        self.aperta = False

    def apri_officina(self):
        if self.aperta == False:
            self.aperta = True
            print("L'officina ora è aperta")
        else:
            print("L'officina è gia aperta")

    def chiudi_officina(self):
        if self.aperta == True:
            self.aperta = False
            print("Hai chiuso l'officina")
        else:
            print("L'officina è già chiusa")


class AutoOfficinaPorche(AutoOfficina):
    def __init__(self, nome, località):
        super().__init__(nome, località)

    def ripara(self):
        pass

class AutoOfficinaBugatti(AutoOfficina):
    def __init__(self, nome, località):
        super().__init__(nome, località)

    def ripara(self):
        pass




class Veicolo:
    def __init__(self,modello,marca,cv):
        self.modello = modello
        self.marca = marca
        self.cv = cv


class Porche(Veicolo):
    def __init__(self, modello, marca, cv, confort, anno_fabbricazione):
        super().__init__(modello, marca, cv)
        self.confort = confort
        self.anno_fabbricazione = anno_fabbricazione


class Bugatti(Veicolo):
    def __init__(self, modello, marca, cv,velocitamassima):
        super().__init__(modello, marca, cv)
        self.velocitamassima = velocitamassima



class App_Riparazioni:
    def __init__(self):
        self.officine = []


    def aggiungi_officina(self,officina):
        self.officine.append(officina)


    def richiedi_riparazione(self,veicolo):
        pass


