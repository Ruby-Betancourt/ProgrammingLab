class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        self.w = window

        if not isinstance(self.w, int):
            raise ExamException('TypeError, la lunghezza della finestra non è un intero')

        if self.w <= 0:
            raise ExamException('Error, la lunghezza della finesta è negatova o nulla')


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
                  

        for j in range(len(lista)-self.w+1):
            somma = sum(lista[j:j+self.w])
            media.append(somma/self.w)   
        
        return media        
