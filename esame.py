class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        self.w = window

    def compute (self, lista):
        media = []
        somma = 0

        #Casi particolari
        if not isinstance(lista, list):
            raise ExamException('TypeError, l\'input non è una lista')

        for el in lista:
            if not isinstance(el, int) and not isinstance(el, float):
                raise ExamException('TypeError, uno o più elementi della lista non sono int o float')

        if(len(lista) == 0):
            raise ExamException('Errore, lista vuota')

        if(len(lista)< self.w):
            raise ExamException('Errore, il numero di valori della lista non sono sufficienti')
                  

        if (self.w == 1): 
            return lista

        elif (self.w == len(lista)):
            for i in range (self.w):
                somma += lista[i]
            media.append(somma/self.w)
        
        else :
            for j in range(len(lista)-self.w+1):
                for i in range(self.w):
                    somma += lista[j+i]
                media.append(somma/self.w)   
                somma = 0

        return media        
